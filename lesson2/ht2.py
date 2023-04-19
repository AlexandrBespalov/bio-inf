class Time:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def __str__(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def __add__(self, other):
        return Time(self.seconds + other.seconds)

    def incTime(self, seconds):
        self.seconds += seconds
