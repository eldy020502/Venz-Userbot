# ⚠️ Credit by @venzproject
# ⚠️ Credit by @tirexgugel
# ⚠️ Jangan hapus credit


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import venz_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos


@venz_cmd(pattern="ppwibu$")
async def _(event):
    try:
        ppwibunya = [
            ppwibu
            async for ppwibu in event.client.iter_messages(
                "@venzanime", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppwibunya),
            caption=f"**pp wibu by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**fotonya ngga ada**")


@venz_cmd(pattern="wallwibu$")
async def _(event):
    try:
        wallwibunya = [
            wallwibu
            async for wallwibu in event.client.iter_messages(
                "@wallpapervenz", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wallwibunya),
            caption=f"**wallpaper wibu by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**fotonya ngga ada**")


CMD_HELP.update(
    {
        "photowibu": f"**Plugin : **ppwibu\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ppwibu\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim mengirim foto wibu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}wallwibu\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim wallpaper wibu secara random.\
"
    }
)
