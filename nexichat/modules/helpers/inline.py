from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat

WELSTART_BOT= [
                [InlineKeyboardButton("❖ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ❖", url="https://t.me/REACTION7_ROBOT?startgroup=true")],
                [InlineKeyboardButton("• σᴡηєꝛ •", user_id=OWNER),
                 InlineKeyboardButton("• ᴄʟσηє •", callback_data="CLONE")], 
                [InlineKeyboardButton("• υᴘᴅᴧᴛє •", url="https://t.me/ll_BOTCHAMBER_ll"),
                InlineKeyboardButton("• sυᴘᴘσꝛᴛ •", url="https://t.me/BOT_SUPPORT_GROUP7")]
]

CLONEBACK = [("⦿ ʙᴀᴄᴋ ⦿", callback_data="STARTCLONE")]


START_BOT = [
    
    [
        InlineKeyboardButton(text="🛠️ σρεи ¢σммαиdꜱ ⚙️", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(text="🛠️ σρεи ¢σммαиdꜱ ⚙️", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄʟᴏsᴇ ⦿",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER),
        #   InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]
