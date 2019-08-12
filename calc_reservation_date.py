#!/usr/bin/env python3

import sys
import datetime

# take target date and duration days from command line
if len(sys.argv) < 3:
    sys.exit('''
        Usage: calc_reservation_date.py <YYYY/MM/DD of target date> <duration days>
           Ex: calc_reservation_date.py 2019/12/24 90
    ''')

target_date = sys.argv[1]
duration_days = sys.argv[2]

# convert string to datetime/timedelta objects
datetime_target_date = datetime.datetime.strptime(target_date, '%Y/%m/%d')
timedelta_duration_days = datetime.timedelta(days=int(duration_days))

datetime_reservation_date = datetime_target_date - timedelta_duration_days
reservation_date = datetime_reservation_date.strftime('%Y/%m/%d (%a)')

print('''
        Make your reservation on {} !!!!
'''.format(reservation_date))