class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    @time.setter
    def time(self, timestr):
        hours, minutes, seconds = [int(part) for part in timestr.split(":", 2)]
        if 0 <= hours and hours < 24:
            self.hours = hours
        else:
            raise TypeError("Hours have to be between 0 and 23.")
        if 0 <= minutes and minutes < 60:
            self.minutes = minutes
        else:
            raise TypeError("Minutes have to be between 0 and 59.")
        if 0 <= seconds and seconds < 60:
            self.seconds = seconds
        else:
            raise TypeError("Seconds have to be between 0 and 59.")

    def tick(self):
        if self.hours < 23:
            if self.minutes < 59:
                if self.seconds < 59:
                    self.seconds += 1
                else:
                    self.seconds = 0
                    self.minutes += 1
            else:
                self.seconds = 0
                self.minutes = 0
                self.hours += 1
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0


if __name__ == "__main__":
    clock = Clock(9, 15, 0)
    print(clock.time)

    clock.time = "10:25:30"
    print(clock.time)
    clock.tick()
    print(clock.time)

    clock.time = "10:25:59"
    print(clock.time)
    clock.tick()
    print(clock.time)

    clock.time = "11:59:59"
    print(clock.time)
    clock.tick()
    print(clock.time)

    clock.time = "23:59:59"
    print(clock.time)
    clock.tick()
    print(clock.time)
    clock.tick()
    print(clock.time)
