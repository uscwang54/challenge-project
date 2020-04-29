class Calendar:

    @staticmethod
    def is_leap_year(year):
        '''return True if leap year
        False if otherwise'''
        if year % 400 == 0:
            return True
        elif year % 400 != 0 and year % 100 == 0:
            return False
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @property
    def date(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @date.setter
    def date(self, datestr):
        self.year, self.month, self.day = [int(part) for part in datestr.split("-", 2)]

    def advance(self):
        '''advance by 1 day'''
        if not Calendar.is_leap_year(self.year):
            day_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        else:
            day_in_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        days = day_in_month[self.month - 1]
        if self.day == days:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1


if __name__ == "__main__":
    calendar = Calendar(2020, 4, 29)
    print(calendar.date)

    calendar.date = "2019-2-28"
    print(calendar.date)
    calendar.advance()
    print(calendar.date)
    calendar.advance()
    print(calendar.date)

    calendar.date = "2019-12-30"
    print(calendar.date)
    calendar.advance()
    print(calendar.date)
    calendar.advance()
    print(calendar.date)

    calendar.date = "2020-2-28"
    print(calendar.date)
    calendar.advance()
    print(calendar.date)
    calendar.advance()
    print(calendar.date)
