# Ported By VCKYOU @VckyouuBitch
# Fixes By Koala @Manusiarakitann

from PIL import Image
import cv2
import os
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import CMD_HELP, bot


@kyy_cmd(pattern="tiny(?: |$)(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await edit_delete(event, "`Mohon Balas Ke Sticker`")
        return
    xx = await edit_or_reply(event, "`Memproses Tiny....`")
    ik = await bot.download_media(reply)
    im1 = Image.open("resources/sky_blank.png")
    if ik.endswith(".tgs"):
        await event.client.download_media(reply, "geez.tgs")
        os.system("lottie_convert.py geez.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = jsn.replace("512", "2000")
        open("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json geez.tgs")
        file = "geez.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(ik)


CMD_HELP.update({
    f"tiny": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}tiny`\
    \nUsage : Untuk Memperkecil Sticker."})
