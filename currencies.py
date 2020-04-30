class Ccy:

    exchange_rate = {"USD": 1, "GBP": 0.8, "EUR": 0.9, "JPY": 106.54, "CAD": 1.39}

    def __init__(self, amount, unit="EUR"):
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f"{self.amount:.2f} {self.unit}"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Ccy(other, "EUR")
        other = Ccy(other.amount*Ccy.exchange_rate[self.unit] /
                    Ccy.exchange_rate[other.unit], self.unit)
        amount = self.amount + other.amount
        unit = self.unit
        return Ccy(amount, unit)

    def __radd__(self, other):
        return Ccy.__add__(self, other)


if __name__ == "__main__":
    v1 = Ccy(23.43, "EUR")
    v2 = Ccy(19.97, "USD")
    print(v1 + v2)
    print(v2 + v1)
    print(v1 + 3)
    print(v2 + 3)
    print(3 + v2)

    # x = Ccy(10, "USD")
    # y = Ccy(11)
    # z = Ccy(12.34, "JPY")
    # z = 7.8 + x + y + 255 + z
    # print(z)
    #
    # lst = [Ccy(10, "USD"), Ccy(11), Ccy(12.34, "JPY"), Ccy(12.34, "CAD")]
    #
    # z = sum(lst)
    #
    # print(z)
