from pyrogram.client import Client
from pyrogram.filters import command
from pyrogram.types import Message
from steam import install, install_game
import os, dotenv

dotenv.load_dotenv(dotenv_path="./config.env")

bot: Client = Client(
      name=str(os.environ.get("SESSION_NAME")),
      api_hash=str(os.environ.get("API_HASH")),
      api_id=int(os.environ.get("API_ID")),
      bot_token=str(os.environ.get("BOT_TOKEN"))
)

@bot.on_message(command("start", prefixes="/"))
async def start(client: Client, message: Message):
    await message.reply("""
Hola {}

-Envie /install para instalar Steam en su sistema
-Envie /game id del juego nombre de la carpeta sin espacios para descargar el juego en el sistema y subirlo a Telegram

Ejemplo:
-/game 761890 AlbionOnline - Instalara Albion Online
-/game 1782210 CrabGame - Instalara The Crab Game
-/game 1625450 Muck - Instalara Muck
""".format(message.from_user.mention))

@bot.on_message(command("install", prefixes="/"))
async def install_steam(client: Client, message: Message):
    await install(msg=message)


@bot.on_message(command("game", prefixes="/"))
async def install_steam_game(client: Client, message: Message):
    await install_game(message, gameid=message.text.split(" ")[1], gamename=message.text.split(" ")[2])



if __name__ == "__main__":
    print("Iniciando Bot")
    bot.start()
    print("Bot iniciado")
    bot.loop.run_forever()
