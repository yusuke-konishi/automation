#!/usr/bin/env python3

import sys
import datetime

# take target date and duration from command line
if len(sys.argv) < 3:
    sys.exit('''
        Usage: calc_reservation_date.py <YYYY/MM/DD of target date> <duration days>
           Ex: calc_reservation_date.py 2019/12/24 59
    ''')

target_date = sys.argv[1]
duration_days = sys.argv[2]

# TODO: translate string to datetime/timedelta objects
