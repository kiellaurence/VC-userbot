from ... import *
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    title = message.chat.title
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await eor(message, f"**Pinged !\nLatency:** `{ms}` ms\n**On Chat:** `{title}`")



__NAME__ = "Ping"
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**
"""
