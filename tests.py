# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from builtins import range
import pytest
from pit import Pit
from japan_holiday import JapanHoliday
from japan_holiday.exceptions import CalenderDoesNotExistError
import datetime
import time
import random


def test_japan_holiday():
    token = Pit.get('google.api').get('token')

    japan_holiday = JapanHoliday(token)
    japan_holiday.get_holiday_calender(2015)
    # 2015/10/12[Mon] is 体育の日
    assert japan_holiday.check(now=datetime.datetime(2015, 10, 12, 0, 0, 0)) is True
    assert japan_holiday.check(now=datetime.datetime(2015, 10, 13, 0, 0, 0)) is False
    assert japan_holiday.check(now=datetime.datetime(2015, 10, 11, 0, 0, 0), weekend=False) is False
    assert japan_holiday.check(now=datetime.datetime(2015, 10, 11, 0, 0, 0), weekend=True) is True

    japan_holiday.check(now=datetime.datetime(2016, 10, 2, 0, 0, 0))
    assert type(japan_holiday.today()) == bool
    japan_holiday.today(weekend=True)
    japan_holiday.check()
    japan_holiday.check(now=datetime.datetime(2016, 10, 2, 0, 0, 0))
    japan_holiday.check(now=datetime.datetime(2016, 10, 2, 0, 0, 0), weekend=True)

    # 10000call Within 1 second
    ts = time.time()
    for x in range(10000):
        JapanHoliday(token).check(now=datetime.datetime(2016, random.randint(1, 12), 2, 0, 0, 0))
    te = time.time()
    assert te - ts < 1, te - ts

    with pytest.raises(CalenderDoesNotExistError):
        japan_holiday.get_holiday_calender(2017)
