class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def toInt(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def toTime(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)

    def incTime(self, seconds):
        seconds += self.toInt()
        self.toTime(seconds)

    def __add__(self, other):
        seconds = self.toInt() + other.toInt()
        return intToTime(seconds)


def intToTime(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def funcTimeInit():
    time = Time()
    time.printTime()

    time1 = Time(9, 45)
    time1.printTime()


def methodStr():
    start1 = Time(9, 55)
    print(start1)
