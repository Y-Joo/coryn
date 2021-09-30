from datetime import datetime, timedelta


def get_interval_date_times_from_unit_and_interval(unit, interval):
    now = datetime.now()
    interval_date_times = []
    if unit == 'minute':
        unit_time_delta = timedelta(minutes=1)
    elif unit == 'hour':
        unit_time_delta = timedelta(hours=1)
    elif unit == 'day':
        unit_time_delta = timedelta(days=1)
    elif unit == 'week':
        unit_time_delta = timedelta(weeks=1)
    else:
        unit_time_delta = timedelta(minutes=1)

    interval_date_time = now
    for i in range(interval):
        interval_date_times.append(interval_date_time)
        interval_date_time -= unit_time_delta
    interval_date_times.reverse()
    return interval_date_times


def to_dict(data, unit):
    high_str = unit + '_high'
    low_str = unit + '_low'
    open_str = unit + '_open'
    close_str = unit + '_close'
    return {
        'high': data[high_str],
        'low': data[low_str],
        'open': data[open_str],
        'close': data[close_str],
        'times': get_interval_date_times_from_unit_and_interval(unit, len(data[high_str].split(',')))
    }
