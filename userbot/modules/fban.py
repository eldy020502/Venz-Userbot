from sqlalchemy.exc import IntegrityError

from userbot import CMD_HELP, bot, CMD_HANDLER as cmd
from userbot.utils import kyy_cmd


@kyy_cmd(pattern="fban(?: |$)(.*)")
async def fban(event):
    """Bans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        fban_id = reply_msg.sender_id
        reason = event.pattern_match.group(1)
    else:
        pattern = str(event.pattern_match.group(1)).split()
        fban_id = pattern[0]
        reason = " ".join(pattern[1:])

    try:
        fban_id = await event.client.get_peer_id(fban_id)
    except BaseException:
        pass

    if event.sender_id == fban_id:
        return await event.edit(
            "**Error: This action has been prevented by KyyBot self preservation protocols.**"
        )

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**You haven't connected to any federations yet!**")

    user_link = f"[{fban_id}](tg://user?id={fban_id})"

    await event.edit(f"**Fbanning** {user_link}...")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/fban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New FedBan" not in reply.text)
                    and ("Starting a federation ban" not in reply.text)
                    and ("Start a federation ban" not in reply.text)
                    and ("FedBan reason updated" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Failed to fban in {len(failed)}/{total} feds.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"Success! Fbanned in {total} feds."

    await event.edit(
        f"**Fbanned **{user_link}!\n**Reason:** {reason}\n**Status:** {status}"
    )


@kyy_cmd(pattern="unfban(?: |$)(.*)")
async def unfban(event):
    """Unbans a user from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    if event.is_reply:
        reply_msg = await event.get_reply_message()
        unfban_id = reply_msg.sender_id
        reason = event.pattern_match.group(1)
    else:
        pattern = str(event.pattern_match.group(1)).split()
        unfban_id = pattern[0]
        reason = " ".join(pattern[1:])

    try:
        unfban_id = await event.client.get_peer_id(unfban_id)
    except BaseException:
        pass

    if event.sender_id == unfban_id:
        return await event.edit("**Wait, that's illegal**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**You haven't connected to any federations yet!**")

    user_link = f"[{unfban_id}](tg://user?id={unfban_id})"

    await event.edit(f"**Un-fbanning **{user_link}**...**")
    failed = []
    total = int(0)

    for i in fed_list:
        total += 1
        chat = int(i.chat_id)
        try:
            async with bot.conversation(chat) as conv:
                await conv.send_message(f"/unfban {user_link} {reason}")
                reply = await conv.get_response()
                await bot.send_read_acknowledge(
                    conv.chat_id, message=reply, clear_mentions=True
                )

                if (
                    ("New un-FedBan" not in reply.text)
                    and ("I'll give" not in reply.text)
                    and ("Un-FedBan" not in reply.text)
                ):
                    failed.append(i.fed_name)
        except BaseException:
            failed.append(i.fed_name)

    reason = reason if reason else "Not specified."

    if failed:
        status = f"Failed to un-fban in {len(failed)}/{total} feds.\n"
        for i in failed:
            status += "• " + i + "\n"
    else:
        status = f"Success! Un-fbanned in {total} feds."

    reason = reason if reason else "Not specified."
    await event.edit(
        f"**Un-fbanned** {user_link}!\n**Reason:** {reason}\n**Status:** {status}"
    )


@kyy_cmd(pattern="addf(?: |$)(.*)")
async def addf(event):
    """Adds current chat to connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import add_flist
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    if not (fed_name := event.pattern_match.group(1)):
        return await event.edit("**Pass a name in order connect to this group!**")

    try:
        add_flist(event.chat_id, fed_name)
    except IntegrityError:
        return await event.edit(
            "**This group is already connected to federations list.**"
        )

    await event.edit("**Added this group to federations list!**")


@kyy_cmd(pattern="delf$")
async def delf(event):
    """Removes current chat from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    del_flist(event.chat_id)
    await event.edit("**Removed this group from federations list!**")


@kyy_cmd(pattern="listf$")
async def listf(event):
    """List all connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import get_flist
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    if len((fed_list := get_flist())) == 0:
        return await event.edit("**You haven't connected to any federations yet!**")

    msg = "**Connected federations:**\n\n"

    for i in fed_list:
        msg += "• " + str(i.fed_name) + "\n"

    await event.edit(msg)


@kyy_cmd(pattern="clearf$")
async def delf(event):
    """Removes all chats from connected federations."""
    try:
        from userbot.modules.sql_helper.fban_sql import del_flist_all
    except IntegrityError:
        return await event.edit("**Running on Non-SQL mode!**")

    del_flist_all()
    await event.edit("**Disconnected from all connected federations!**")


CMD_HELP.update(
    {
        "federation": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}fban <id/username> <reason>`"
        "\n↳ : Bans user from connected federations."
        "\nYou can reply to the user whom you want to fban or manually pass the username/id."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}unfban <id/username> <reason>`"
        "\n↳ : Same as fban but unbans the user"
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}addf <name>`"
        "\n↳ : Adds current group and stores it as <name> in connected federations."
        "\nAdding one group is enough for one federation."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}delf`"
        "\n↳ : Removes current group from connected federations."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}listf`"
        "\n↳ : Lists all connected federations by specified name."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}clearf`"
        "\n↳ : Disconnects from all connected federations. Use it carefully."})
