from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):



    START_TEXT = """
𝗛𝗘𝗟𝗟𝗢 {} 

𝗜 𝗔𝗠 𝗧𝗚 𝗠𝗢𝗦𝗧 𝗣𝗢𝗪𝗘𝗥 𝗙𝗨𝗟𝗟 𝗠𝗘𝗗𝗜𝗔 𝗘𝗡𝗖𝗢𝗗𝗘𝗥 / 𝗩𝗜𝗗𝗘𝗢 𝗘𝗡𝗖𝗢𝗗𝗘𝗥 𝗕𝗢𝗧 

𝗧𝗬𝗣𝗘 : /help 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧

𝗕𝗢𝗧 𝗠𝗔𝗜𝗡𝗧𝗔𝗜𝗡/𝗠𝗔𝗗𝗘 𝗕𝗬 : @KOT_BOTS | @KOT_FREE_DE_LA_HOYA_OFF | @KOT_REPORS
"""
    HELP_TEXT = """
Hᴏᴡ Tᴏ Usᴇ M ᴇʜ 

➠ Jᴜsᴛ Sᴇɴᴅ Mᴇʜ Mᴇᴅɪᴀ Tᴏ Gᴇᴛ Sᴛᴀʀᴛᴇᴅ 

➠ Tᴏ Dᴇʟᴇᴛᴇ Tʜᴜᴍʙɴᴀɪʟ Tʏᴘᴇ : /dthumb 

➠ Tᴏ Sᴇᴛ ᴀ Tʜᴜᴍʙɴᴀɪʟ Tʏᴘᴇ : /sthumb 

➠ Usᴇ /settings Cᴏᴍᴍᴇɴᴛ Tᴏ Cʜᴇᴄᴋ Yᴏᴜʀ Sᴇᴛᴛɪɴɢs

➠ ɪ Cᴀɴ Eɴᴄᴏᴅᴇ Aɴʏ Vɪᴅᴇᴏ Oʀ Fɪʟᴇ Iɴ Nᴇɢʟɪɢɪʙʟᴇ Qᴜᴀʟɪᴛʏ

𝗕𝗢𝗧 𝗠𝗔𝗜𝗡𝗧𝗔𝗜𝗡/𝗠𝗔𝗗𝗘 𝗕𝗬 : @KOT_BOTS | @KOT_FREE_DE_LA_HOYA_OFF | @KOT_REPORS
"""
    ABOUT_TEXT = """
╭──────[@KOT_BOTS]───────〄
│
├ Nᴀᴍᴇ : <a href='https://t.me/KOT_VIDEO_ENCODING_BOT'>Vɪᴅᴇᴏ Eɴᴄᴏᴅɪɴɢ Bᴏᴛ</a>
│
├ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>Hᴇʀᴏᴋᴜ</a>
│ 
├ Lᴀɴɢᴜᴀɢᴇ : <a href='https://docs.pyrogram.org/'>Pʏᴛʜᴏɴ 3.9.6</a>
│
├ Vᴇʀꜱɪᴏɴ : <a href='https://t.me/KOT_VIDEO_ENCODING_BOT'>1.0 Bᴇᴛᴀ</a>
│
├ Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ 1.2.9</a>
│
├ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
│
├ Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/KOT_LINKS_TEAM'>Kᴏᴛ Lɪɴᴋs Tᴇᴀᴍ</a>
│
├ Uᴘᴅᴀᴛᴇᴅ Oɴ : [ 17.1.2022 ] 08:00 AM"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/KOT_BOTS'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/KOT_REPORS')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
