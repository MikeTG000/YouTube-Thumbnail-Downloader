import os
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "my-first-project",
    api_id = 8792993,
    api_hash = "32606d7130c8b67b2b11620aa0ee016d",
    bot_token = "6023336627:AAGGJH2sldGKaYiBnbyITt-eMS4ov9sAiKs"
)

START_TEXT="""
Hey {} ,

I'm just an age calculating bot. You can calculate your age using this bot. Press the help button to know more.

"""
START_BUTTONS = InlineKeyboardMarkup( 
         [[ 
         InlineKeyboardButton('google', callback_data='help'), 
         ],[ 
         InlineKeyboardButton('About', callback_data='about'),         
         ]] 
     )
    

@Bot.on_message(filters.command(["start"])) 
async def start(bot, update): 
     text = START_TEXT.format(update.from_user.mention) 
     reply_markup = START_BUTTONS 
     await update.reply_text( 
         text=text, 
         disable_web_page_preview=True, 
         reply_markup=reply_markup, 
     )


Bot.run
