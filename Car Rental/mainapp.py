import os
import pickle
from rentalshop import Shop, Customer

if "shop.pkl" not in os.listdir():
    shop = Shop()
else:
    with open("shop.pkl", "rb") as f:
        shop = pickle.load(f)

car_types = {1: "economy", 2: "compact", 3: "mid-size", 4: "full-size"}
print("Welcome to the car rental app.")

stay = True
while stay:
    isreturning = input("Are you a returning customer? (y/n) ")
    if isreturning == 'y':
        email = input("What's your email address? ")
        for customer in shop.customers:
            if email == customer.email:
                returning_customer = customer
                break
        print(f"Welcome, {returning_customer.firstname}!")
        while True:
            print("You can choose the following services.")
            print("1. Request a car rental.")
            print("2. Return a rental car")
            choose = int(input("What service do you want to do? "))
            if choose == 1:
                print("Our shop has the following cars.")
                shop.display()
                type = int(input("What type of cars do you want (choose 1,2,3,4)? "))
                quantity = int(input("How many cars do you need? "))
                duration = int(input("How many days do you need the car(s)? "))
                receipt_no, bill = returning_customer.request_rental(
                    shop, car_types[type], quantity, duration)
                print(f"OK. Your bill total is ${bill}, and your receipt number is {receipt_no}")
                isstay = input("Do you need anything else? (y/n) ")
                if isstay == 'y':
                    continue
                else:
                    print("Thank you for using our car rental app!")
                    with open("shop.pkl", "wb") as f:
                        pickle.dump(shop, f)
                    stay = False
                    break
            elif choose == 2:
                receipt_no = input("OK. What's your receipt_no? ")
                returning_customer.request_return(shop, receipt_no)
                print("Thank you for returning your car.")
                isstay = input("Do you need anything else? (y/n) ")
                if isstay == 'y':
                    continue
                else:
                    print("Thank you for using our car rental app!")
                    with open("shop.pkl", "wb") as f:
                        pickle.dump(shop, f)
                    stay = False
                    break

    else:
        firstname = input("What's your first name?: ")
        lastname = input("What's your last name?: ")
        email = input("What's your email address?: ")
        print("Thank you for registering.")
        new_customer = Customer(shop, firstname, lastname, email)
        while True:
            print("Our shop has the following cars.")
            shop.display()
            type = int(input("What type of cars do you want (choose 1,2,3,4)? "))
            quantity = int(input("How many cars do you need? "))
            duration = int(input("How many days do you need the car(s)? "))
            receipt_no, bill = new_customer.request_rental(
                shop, car_types[type], quantity, duration)
            print(f"OK. Your bill total is ${bill}, and your receipt number is {receipt_no}")
            isstay = input("Do you need anything else? (y/n) ")
            if isstay == 'y':
                continue
            else:
                print("Thank you for using our car rental app!")
                with open("shop.pkl", "wb") as f:
                    pickle.dump(shop, f)
                stay = False
                break
