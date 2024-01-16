from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from config import BOT_USERNAME
from config import OWNER_ID

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = """**
🤖 Wᴇʟᴄᴏᴍᴇ ᴛᴏ GɪᴛHᴜʙ Cᴏɴᴛʀᴏʟ Bᴏᴛ! 🚀

Tʜɪs ʙᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ʀɪɢʜᴛ ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ. Usᴇ ᴄᴏᴍᴍᴀɴᴅs ʟɪᴋᴇ /gitprivate ᴀɴᴅ /gitpublic ᴛᴏ ᴄʜᴀɴɢᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴠɪsɪʙɪʟɪᴛʏ. Eɴsᴜʀᴇ ᴛᴏ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛᴇ ᴡɪᴛʜ ʏᴏᴜʀ GɪᴛHᴜʙ ᴛᴏᴋᴇɴ ғᴏʀ sᴇᴄᴜʀᴇ ᴀᴄᴄᴇss. Fᴏʀ ᴀssɪsᴛᴀɴᴄᴇ, ᴜsᴇ /help.

🔗 GɪᴛHᴜʙ Cᴏɴᴛʀᴏʟ Bᴏᴛ ɪs ʜᴇʀᴇ ᴛᴏ sɪᴍᴘʟɪғʏ ʏᴏᴜʀ GɪᴛHᴜʙ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ. Hᴀᴘᴘʏ ᴄᴏᴅɪɴɢ!
**"""




@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/iam_daxx"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ecbeac5889f9542f32469.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )



#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪




@app.on_message(filters.command("help", prefixes="/"))
def help_command(_, message):
    help_message = (
        "GitHub Control Bot Commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/allrepo - List your GitHub repositories\n"
        "/create_repo - Create a new GitHub repository\n"
        "/delrepo - Delete a GitHub repository\n"
        "/add_collaborator - Add a collaborator to a GitHub repository\n"
        "/remove_collaborator - Remove a collaborator from a GitHub repository"
    )

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Help", callback_data='help')]])

    message.reply_text(help_message, reply_markup=keyboard)

@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'help':
        help_text = (
            "GitHub Control Bot Commands:\n"
            "/start - Start the bot\n"
            "/help - Display this help message\n"
            "/allrepo - List your GitHub repositories\n"
            "/create_repo - Create a new GitHub repository\n"
            "/delrepo - Delete a GitHub repository\n"
            "/add_collaborator - Add a collaborator to a GitHub repository\n"
            "/remove_collaborator - Remove a collaborator from a GitHub repository"
        )
        query.message.edit_text(help_text)
        
# incoming msg

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
        
