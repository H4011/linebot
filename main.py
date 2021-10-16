from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
import requests
from bs4 import BeautifulSoup

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

load_url = os.environ["URL"]
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
soup = str(soup).replace('<br>','・')
soup2 = soup[:-1].split('・')

for i in soup2:
    line_bot_api.push_message(i, TextSendMessage(text="test"))
