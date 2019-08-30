"""
Being aware of pytz library, it is a library which goal is to provide easy
way to time-space awareness and time relation to somehow never fully defined
`now`as it is relative to place and the `now` of others.
"""

from datetime import timezone, datetime, timedelta


class TimeMachine:

    def __init__(self):
        """
        It starts with setting itself in the time space by getting what
        means `now` for UTC place.
        """
        self.my_now = self.get_utc()
        self.rel_now = self.get_utc()
        self.my_time_offset = 0
        self.rel_time_offset = 0

    def get_utc(self):
        """
        Gets current time position in space of UTC.

        :return: utc datetime
        """
        return datetime.utcnow()

    def move_timezones(self, time_offset):
        """
        Sets move in space in timezones.

        :param time_offset:
        :return:
        """
        self.my_time_offset = time_offset

        return self.my_now.now(timezone(timedelta(hours=self.my_time_offset)))

    def set_timezone(self, tz_name):
        """
        Sets move in space in timezones.

        :param tz_name:
        :return:
        """
        # TODO: timezone setting with dateutils

    def set_now(self, **kwargs):
        """
        Sets 'now' as date time in a time space.

        :param **kwargs: keyword arguments
        """
        keys = ['year', 'month', 'day', 'hour', 'minute', 'second']

        if keys-kwargs.keys():
           raise Exception(
               "You can only provide followings keys {}".format_map(keys)
           )

        self.my_now = self.my_now.replace(**kwargs)

    def get_now(self):
        return self.my_now

    def generate_now(self):
        """
        Generates current moment on request
        """
        self.my_now = datetime.today()

    def back_days_periods(self, days, periods=1, today_aware=False):
        """
        Generates period inlcuding or not current day but counting full days
        except current.

        :param days: how many days in the past
        :param periods: number of adequate periods to attach
        :param today_aware: if consider today as first day
        :return: list of tuple with current point in time and days
        """

        period_spans = []
        start = self.my_now
        for period in range(periods):
            period = self.back_days_period(
                days, start_point=start, today_aware=today_aware
            )
            start = period[1]
            period_spans.append(period)
        return period_spans

    def back_days_period(self, days, start_point=None, today_aware=False):
        """
        Generates period including or not current day but counting full days
        except current.

        :param days: how many days in the past
        :param start_point: the pointe from which it counts
        :param today_aware: if consider today as first day
        :return: tuple with current point in time and days
        """

        if not start_point:
            start_point = self.my_now

        move = timedelta(days=days-1 if today_aware else days)
        if days > 0:
            return start_point.replace(
                hour=0, minute=0, second=0
            ) - move, start_point
        else:
            return start_point, start_point.replace(
                hour=23, minute=59, second=59
            ) + move
