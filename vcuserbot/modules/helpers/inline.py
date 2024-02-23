import asyncio

from ... import *
from .buttons import *
from .wrapper import *
from pyrogram.types import *


async def help_menu_logo(answer):
    image = None
    if image:
        thumb_image = image
    else:
        thumb_image = "https://te.legra.ph/file/d8063209266dce7654c0d.jpg"
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="ðŸ¥€ Help Menu âœ¨",
            thumb_url=f"{thumb_image}",
            description=f"ðŸ¥€ Open Help Menu Of VC-Userbot âœ¨...",
            caption=f"""
**ðŸ¥€ Welcome To Help Menu Of
VC Userbot Â» {__version__} âœ¨...

Click On Below ðŸŒº Buttons To
Get Userbot Commands.

ðŸŒ·Powered By : [N1xDÕLL](https://t.me/DollxSpam_BOT).**
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    from ... import __version__
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultArticle(
            title="ðŸ¥€ Help Menu âœ¨",
            input_message_content=InputTextMessageContent(f"""
**ðŸ¥€ Welcome To Help Menu Of
VC Userbot Â» {__version__} âœ¨...

Click On Below ðŸŒº Buttons To
Get VC Commands.

ðŸŒ·Powered By : [ ¤N1xDÕLL](https://t.me/DollxSpam_BOT).**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def run_async_inline():
    @bot.on_inline_query()
    @inline_wrapper
    async def inline_query_handler(bot, query):
        text = query.query
        if text.startswith("help_menu_logo"):
            answer = []
            answer = await help_menu_logo(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        elif text.startswith("help_menu_text"):
            answer = []
            answer = await help_menu_text(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        else:
            return

