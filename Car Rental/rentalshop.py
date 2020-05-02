from datetime import datetime


class Shop:

    inventory = {"economy": 40, "compact": 20, "mid-size": 20, "full-size": 20}
    rental_rate = {"economy": 60, "compact": 80, "mid-size": 120, "full-size": 150}

    def __init__(self):
        self.available = Shop.inventory.copy()
        self.receipts = []
        self.customers = []
        self.revenue = 0

    def display(self):
        for i, ((type, quantity), (type, rate)) in enumerate(zip(self.available.items(), self.rental_rate.items())):
            print(f"{i+1}.{type}:")
            print(f"\tquantity: {quantity}, rental_rate: {rate}$/day")

    def generate_receipt_no(self):
        today_receipts = []
        for receipt in self.receipts:
            receipt_no = list(receipt.keys())[0]
            receipt_date = receipt_no.split("-")[0]
            if datetime.today().strftime('%m/%d/%Y') == receipt_date:
                today_receipts.append(receipt)
        return f"{datetime.today().strftime('%m/%d/%Y')}-S{len(today_receipts) + 1:04d}"


class Customer:

    def __init__(self, shop, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        shop.customers.append(self)

    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.email}"

    def request_rental(self, shop, type, quantity, duration):
        request = {"type": type, "quantity": quantity, "duratoin": f"{duration} day(s)"}
        receipt_no = shop.generate_receipt_no()
        bill = shop.rental_rate[type] * quantity * duration
        request["bill"] = f"${bill}"
        request["customer name"] = f"{self.firstname} {self.lastname}"
        request["customer email"] = self.email
        receipt = {receipt_no: request}
        shop.receipts.append(receipt)
        shop.available[type] -= quantity
        shop.revenue += bill
        return receipt_no, bill

    def request_return(self, shop, receipt_no):
        return_receipt = [receipt for receipt in shop.receipts if list(receipt.keys())[
            0] == receipt_no][0]
        shop.available[return_receipt[receipt_no]["type"]] += return_receipt[receipt_no]["quantity"]


if __name__ == "__main__":
    shop = Shop()
    shop.display()

    customer1 = Customer(shop, "Yu", "Wang", "yuwang@gmail.com")
    customer2 = Customer(shop, "Wei", "Guo", "weiguo@gmail.com")

    customer1.request_rental(shop, type="mid-size", quantity=1, duration=3)
    customer2.request_rental(shop, type="compact", quantity=2, duration=1)
    print(shop.receipts)
    shop.display()

    customer1.request_return(shop, list(customer1.receipts[0].keys())[0])
    customer2.request_return(shop, list(customer2.receipts[0].keys())[0])
    print(shop.receipts)
    shop.display()
