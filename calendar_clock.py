from clock import Clock
from calendar import Calendar


class CalendarClock(Clock, Calendar):
    '''multiple inheritance from both Clock and Calendar'''

    def __init__(self, year, month, day, hours, minutes, seconds):
        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, year, month, day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d} {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def move(self):
        previous_hours = self.hours
        self.tick()
        hours_after_tick = self.hours
        if hours_after_tick < previous_hours:
            self.advance()


if __name__ == "__main__":

    x = CalendarClock(2013, 12, 31, 23, 59, 59)
    print("One move from ", x, end=" ")
    x.move()
    print("to ", x)

    x = CalendarClock(1900, 2, 28, 23, 59, 59)
    print("One move from ", x, end=" ")
    x.move()
    print("to ", x)

    x = CalendarClock(2000, 2, 28, 23, 59, 59)
    print("One move from ", x, end=" ")
    x.move()
    print("to ", x)

    x = CalendarClock(2013, 2, 7, 13, 55, 40)
    print("One move from ", x, end=" ")
    x.move()
    print("to ", x)
