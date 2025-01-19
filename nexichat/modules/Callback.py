import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from nexichat import nexichat

# Dummy variables to avoid undefined errors
HELP_READ = "Help text here"
STARTWEL = "Welcome to the bot!"
CLONEHELP_READ = "Clone help text here"
START = "Back to start"
ABOUT_READ = "About text here"
ADMIN_READ = "Admin panel here"
TOOLS_DATA_READ = "Tools data text here"
CHATBOT_READ = "Chatbot commands"

HELP_BTN = [[InlineKeyboardButton("Option 1", callback_data="OPTION1"), InlineKeyboardButton("Option 2", callback_data="OPTION2")]]
ABOUT_BTN = [[InlineKeyboardButton("Back", callback_data="BACK")]]
DEV_OP = [[InlineKeyboardButton("Developer", callback_data="DEV")]]
MUSIC_BACK_BTN = [[InlineKeyboardButton("Back", callback_data="BACK")]]
CHATBOT_BACK = [[InlineKeyboardButton("Back to Help", callback_data="BACK_HELP")]]
CLONEBACK = [[InlineKeyboardButton("Back", callback_data="BACK")]]
WELSTART_BOT = "Start Cloning"


@nexichat.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    bot_id = client.me.id

    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )

    elif query.data == "STARTCLONE":
        await query.message.edit(
            text=STARTWEL,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(WELSTART_BOT, callback_data="START")]]),
        )

    elif query.data == "CLONE":
        await query.message.edit(
            text=CLONEHELP_READ,
            reply_markup=InlineKeyboardMarkup(CLONEBACK),
        )

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
