# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime
import requests
import json
from .consts import GOOGLE_CALENDER_URL_BASE
from .exceptions import ConnectionError, JsonParseError, CalenderDoesNotExistError


class JapanHoliday(object):
    _token = None
    _CACHE_CALENDER = {}

    def __init__(self, token):
        """
        :param token: str
        """

        self._token = token

    @property
    def token(self):
        return self._token

    def today(self, weekend=False):
        """
        today is holiday
        :rtype : bool
        """
        return self.check(now=datetime.datetime.now().date(), weekend=weekend)

    def check(self, now=None, weekend=False):
        """
        the chosen day is holiday
        :type now: datetime.datetime or datetime.date
        :type weekend: bool
        :rtype : bool
        """
        if now is None:
            now = datetime.datetime.now().date()

        if type(now) == datetime.datetime:
            now = now.date()

        if weekend:
            if now.weekday() in [5, 6]:
                return True

        return self.check_date(now)

    def check_date(self, date):
        """
        :type date: datetime.date
        :rtype : bool
        """
        holiday_calender = self.get_holiday_calender(date.year)
        return date in [calender.date for calender in holiday_calender]

    def get_holiday_calender(self, year):
        """
        Get holiday from google calender
        :type year: int
        :rtype : list[date]
        """
        calender = JapanHoliday._CACHE_CALENDER.get(year)
        if calender is None:
            calender = self.get_holiday_calender_from_google(year)
            JapanHoliday._CACHE_CALENDER[year] = calender
        return calender

    def get_holiday_calender_from_google(self, year):
        """
        :type year: int
        :rtype : list[CalenderHoliday]
        """
        url = GOOGLE_CALENDER_URL_BASE.format(
            "japanese__ja@holiday.calendar.google.com",
            self.token,
            "{}-01-01T00:00:00Z".format(year),
            "{}-01-01T00:00:00Z".format(year + 1)
        )
        response = requests.get(url)
        print url

        if response.status_code != 200:
            raise ConnectionError, ConnectionError.message

        _json = json.loads(response.text)
        if 'items' not in _json:
            raise JsonParseError, JsonParseError.message
        result = [CalenderHoliday(item) for item in _json.get('items')]

        if len(result) < 2:
            raise CalenderDoesNotExistError, CalenderDoesNotExistError.message

        return result


class CalenderHoliday(object):
    _base_json = None
    holiday_name = ""
    date = None

    def __repr__(self):
        # output sample >> 勤労感謝の日:2015/11/23
        return "{}:{}/{}/{}".format(self.holiday_name,
                                    self.date.year,
                                    self.date.month,
                                    self.date.day)

    def __init__(self, _dict):
        self._base_json = None
        self.holiday_name = _dict.get('summary')
        _date_str = _dict.get('start').get('date')
        now = datetime.datetime.strptime(_date_str, '%Y-%m-%d')
        self.date = datetime.date(now.year, now.month, now.day)
