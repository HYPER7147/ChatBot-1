import asyncio
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import IMG
from Champu import ChampuBot


start_txt = """**
✪ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗖𝗵𝗮𝗺𝗽𝘂 𝗥𝗲𝗽𝗼𝘀 ✪

➲ ᴇᴀsʏ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ✰  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs ✰  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ ✰

► sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs!
**"""




@ChampuBot.on_cmd("repo")
async def repo(_, m: Message):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{ChampuBot.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐺𝑅𝑂𝑈𝑃 🥀", url="https://t.me/Friendship_Club_Group"),
          InlineKeyboardButton("𝒄𝒉𝒂𝒏𝒏𝒆𝒍 ✨", url="https://t.me/Feeling_smiley"),
          ],
               [
                InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/ll_DEVIL_VENOM_ll"),

],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ", url=f"https://github.com/TheChampu/ChampuMusic"),
              InlineKeyboardButton("ᴄʜᴀᴛʙᴏᴛ", url=f"https://github.com/TheChampu/ChatBot")
              ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await m.reply_photo(
        photo=random.choice(IMG),
        caption=start_txt,
        reply_markup=reply_markup
    )
