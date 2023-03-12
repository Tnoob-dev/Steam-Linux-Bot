# Steam-Linux-Bot

## Bot para la descarga de juegos de Steam y subirlo a Telegram
### Uso:

-/start - Inicia el Bot
-/install - Instala Steam en su sistema
-/game id name - descarga el juego guiandose por su ID y subiendolo a Telegram con el nombre que usted le ponga

### Antes de montar/iniciar el bot establezca las variables de Entorno en el config.env:
- SESSION_NAME - Nombre de la sesion creada por Pyrogram
- BOT_TOKEN - Token del bot que se obtiene por https://t.me/BotFather
- API_HASH - Credenciales de https://my.telegram.org/
- API_ID - Credenciales de https://my.telegram.org/
- STEAM_USER - Usuario de Steam
- STEAM_PASSWORD - Contraseña de Steam

## ¿Por que son necesarias las credenciales de Steam?
- Principalmente para evitar conflictos con la plataforma
- Antes de instalar algun juego va a la tienda de Steam entrando via Web o por la app en su Smartphone/Tablet/PC y presione en Agregar a la Biblioteca, esto ahorrara error de subscripcion para la mayoria de juegos

(https://raw.githubusercontent.com/Tnoob-dev/Steam-Linux-Bot/main/image.png)
