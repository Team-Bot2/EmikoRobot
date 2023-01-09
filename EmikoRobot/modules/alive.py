import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/b50f2a808f8f51f3124e8.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**» Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Devil x Robot.** \n\n"
  TEXT += "» **I'm Working Properly** \n\n"
  TEXT += f"» **My Master : [Click here](https://t.me/official_pro_xD)** \n\n"
  TEXT += f"» **Library Version :** `{telever}` \n\n"
  TEXT += f"» **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"» **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**» Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("👷🏻 Support", "https://t.me/team_bot_support"), Button.url("Updates 🙋", "https://t.me/Team_bot_update")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
