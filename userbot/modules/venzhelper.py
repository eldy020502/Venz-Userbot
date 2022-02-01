""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Kalo Lu Ga Tau Cara Gunain Bot Gw Lu Bisa Ketik** `.help` Atau Lu Juga Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/vnotv)"
        "\n[Repo](https://github.com/S/Venz-Userbot)"
        "\n[Instagram](instagram.com/eldydwinggga_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/eldy020502/Venz-Userbot/Venz-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.lhelp`\
\nUsage: Bantuan Untuk Rose-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
