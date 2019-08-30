from datetime import datetime
from unittest import TestCase

from time_machine import TimeMachine


class TestPeriods(TestCase):

    def setUp(self):
        self.tm = TimeMachine()

    def test_set_timezone(self):
        self.skipTest("Not yest implemented")

        utc_place = self.tm.get_utc()
        current_place = self.tm.move_timezones(3)
        self.assertEqual(current_place-utc_place, 3)

    def test_back_in_23_days(self):
        days = 23

        # to have fixed now
        self.tm.set_now(year=2019, month=8, day=30, hour=0, minute=0, second=0)

        # makes sure now is what was set
        self.assertEqual(
            '2019-08-30 00:00:00',
            self.tm.get_now().strftime('%Y-%m-%d %H:%M:%S')
        )

        # checks if created period has correct boundaries
        date_from, date_to = self.tm.back_days_period(days=days)
        self.assertEqual(
            '2019-08-30 00:00:00', date_to.strftime('%Y-%m-%d %H:%M:%S')
        )
        self.assertEqual(
            '2019-08-07 00:00:00', date_from.strftime('%Y-%m-%d %H:%M:%S')
        )


