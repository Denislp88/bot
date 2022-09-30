#def main() -> None:
    #updater = Updater("5448621471:AAFJQxh9U1RWL21y2QT9utQB2h4QdZkiK-c")

import requests
from pyquery import PyQuery

r = requests.get("https://www.coindesk.com/price/bitcoin")
html = PyQuery(r.text)

price = html.find(".price-large").text()

print(price)






