# Edit By @pikyus1

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, venz_cmd


@venz_cmd(pattern='thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                        "╔══╦╗────╔╗─╔╗╔╗\n"
                        "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                        "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                        "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                        "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@venz_cmd(pattern='malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "╔═╦═╦╗╔═╦══╦═╦══╗\n"
                        "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                        "╠═║═╣╚╣║║║║║║║║║\n"
                        "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                        "╔══╦═╦╗╔═╦══╗\n"
                        "║║║║╬║║║╬║║║║\n"
                        "║║║║║║╚╣║║║║║\n"
                        "╚╩╩╩╩╩═╩╩╩╩╩╝")


@venz_cmd(pattern='rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**GAMBAR RUMAH**\n"
                        "╱◥◣\n"
                        "│∩ │◥███◣ ╱◥███◣\n"
                        "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                        "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                        "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                        "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@venz_cmd(pattern='join(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "_/﹋\\_\n"
                        "(҂`_´)\n"
                        "<,︻╦╤─ ҉\n"
                        r"_/﹋\_"
                        "\n**ᴊᴏɪɴ ʟɪɴᴋ ʙɪᴏ😡**")


CMD_HELP.update({
    "animasi5":
    f"`{cmd}rumah` ; `{cmd}join` ; `{cmd}malam` ; `{cmd}thanks`\
    \nUsage: test aja."
})
