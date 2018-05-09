from datetime import datetime, timedelta, date
import time

FMT = "%Y-%m-%d %H:%M:%S"
FMTIME = "%H:%M:%S"


class CalculateCost(object):
    """
    Class to calculate cost of a call
    """

    def __init__(self, cost_per_minute, connection_cost, initial_period,
                 end_period):
        """
        :param cost_per_minute:
        :param connection_cost:
        :param initial_period: Initial of trading period
        :param end_period: End of trading period
        """
        self.cost_per_minute = cost_per_minute
        self.connection_cost = connection_cost
        self.initial_period = initial_period
        self.end_period = end_period
        CalculateCost.validate_datetime(self.initial_period, '%H:%M:%S')
        CalculateCost.validate_datetime(self.end_period, '%H:%M:%S')

    @staticmethod
    def duration_of_call(initial_date, final_date):
        """
        Function to calculate a duration of call
        :param initial_date:
        :param final_date:
        :return:
        """
        t1 = datetime.strptime(initial_date, FMT)
        t2 = datetime.strptime(final_date, FMT)
        t1_ts = time.mktime(t1.timetuple())
        t2_ts = time.mktime(t2.timetuple())
        total_minutes, s = divmod(t2_ts - t1_ts, 60)
        h, m = divmod(total_minutes, 60)
        return {"hour": h, "minutes": int(m), "seconds": s, "t1": t1, "t2": t2,
                "total_minutes": int(total_minutes)}

    @staticmethod
    def validate_datetime(date_text, pattern='%Y-%m-%d %H:%M:%S'):
        try:
            datetime.strptime(date_text, pattern)
        except ValueError:
            raise ValueError("Incorrect format, should be %s" % pattern)

    def calculate_cost_per_period(self, initial_date, final_date):
        """
        Function to return a cost of call
        :param initial_date: datetime %Y-%m-%d %H:%M:%S
        :param final_date: datetime %Y-%m-%d %H:%M:%S
        :return:
        """
        try:
            CalculateCost.validate_datetime(initial_date, '%Y-%m-%d %H:%M:%S')
            CalculateCost.validate_datetime(final_date, '%Y-%m-%d %H:%M:%S')
            call_duration = CalculateCost.duration_of_call(initial_date,
                                                           final_date)
            t1 = call_duration["t1"]
            t2 = call_duration["t2"]
            total_minutes = call_duration["total_minutes"]
            minutes = call_duration["minutes"]
            hour = call_duration["hour"]
            seconds = call_duration["seconds"]
            start_ot = datetime.strptime(
                self.initial_period + " {}".format(t1.date()),
                "%H:%M:%S %Y-%m-%d") - timedelta(days=1)
            end_ot = datetime.strptime(
                self.end_period + " {}".format(t2.date()),
                "%H:%M:%S %Y-%m-%d") + timedelta(days=1)
            total_pay = self.connection_cost
            for x in range(total_minutes):
                t1 += timedelta(minutes=1)
                if t1 < t2 and start_ot.time() < t1.time() < end_ot.time():
                    total_pay += self.cost_per_minute

            return {"cost": total_pay,
                    "duration": "%d:%02d:%02d" % (hour, minutes, seconds)}
        except Exception as e:
            raise e
