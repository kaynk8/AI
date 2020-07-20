
import requests
def checkBitcoin():
    url = requests.get("https://blockchain.info/ticker")
    get = url.json()
    USD = get["USD"]

    sell = str(USD["sell"])
    buy = str(USD["buy"])

    print(sell)
    print(buy)

checkBitcoin(sell)
