""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/moonscrsh)"
        "\n[Repo](https://github.com/eldy020502/Venz-Userbot)"
        "\n[Instagram](instagram.com/eldydwinggga_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/eldy020502/Venz-Userbot/Venz-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.lhelp`\
\nUsage: Bantuan Untuk Venz-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
