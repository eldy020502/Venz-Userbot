from time import sleep
from userbot import CMD_HELP, bot, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@kyy_cmd(pattern='helikopter(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "▬▬▬.◙.▬▬▬ \n"
                        "═▂▄▄▓▄▄▂ \n"
                        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                        "◥█████◤ \n"
                        "══╩══╩══ \n"
                        "╬═╬ \n"
                        "╬═╬ \n"
                        "╬═╬ \n"
                        "╬═╬ \n"
                        "╬═╬ \n"
                        "╬═╬ \n"
                        "╬═╬ Hallo Semuanya :) \n"
                        "╬═╬☻/ \n"
                        "╬═╬/▌ \n"
                        "╬═╬/ \\ \n")


@kyy_cmd(pattern='tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "_/﹋\\_\n"
                        "(҂`_´)\n"
                        "<,︻╦╤─ ҉\n"
                        r"_/﹋\_"
                        "\n**Mau Jadi Pacarku Gak?!**")


@kyy_cmd(pattern='bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "`Dadah Semuanya...`          \n　　　　　|"
                        "\n　　　　　| \n"
                        "　　　　　| \n"
                        "　　　　　| \n"
                        "　　　　　| \n"
                        "　　　　　| \n"
                        "　　　　　| \n"
                        "　　　　　| \n"
                        "　／￣￣＼| \n"
                        "＜ ´･ 　　 |＼ \n"
                        "　|　３　 | 丶＼ \n"
                        "＜ 、･　　|　　＼ \n"
                        "　＼＿＿／∪ _ ∪) \n"
                        "　　　　　 Ｕ Ｕ\n")


@kyy_cmd(pattern='awkwok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "────██──────▀▀▀██\n"
                        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                        "▄▀──█▄▄──────█─█▄▄\n"
                        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`")


@kyy_cmd(pattern='ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "░░░░▓\n"
                        "░░░▓▓\n"
                        "░░█▓▓█\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░░░██▓▓██\n"
                        "░░░░██▓▓██\n"
                        "░░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░██▓▓██\n"
                        "░░░██▓▓███\n"
                        "░░░░██▓▓████\n"
                        "░░░░░██▓▓█████\n"
                        "░░░░░░██▓▓██████\n"
                        "░░░░░░███▓▓███████\n"
                        "░░░░░████▓▓████████\n"
                        "░░░░█████▓▓█████████\n"
                        "░░░█████░░░█████●███\n"
                        "░░████░░░░░░░███████\n"
                        "░░███░░░░░░░░░██████\n"
                        "░░██░░░░░░░░░░░████\n"
                        "░░░░░░░░░░░░░░░░███\n"
                        "░░░░░░░░░░░░░░░░░░░\n")


@kyy_cmd(pattern='y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                        "██████▄▄█‡‡‡‡‡‡████████▄\n"
                        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                        "█████‡‡‡‡‡‡‡██████████\n")


@kyy_cmd(pattern='tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                        "▂▄▅█████████▅▄▃▂…\n"
                        "[███████████████████]\n"
                        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@kyy_cmd(pattern='babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "┈┈┏━╮╭━┓┈╭━━━━╮\n"
                        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@kyy_cmd(pattern='ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "╥━━━━━━━━╭━━╮━━┳\n"
                        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@kyy_cmd(pattern='bernyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    typew = await edit_or_reply(typew, "**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


CMD_HELP.update({
    "animasi4":
    f"`{cmd}bulan` ; `{cmd}hati` ; `{cmd}bernyanyi`\
    \nUsage: liat aja.\
    \n\n`{cmd}helikopter` ; `{cmd}tank` `{cmd}tembak`\n`{cmd}bundir`\
    \nUsage: liat sendiri\
    \n\n`{cmd}y`\
    \nUsage: jempol\
    \n\n`{cmd}awkwok`\
    \nUsage: ketawa lari.\
    \n\n`{cmd}ular` ; `{cmd}babi` ; `{cmd}ajg`\
    \nUsage: liat sendiri."
})
