def to_dict(data, unit):
    high_str = unit + '_high'
    low_str = unit + '_low'
    open_str = unit + '_open'
    close_str = unit + '_close'
    return {
        'high': data[high_str],
        'low': data[low_str],
        'open': data[open_str],
        'close': data[close_str]
    }