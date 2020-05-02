import pickle

with open("shop.pkl", "rb") as f:
    shop = pickle.load(f)

shop.display()
print(shop.receipts)
print(shop.revenue)
