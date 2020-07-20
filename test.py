import requests
import json

def checkBitcoin():
    url = requests.get("https://blockchain.info/ticker")
    get = url.json()
    USD = get["USD"]

    sell = str(USD["sell"])
    buy = str(USD["buy"])

    check = input("Type 'sell' or 'buy: ")

    if check == "sell":
        print("sell: " + sell)
    elif check == "buy":
        print("buy: " + buy)
    else:
        print("No data")

checkBitcoin()

print()