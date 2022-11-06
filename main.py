import telebot
from config import TOKEN
from config import chanel_name
from config import delay
import requests
from time import sleep
from datetime import datetime
from config import admin_id

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def get_crypto_info():
    market = requests.get("https://yobit.net/api/3/ticker/eth_usd").json()
    market_buy = round(market["eth_usd"]["buy"], 2)
    market_sell = round(market["eth_usd"]["sell"], 2)

    p2p = requests.get("https://yobit.net/api/3/depth/eth_usd").json()
    p2p_buy = round(p2p["eth_usd"]["asks"][0][0], 2)
    p2p_sell = round(p2p["eth_usd"]["bids"][0][0])

    message = f"""
💳 ETH Actual course 💳

🕖TIME: {datetime.now().strftime("%H:%M:%S")}

🔰MARKET🔰
    buy: {market_buy} usd
    sell: {market_sell} usd
    
💱 P2P 💱
    buy: {p2p_buy} usd
    sell: {p2p_sell} usd
    """

    bot.send_message(chanel_name, message)


if __name__ == "__main__":
    print("Bot succcesfully started!")
    bot.send_message(admin_id, "Bot succcesfully started!")
    while True:
        get_crypto_info()
        sleep(delay)