import schedule as schedule


def scheduler(function, time):
    def inner():
        schedule.every(time).seconds.do(function)
        return

    return inner