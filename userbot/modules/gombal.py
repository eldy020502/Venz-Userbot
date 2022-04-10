from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Xa_cmd
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

CMD_HELP.update(
    {
        \n\n    **Perintah :** `{cmd}dudul`\
        \n⌬    **Fungsi : **dudul mau tembak kamu"
    })