from ... import *
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    title = message.chat.title
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await eor(message, f"""<b>Pinged !</b>\n<b>Latency:</b> `{ms}` ms\n<b>On Chat:</b> <code>`{title}`<\code>\n</b>Owner: </b> <a href='tg://user?id=6965945364'>k</a>""")



__NAME__ = "Ping"
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**
"""
