import math
from django.test import TestCase
from .libs.cost import CalculateCost


class CalculateBillTest(TestCase):

    def test_calculate_bill(self):
        """
        Unit test to validate CalculateCost class
        :return:
        """
        cost_per_minute = 0.09
        cost_connection = 0.36
        start_trading_period = '06:00:00'
        end_trading_period = '22:00:00'
        initial_period = '2018-05-10 21:57:13'
        final_period = '2018-05-10 22:10:56'
        calculate_cost = CalculateCost(cost_per_minute,
                                       cost_connection,
                                       start_trading_period,
                                       end_trading_period)
        bill = calculate_cost.calculate_cost_per_period(
            initial_period, final_period)
        self.assertEqual(math.ceil(bill['cost']*100)/100, 0.54)
        self.assertEqual(bill['duration'], '0:13:43')
