# Credit by @justrex Xa-Userbot | Ultroid
# Inspired by https://github.com/rexashh/Xa-Userbot
# And inspired by https://github.com/TeamUltroid/Ultroid
# klo ambil credit jangan dihapus lah pantek

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import venz_cmd
import asyncio


@venz_cmd(pattern="dudul(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('hmmmm')
    animation_chars = [
        '[Ini aku dudul](https://telegra.ph/file/7c232e811f2db5cfc7e7e.jpg)',
        '[dudul mau ngomong sesuatu,boleh ga?](https://telegra.ph/file/fc9a0178d8240f163d34e.jpg)',
        '[dudul suka kamu 😻](https://telegra.ph/file/afcc3f52fbb59e4cab069.jpg)',
        '[­kamu mau ga jadi pacal na dudul😻](https://telegra.ph/file/afcc3f52fbb59e4cab069.jpg)',
        '[terima yaa😿](https://telegra.ph/file/6966de30e3b4f9ff4bfe2.jpg)',
        '[klo ga terima nanti dudul nangis lho😿](https://telegra.ph/file/e96ea8dd2d598395f4457.jpg)',
        '[pwissss](https://telegra.ph/file/e96ea8dd2d598395f4457.jpg)',
        '[terima dudul ya😻](https://telegra.ph/file/afcc3f52fbb59e4cab069.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)


@venz_cmd(pattern="papku(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 9)
    await event.edit('Aku mau ngasih Pap aku buat kamu')
    animation_chars = [
        '[Ini aku](https://telegra.ph/file/091024e9bb4729426cc44.jpg)',
        '[aku ganteng](https://telegra.ph/file/836ec69a83a81b909e106.jpg)',
        '[Ganteng Banget kan 😻](https://telegra.ph/file/597969f9c0783081e523e.jpg)',
        '[­Ganteng intinya👩‍❤️‍💋‍👨](https://telegra.ph/file/32fc29f1689be15e20a7d.jpg)',
        '[Kamu Mau jadi pacarku?😻😍💘](https://telegra.ph/file/0cdcb0452c89a664dcb98.jpg)',
        '[Mau lagi?](https://telegra.ph/file/10140ec996bfed2b41dc1.jpg)',
        '[Nihhh](https://telegra.ph/file/ba17968cd0fa477e96dc3.jpg)',
        '[Terkahir](https://telegra.ph/file/ed6a84a8b1c315183cc35.jpg)',
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8], link_preview=True)

CMD_HELP.update(
    {
        "gombal": f"**Plugin : **`gombal`\
        \n\n    **Perintah :** `{cmd}dudul`\
        \n⌬    **Fungsi : **dudul nembak kamu.\
       \n\n    **Perintah :** `{cmd}papku`\
        \n⌬    **Fungsi : **Bonus awoakwoak."
    })
