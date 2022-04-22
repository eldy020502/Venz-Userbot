# ⚠️ Module berisi video dewasa,jangan perlihatkan module ini ke anak kecil
# ⚠️ Credit by @venzproject
# ⚠️ Jangan hapus credit


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import venz_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@venz_cmd(pattern="pedo$")
async def _(event):
    try:
        pedonya = [
            pedo
            async for pedo in event.client.iter_messages(
                "@venzpedobot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(pedonya),
            caption=f"**ᴠɪᴅᴇᴏ ᴘᴇᴅᴏ ʙʏ** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("ᴠɪᴅᴇᴏ ʟᴏʟɪ ɴʏᴀ ɢᴀ ᴀᴅᴀ")


@venz_cmd(pattern="olyfans$")
async def _(event):
    try:
        olyfansnya = [
            olyfans
            async for olyfans in event.client.iter_messages(
                "@onlyvenzzz", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(olyfansnya),
            caption=f"**ᴠɪᴅᴇᴏ ᴏɴʟʏꜰᴀɴꜱ ʙʏ** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("ᴠɪᴅᴇᴏ ᴏɴʟʏꜰᴀɴꜱɴʏᴀ ɢᴀᴅᴀ")


CMD_HELP.update(
    {
        "asupan2": f"**Plugin : **pedo\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}pedo\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video pedo secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}olyfans\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video onlyfans.\
"
    }
)
