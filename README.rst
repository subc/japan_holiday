japan_holiday:holiday in japan from Google Calendar
====================================================

Features
--------
- 10000 call within 1 seconds

Installation
-----------------

.. code-block:: bash

    $ pip install japan_holiday

Sample Code
-----------------

.. code-block:: python

    # 今日が祝日か判定(today is holiday)
    import JapaneHoliday
    JapanHoliday(google_api_token).today()
    >>>False

    # 今日が祝日若しくは週末か判定(today is holiday or weekend)
    JapanHoliday(google_api_token).today(weekend=True)
    >>>True

    # 指定日が祝日若しくは週末か判定(the chosen day is holiday or weekend)
    from datetime import datetime
    now = datetime(2016, 1, 8, 00, 00, 00)
    JapanHoliday(google_api_token).check(now=now, weekend=True)
    >>>True

    # list
    JapanHoliday(token).get_holiday_calender(2015)
    >>>[元日:2015/1/1, 成人の日:2015/1/12, 建国記念の日:2015/2/11, 春分の日:2015/3/21, 昭和の日:2015/4/29, 憲法記念日:2015/5/3, みどりの日:2015/5/4, こどもの日:2015/5/5, 憲法記念日 振替休日:2015/5/6, 海の日:2015/7/20, 敬老の日:2015/9/21, 国民の休日:2015/9/22, 秋分の日:2015/9/23, 体育の日:2015/10/12, 文化の日:2015/11/3, 勤労感謝の日:2015/11/23, 天皇誕生日:2015/12/23]

    # test
    py.test ./tests.py
    ...

Documentation
-----------------

- get `GoogleAPI token`_

- `White Paper`_ in Qiita

.. _`GoogleAPI token`: http://www.php-factory.net/calendar_form/google_api.php
.. _`White Paper`: http://www.php-factory.net/calendar_form/google_api.php
