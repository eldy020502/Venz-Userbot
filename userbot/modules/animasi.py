from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd


@kyy_cmd(pattern='lunacy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.5)
    xnxx = await edit_or_reply(typew, "`Pertama-tama Cizi`")
    sleep(1.5)
    await xnxx.edit("`Kedua cizi cantik lagi`")
    sleep(1.5)
    await xnxx.edit("`Ketiga cizi masi cantik`")
    sleep(1.5)
    await xnxx.edit("`keempat punya cold`")
    sleep(1.5)
    await xnxx.edit("`Dan Kelima balik lagi ke nomor 1:3`")

# Create by myself @localheart


@kyy_cmd(pattern='punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "`\n┻┳|―-∩`"
                        "`\n┳┻|     ヽ`"
                        "`\n┻┳|    ● |`"
                        "`\n┳┻|▼) _ノ`"
                        "`\n┻┳|￣  )`"
                        "`\n┳ﾐ(￣ ／`"
                        "`\n┻┳T￣|`"
                        "\n**Hawoo ciziii**")

# Create by myself @localheart


@kyy_cmd(pattern='pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "`\n┻┳|―-∩`"
                        "`\n┳┻|     ヽ`"
                        "`\n┻┳|    ● |`"
                        "`\n┳┻|▼) _ノ`"
                        "`\n┻┳|￣  )`"
                        "`\n┳ﾐ(￣ ／`"
                        "`\n┻┳T￣|`"
                        "\n**Sedang memantau cizi dri jauh**")


# Create by myself @localheart


@kyy_cmd(pattern='idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "\n╭╮╱╱╭╮"
                        "\n┃╰╮╭╯┃"
                        "\n╰╮╰╯╭┻━┳╮╭╮"
                        "\n╱╰╮╭┫╭╮┃┃┃┃"
                        "\n╱╱┃┃┃╰╯┃╰╯┃"
                        "\n╱╱╰╯╰━━┻━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮"
                        "\n┃╭━╮┃"
                        "\n┃┃╱┃┣━┳━━╮"
                        "\n┃╰━╯┃╭┫┃━┫"
                        "\n┃╭━╮┃┃┃┃━┫"
                        "\n╰╯╱╰┻╯╰━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮╱╭╮╱╱╱╭╮"
                        "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                        "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                        "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                        "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                        "\n╰━━━┻━━┻┻━━┻━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━╮╱╭╮"
                        "\n┃┃╰╮┃┃"
                        "\n┃╭╮╰╯┣━━╮"
                        "\n┃┃╰╮┃┃╭╮┃"
                        "\n┃┃╱┃┃┃╰╯┃"
                        "\n╰╯╱╰━┻━━╯"
                        "\nㅤㅤㅤ"
                        "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                        "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                        "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                        "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                        "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                        "\n╰━━━┻━━┻━━┻━━┻━╯")


CMD_HELP.update({
    "animasi":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}lunacy`\
    \n↳ : Biasalah buat cizi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}punten` dan `.pantau`\
    \n↳ : Coba aja hehehe.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}idiot`\
    \n↳ : u're ediot xixixi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `kosong`\
    \n↳ : Tunggu update selanjutnya kawan."
})
