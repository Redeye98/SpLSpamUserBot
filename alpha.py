from pyrogram import Client, filters, idle
from config import *
from YashuAlpha.plugins import start, help, cmds_cbq, close_cbq, raid_cbq, extra_cbq, spam_cbq
from YashuAlpha.raid import raid, replyraid, dreplyraid, raid_cwf
from YashuAlpha.data import KeshavX
from YashuAlpha.spam import spam, dspam
from YashuAlpha.echo import addecho, rmecho, echo_cwf

END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)
END2 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_2)
END3 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_3)
END4 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_4)
END5 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_5)
END6 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_6)
END7 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_7)
END8 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_8)
END9 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_9)
END10 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_10)

@END.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("help", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("help", hl) & filters.user(LEGENDS))
async def help_plug(_, m):
    await help(_, m)

@END.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("spam", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
async def spam_plug(_, m):
    await spam(_, m)

@END.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("dspam", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
async def dspam_plug(_, m):
    await dspam(_, m)
