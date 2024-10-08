import asyncio
import random
from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from ... import *
from ...modules.helpers.events import edit_or_reply, extract_user
from ...modules.clients.clients import Client

@app.on_message(cdx("q"))
@sudo_users_only
async def quotly(bot: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Reply to any users text message")
        return

    await message.edit("Making a Quote")

    await message.reply_to_message.forward("@QuotLyBot")

    is_sticker = False
    progress = 0

    while not is_sticker:
        try:
            await sleep(4)
            msg = await bot.get_history("@QuotLyBot", 1)
            print(msg)
            is_sticker = True
        except:
            await sleep(1)

            progress += random.randint(0, 5)

            if progress > 100:
                await message.edit('There was a long running error')
                return

            try:
                await message.edit("```Making a Quote\nProcessing {}%```".format(progress))
            except:
                await message.edit("ERROR")

    if msg_id := msg[0]['message_id']:
        await asyncio.gather(
            message.delete(),
            bot.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
        )


__NAME__ = "quotly"
__MENU__ = """
`.q` - **Make Quotly.**
"""
