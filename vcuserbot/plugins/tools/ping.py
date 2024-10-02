from ... import *
import requests
import time
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await eor(message, f"""<b>Pinged !</b>\n<b>Latency:</b> `{ms}` ms\n<b>On Chat:</b> `{title}`\n<b>Owner:</b> <a href='tg://user?id=8109165166'>k</a>""")



__NAME__ = "Ping"
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**
"""
