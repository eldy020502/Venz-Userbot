# ⚠️ Module berisi video dewasa,jangan perlihatkan module ini ke anak kecil
# ⚠️ Credit by @venzproject
# ⚠️ Jangan hapus credit


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import venz_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@venz_cmd(pattern="pekob$")
async def _(event):
    try:
        pekobnya = [
            pekob
            async for pekob in event.client.iter_messages(
                "https://t.me/+skTTN1wh0ygyMzFl", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(pekobnya),
            caption=f"**ᴠɪᴅᴇᴏ ᴘᴇᴋᴏʙ ʙʏ** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("ᴠɪᴅᴇᴏ ᴘᴇᴋᴏʙɴʏᴀ ɢᴀᴅᴀ")


CMD_HELP.update(
    {
        "asupan2": f"**Plugin : **pekob\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}pekop\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video bokep secara random.\
"
    }
)
