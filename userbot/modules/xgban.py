from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.utils import edit_or_reply, edit_delete, kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="allban(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await edit_or_reply(event, "Anda Tidak Mempunyai Hak")
        return
    await edit_or_reply(event, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await edit_or_reply(event, str(e))
        await sleep(.5)
    await edit_delete(event, "Tidak Ada yang Terjadi di sini🙃🙂")

CMD_HELP.update(
    {
        "allban": f"**Plugin : **`allban`\
    \n\n**Syntax : **`{cmd}allban`\
    \n**Function : **ban all members in 1 cmnd"
    }
)
