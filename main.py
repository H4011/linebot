from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main():
    user_id = os.environ["LINE_MY_USERID"]

    messages = TextSendMessage(text=f"test")
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    main()
