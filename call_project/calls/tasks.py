from call_project.celery import app

from .cost import CalculateCost
from .models import Cost, STATUS, Bill, Call


@app.task(name='generate_bill', bind=True)
def generate_bill(self, call_id):
    """
    Calculate and generate a Bill
    :param call_id:
    :return:
    """
    # TODO: send excptions to Sentry, NewRelic, Graylog
    try:
        calls = Call.objects.filter(call_id=call_id).order_by('call_type')
        cost = Cost.objects.get(status=STATUS[0][0])
        if not calls:
            raise ValueError("Call doesn't not exist.")

        if calls.count() == 1:
            raise self.retry(countdown=15)

        calculate_cost = CalculateCost(cost.cost_per_minute,
                                       cost.connection_cost,
                                       str(cost.initial_period),
                                       str(cost.end_period))
        calculate_bill = calculate_cost.calculate_cost_per_period(
            str(calls[0].timestamp)[0:19], str(calls[1].timestamp)[0:19])
        Bill.objects.create(destination=calls[1].destination,
                            source=calls[1].source,
                            call_id=calls.last().call_id,
                            call_start_date=str(calls[0].timestamp)[0:10],
                            call_start_time=str(calls[0].timestamp)[11:19],
                            call_price=float(calculate_bill['cost']),
                            duration=calculate_bill['duration'])

    except Cost.DoesNotExist as exc:
        raise self.retry(exc=exc, countdown=15)
