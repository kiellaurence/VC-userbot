# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from ... import *
from ...modules.helpers.events import edit_or_reply, extract_user
from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *


@app.on_message(cdx("sg"))
@sudo_users_only
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await edit_or_reply(message, "`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(message, f"`Please specify a valid user!`")
    bot = "SangMata_BOT"
    try:
        await client.send_message(bot, f"history {user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"history {user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await lol.edit(message, f"**Orang Ini Belum Pernah Mengganti Namanya**")
            return
        elif stalk:
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()

__NAME__ = "Sangmata"
__MENU__ = """
`.sg` - **Check Sangmata.**
"""
