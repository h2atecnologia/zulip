import datetime
import calendar
from django.utils.timezone import utc as timezone_utc

class TimezoneNotUTCException(Exception):
    pass

def verify_UTC(dt):
    # type: (datetime.datetime) -> None
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) != timezone_utc.utcoffset(dt):
        raise TimezoneNotUTCException("Datetime %s does not have a UTC timezone." % (dt,))

def floor_to_hour(dt):
    # type: (datetime.datetime) -> datetime.datetime
    return datetime.datetime(*dt.timetuple()[:4]) \
                   .replace(tzinfo=dt.tzinfo)

def floor_to_day(dt):
    # type: (datetime.datetime) -> datetime.datetime
    return datetime.datetime(*dt.timetuple()[:3]) \
                   .replace(tzinfo=dt.tzinfo)

def ceiling_to_hour(dt):
    # type: (datetime.datetime) -> datetime.datetime
    floor = floor_to_hour(dt)
    if floor == dt:
        return floor
    return floor + datetime.timedelta(hours=1)

def ceiling_to_day(dt):
    # type: (datetime.datetime) -> datetime.datetime
    floor = floor_to_day(dt)
    if floor == dt:
        return floor
    return floor + datetime.timedelta(days=1)

def timestamp_to_datetime(timestamp):
    # type: (float) -> datetime.datetime
    return datetime.datetime.fromtimestamp(float(timestamp), tz=timezone_utc)

def datetime_to_timestamp(dt):
    # type: (datetime.datetime) -> int
    verify_UTC(dt)
    return calendar.timegm(dt.timetuple())
