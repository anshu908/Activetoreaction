from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

OWNER = 6258915779

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    # Sending a video along with the reply text
    await message.reply_video(
        video="https://envs.sh/RCD.mp4",  # Replace with the actual video URL or local file path
        caption=(
            f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•\n│◍ ʜᴇʏ {message.from_user.first_name} ,\n│◍ ɪ'ᴍ {(await client.get_me()).mention} !\n└──────────────────────•\n✦ ϻσsᴛ ᴘσᴡєꝛғυʟʟ ʀєᴧᴄᴛɪση ʙσᴛ  \n✦ ʙєsᴛ ᴄʟσηєʀ ʙσᴛ ση ᴛєʟєɢꝛᴧϻ \n✦ ᴍᴀᴋᴇ ʏᴏᴜʀ ʙᴏᴛ ʙʏ /clone \n✦ ᴧᴅᴅ ϻє ɢꝛσυᴘ ᴛσ sєє ϻʏ ᴘσᴡєꝛ\n•──────────────────────•\n❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ ➟ [ʙσᴛ ᴄʜᴧϻʙєꝛ ](https://t.me/ll_BOTCHAMBER_ll)❤️‍🔥\n•──────────────────────•**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("❖ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ❖", url="https://t.me/ReactionByBot?startgroup=true")],
                [InlineKeyboardButton("• σᴡηєꝛ •", user_id=OWNER),
                 InlineKeyboardButton("• ᴄʟσηє •", callback_data="CLONE")], 
                [InlineKeyboardButton("• υᴘᴅᴧᴛє •", url="https://t.me/ll_BOTCHAMBER_ll"),
                InlineKeyboardButton("• sυᴘᴘσꝛᴛ •", url="https://t.me/BOT_SUPPORT_GROUP7")]
            ]
        )
    )
