from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, kyy_cmd


@kyy_cmd(pattern="cizi(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    x = await edit_or_reply(typew, "**Halo Cizi**")
    sleep(1.5)
    await x.edit("**Cuma Mau Bilang**")
    sleep(1.5)
    await x.edit("**Kalo Cizi Tuh Cantik**")
    sleep(1.5)
    await x.edit("**No Debat Sih**")
    sleep(1.5)
    await x.edit("**Pawangnya Cold?**")
    sleep(1.5)
    await x.edit("**Anjayyyy**")
    sleep(1.5)
    await x.edit("**Yang Gasuka Bewan Dek**")
    sleep(1.5)
    await d.edit("**I Love You Cizi**")
    sleep(1.5)
    await x.edit("**Mwahhh**")
    sleep(1.5)
    await x.edit("**Cizi chan kawaiii desuu**")
    sleep(1.5)
    await x.edit("**>\\<**")


@kyy_cmd(pattern="cheeze(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,
                        "**Cizi Tuh Cantik,Jadi Mundur Aja Kelen Yak,Maaf Saya Dluan**")


@kyy_cmd(pattern="cz(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**Cizi Tuh Pas Lahir Terbuat Dari Gula Aren,Jadi Manis**")


@kyy_cmd(pattern="pungut(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**Kebetulan Kemarin Cizi Imut Aku Pungut Didunia Kayangan,Pas Liat Kondisinya Terlalu Miris,Jadi Aku Pungut,Saya Gasalah Pungut,Soalnya Dia Spek Bidadari,Yang Terlantar**")


@kyy_cmd(pattern="cold(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**Cold Baik Sudah Merawat Cizi Dengan Memberinya Segala Asupan Vitamin**")


@kyy_cmd(pattern="coldy(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**Cold Adalah Pejantan Unggul Yang Tidak Suka Digoda,Dan Cold Adalah Si Pria Cuek,Gasuka Dichat Cewe Lain,Kecuali Cizichan**")


@kyy_cmd(pattern="cool(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(event,"**Cold Orgnya Cuek**")


@kyy_cmd(pattern="col(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Cold Bukan Wibu Tapi Suka Anime**")


@kyy_cmd(pattern="colm(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Gatau Deh Saya Anak Konglomerat**")


@kyy_cmd(pattern="el(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Nama Asli Cold Itu Eldy Dwingga Saputra**")


@kyy_cmd(pattern="asal(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Asal Saya Dari Riau,Dumai**")


@kyy_cmd(pattern="meet(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Mungkin Ada Yang Dari Dumai,Salam Kenal**")


@kyy_cmd(pattern="skrg(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,"**Skrg Tinggal Di sulawesi Di kabupaten Sidrap**")


CMD_HELP.update(
    {
        "cizi": f"**Plugin : **`cizi`\
        \n\n  •  **Syntax :** `{cmd}cizi`\
        \n  •  **Function : **Bucin Ke cizi\
        \n\n  •  **Syntax :** `{cmd}cheeze`\
        \n  •  **Function : **Bucin Ke cizi\
        \n\n  •  **Syntax :** `{cmd}cz`\
        \n  •  **Function : **kelahiran cizi\
        \n\n  •  **Syntax :** `{cmd}pungut`\
        \n  •  **Function : **cizi el pungut\
        \n\n  •  **Syntax :** `{cmd}cold`\
        \n  •  **Function : **tentang cold\
        \n\n  •  **Syntax :** `{cmd}coldy`\
        \n  •  **Function : **cold sijantan\
        \n\n  •  **Syntax :** `{cmd}cool`\
        \n  •  **Function : **cold sicuek\
        \n\n  •  **Syntax :** `{cmd}col`\
        \n  •  **Function : **cold bukan wibu\
        \n\n  •  **Syntax :** `{cmd}colm`\
        \n  •  **Function : **cold si anak konglomerat\
        \n\n  •  **Syntax :** `{cmd}el`\
        \n  •  **Function : **nama lengkap el\
        \n\n  •  **Syntax :** `{cmd}asal`\
        \n  •  **Function : **asal si cold\
        \n\n  •  **Syntax :** `{cmd}meet`\
        \n  •  **Function : **gatau\
        \n\n  •  **Syntax :** `{cmd}skrg`\
        \n  •  **Function : **tempat tinggal cold yg sekarang\
        \n\n**Klo mau Req, kosa kata dari lu Hubungi @moonscrsh**\
    "
    }
)
