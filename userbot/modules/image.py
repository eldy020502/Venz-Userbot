# Ported By VCKYOU @VckyouuBitch
# Credits © Rose-Userbot
# Ya gitu deh:')

from shutil import rmtree
from userbot.utils import kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import googleimagesdownload


@kyy_cmd(pattern="img (.*)")
async def goimg(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("`Give something to search...`")
    await event.edit("`Processing Keep Patience...`")
    if ";" in query:
        try:
            lmt = int(query.split(";")[1])
            query = query.split(";")[0]
        except BaseExceptaion:
            lmt = 5
    else:
        lmt = 5
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": lmt,
        "format": "jpg",
        "output_directory": "./downloads/",
    }
    pth = gi.download(args)
    ok = pth[0][query]
    await event.client.send_file(event.chat_id, ok, caption=query, album=True)
    rmtree(f"./downloads/{query}/")
    await event.delete()


CMD_HELP.update(
    {
        "img": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}img <search_query>`\
         \n↳ : Does an image search on Google and shows 5 images."
    }
)
