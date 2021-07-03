from static import StaticInfo


def choose_period():
    period = None
    while period not in StaticInfo.periods:
        period = input('give period: {h for help list}')
        if period == 'h':
            print(StaticInfo.periods)
        elif period not in StaticInfo.periods:
            print('wrong period: h to get list of periods')
        else:
            continue
    return period


def choose_interval():
    interval = None
    while interval not in StaticInfo.intervals:
        interval = input('give interval: {h for help list}')
        if interval == 'h':
            print(StaticInfo.intervals)
        elif interval not in StaticInfo.intervals:
            print('wrong interval: h to get list of intervals')
        else:
            continue
    return interval
