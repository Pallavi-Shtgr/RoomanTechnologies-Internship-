"""Day 05 MODULES AND LIBRARIES """

# Write a Python function get_current_datetime() -> dict that returns a dictionary containing:
# The current date.
# The current time.
# The current date and time formatted as YYYY-MM-DD HH:MM:SS.

import datetime

def get_current_datetime() -> dict:
    result = {}
    now = datetime.datetime.now()

    result['current_date'] = now.date()
    result['current_time'] = now.time()

    result['formatted_datetime'] = now.strftime('%Y-%m-%d %H:%M:%S')
    return result
