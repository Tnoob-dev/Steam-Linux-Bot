# from pysteamcmd.steamcmd import Steamcmd, SteamcmdException
from pyrogram.types import Message
from pysteamcmdwrapper import SteamCMD, SteamCMDException
from pathlib import Path
import shutil, os, compress, dotenv

dotenv.load_dotenv(dotenv_path="./config.env")

if not os.path.exists("./Steam/"):
    os.mkdir("./Steam/")

s = SteamCMD("./Steam/")

async def install(msg: Message):

    message = await msg.reply("Instalando Steam🧪 en local")

    try:
        s.install()
        await message.edit("Instalado✅")
        # os.system("bash Steam/steamcmd.sh")
    except SteamCMDException:

        print("ya esta instalado")
        # os.system("bash Steam/steamcmd.sh")
        await message.edit("Steam🧪 ya esta instalado en el sistema")

# Progreso de la subida en la terminal
async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

async def upload_to_tg(msg: Message, doc: str):
    await msg.reply_document(doc, quote=True, progress=progress)

async def install_game(msg: Message, gameid: int, gamename: str):

    await msg.reply("Descargando: {}\nID: {}".format(gamename, gameid))
    message = await msg.reply("Comenzando Descarga...")
    
    try:
        message2 = await message.edit("Logeandose con la cuenta🤖")

        s.login(os.environ.get("STEAM_USER"), os.environ.get("STEAM_PASSWORD"))
        
        await message2.edit("Logeo Completado✅, ahora instalando {}...".format(gamename))
        
        s.app_update(app_id=gameid, install_dir="/{}/".format(gamename), validate=True)
        await msg.reply("Juego ||{}|| Instalado, ahora subiendo a Telegram".format(gamename))
        # Compresion #
        file = shutil.make_archive(gamename, "zip", "./Steam/{}/".format(gamename), "./")

        # 900 MB = 943718400
        # 1.5 GB = 1610612736

        if Path(file).stat().st_size > 1610612736:

            message3 = await msg.reply("El juego pesa mas de 1.5 GB asi que se comprimira y se subira")
            file_list = compress.compress("./{}.zip".format(gamename), part_size=1500)
            await message3.edit("Comprimido, ahora subiendo :D")

            for files in file_list:
                await upload_to_tg(msg, files)
            
            await message3.delete()
            await msg.reply("Listo✅")
        
        else:
            message3 = await msg.reply("El juego esta en un tamaño  aceptable, asi que ya se subira")
            await upload_to_tg(msg, file)

            await message3.delete()
            await msg.reply("Listo✅")
    except SteamCMDException:
        print("Ocurrio algun error")
        await message.edit("Ha ocurrido algun error")