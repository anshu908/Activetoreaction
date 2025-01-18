import random
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from nexichat.database.chats import add_served_chat
from nexichat.database.users import add_served_user
from config import MONGO_URL
from nexichat import nexichat, mongo
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery
import asyncio
import config
from nexichat import LOGGER, nexichat, db
from nexichat.modules.helpers import (
    ABOUT_BTN,
    CLONEHELP_READ,
    STARTWEL,
    ABOUT_READ,
    ADMIN_READ,
    BACK,
    CHATBOT_BACK,
    CHATBOT_READ,
    DEV_OP,
    HELP_BTN,
    HELP_READ,
    MUSIC_BACK_BTN,
    START,
    TOOLS_DATA_READ,
    
)


@nexichat.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    bot_id = client.me.id
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )
#-----------------------Testing call back-----------------------------#

#cloner wala 

elif query.data == "CLONE":
    await query.message.edit(
        text=CLONEHELP_READ,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(CLONEBACK, callback_data='back')]])
    )


#Start back

elif query.data == "STARTCLONE":
        await query.message.edit(
            text=STARTWEL,
            reply_markup=InlineKeyboardButton(WELSTART_BOT),
        )

    
#----------------------------------------------------------#   
    elif query.data == "CLOSE":
        await query.message.delete()
        await query.answer("Closed menu!", show_alert=True)
    elif query.data == "BACK":
        await query.message.edit(
            text=START,
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    
    elif query.data == "ABOUT":
        await query.message.edit(
            text=ABOUT_READ,
            reply_markup=InlineKeyboardMarkup(ABOUT_BTN),
            disable_web_page_preview=True,
        )
    elif query.data == "ADMINS":
        await query.message.edit(
            text=ADMIN_READ,
            reply_markup=InlineKeyboardMarkup(MUSIC_BACK_BTN),
        )
    elif query.data == "TOOLS_DATA":
        await query.message.edit(
            text=TOOLS_DATA_READ,
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif query.data == "BACK_HELP":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif query.data == "CHATBOT_CMD":
        await query.message.edit(
            text=CHATBOT_READ,
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif query.data == "CHATBOT_BACK":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    
    
