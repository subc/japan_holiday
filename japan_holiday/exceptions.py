# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class ConnectionError(Exception):
    message = 'Failed connect to google calender api'


class JsonParseError(Exception):
    message = 'Failed parse google calender api response'


class CalenderDoesNotExistError(Exception):
    message = 'Calender data doesnt exist. Public holiday is undefined future more than 2 years'
