from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    ApplicationBuilder,
    ContextTypes,
    CallbackQueryHandler,
    filters,
)


TELEGRAM_API_TOKEN = "6881625558:AAHWCWB22HtYbIw40gghT4UxZT-HIuZedV0"

token = {"access_token": ""}
headers = {"Content-Type": "application/json"}
replay_keyboard = [
    [InlineKeyboardButton("client", callback_data="client")],
    [InlineKeyboardButton("Organization", callback_data="org")],
]
markup = InlineKeyboardMarkup(replay_keyboard)
choose_client_org = 0
register_org = 1
(
    to_full_name,
    to_date_of_birth,
    to_email,
    to_phone_number,
    to_highest_education_level,
    to_portfolio,
    to_cv,
    to_github,
    to_linkedin,
    to_save,
    to_done,
) = range(2, 12)
client_profile = {}
org_profile = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("hey abel", reply_markup=markup)
    return choose_client_org

#choose client or organization
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "client":
        if context._user_id in ["response"]:
            await query.message.reply_text("You are in what you want to do")
            return register_org
        else:
            await query.message.reply_text("You are not regestered")
            return register_org
    else:
        if context._user_id in ["response"]:
            await query.message.reply_text("You are in what you want to do")
            return register_org
        else:
            replay_keyboard = [
                [InlineKeyboardButton("REGISTER", callback_data="register")],
                [InlineKeyboardButton("EXIT", callback_data="exit")],
            ]
            markup = InlineKeyboardMarkup(replay_keyboard)
            await query.message.reply_text(
                "You are not regestered", reply_markup=markup
            )
            return register_org

#register client
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "register":
        await context.bot.send_message(
            chat_id=context._user_id,
            text="write your full name with space like 'abel tesfaye'",
        )
        return to_full_name
    else:
        await context.bot.send_message(chat_id=context._user_id, text="Bye")
        return ConversationHandler.END

#name of the client 
async def full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["telegramId"] = context._user_id
    client_profile["telegramUsername"] = context._user_name
    client_profile["firstName"], client_profile["lastName"] = update.message.text.split(
        " "
    )
    await context.bot.send_message(chat_id=context._user_id, text="date of birth")
    return to_date_of_birth

#register date of birth
async def date_of_birth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["dateOfBirth"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your email"
    )
    return to_email

#register email
async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["email"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your phone number"
    )
    return to_phone_number

#register phone number
async def phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["phone_number"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="what is your highest education level"
    )
    return to_highest_education_level

#register highest education level
async def highest_education_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["highest_education_level"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="link of your protfolio"
    )
    return to_portfolio

#register portfolio
async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["portfolio"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your cv"
    )
    return to_cv

#register cv
async def cv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["cv"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your github account"
    )
    return to_github

#register github
async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["github"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your linkedin account"
    )
    return to_linkedin

#register linkedin
async def linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["linkedin"] = update.message.text
    await context.bot.send_message(chat_id=context._user_id, text="Bye")
    return to_save

#save the data
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    replay_keyboard = [
        [InlineKeyboardButton("YES", callback_data="save")],
        [InlineKeyboardButton("EXIT", callback_data="exit")],
    ]
    markup = InlineKeyboardMarkup(replay_keyboard)
    await context.bot.send_message(
        chat_id=context._user_id,
        text="do your want to save your data",
        reply_markup=markup,
    )
    return to_done

#save the data
async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "save":
        await context.bot.send_message(chat_id=context._user_id, text="Data saved")
    else:
        await context.bot.send_message(chat_id=context._user_id, text="Bye")
        return ConversationHandler.END

#exit the conversation
async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context._user_id, text="Bye")
    return ConversationHandler.END




conversation_one = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        choose_client_org: [
            CallbackQueryHandler(
                button,
            )
        ],
        register_org: [
            CallbackQueryHandler(
                register,
            ),
            CallbackQueryHandler(
                exit,
            ),
        ],
        to_full_name: [MessageHandler(~filters.COMMAND, full_name)],
        to_date_of_birth: [MessageHandler(~filters.COMMAND, date_of_birth)],
        to_email: [MessageHandler(~filters.COMMAND, email)],
        to_phone_number: [MessageHandler(~filters.COMMAND, phone_number)],
        to_highest_education_level: [
            MessageHandler(~filters.COMMAND, highest_education_level)
        ],
        to_portfolio: [MessageHandler(~filters.COMMAND, portfolio)],
        to_cv: [MessageHandler(~filters.COMMAND, cv)],
        to_github: [MessageHandler(~filters.COMMAND, github)],
        to_linkedin: [MessageHandler(~filters.COMMAND, linkedin)],
        to_save: [MessageHandler(~filters.COMMAND, done)],
        to_done: [
            CallbackQueryHandler(
                save,
            ),
            CallbackQueryHandler(
                exit,
            ),
        ],
    },
    fallbacks=[CommandHandler("cancel", start)],
)


app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

app.add_handler(conversation_one)

app.run_polling()
