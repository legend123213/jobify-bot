from request_util import Request_to_Django


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


TELEGRAM_API_TOKEN = ""

token = {"access_token": ""}
headers = {"Content-Type": "application/json"}
replay_keyboard = [
    [InlineKeyboardButton("client", callback_data="client")],
    [InlineKeyboardButton("Organization", callback_data="org")],
]
markup = InlineKeyboardMarkup(replay_keyboard)
choose_client_org = 0
register_client = 1
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
    register_org,
    to_org_name,
    to_type,
    to_email_org,
    to_phone_number_org,
    to_description,
    to_website,
    to_address,
    to_linkedin_org,
) = range(2, 22)
client_profile = {}
org_profile = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("hey abel", reply_markup=markup)
    return choose_client_org

# choose client or organization
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "org":
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
    else:
        if context._user_id in ["response"]:
            await query.message.reply_text("You are in what you want to do")
            return register_client
        else:
            replay_keyboard = [
                [InlineKeyboardButton("REGISTER", callback_data="register")],
                [InlineKeyboardButton("EXIT", callback_data="exit")],
            ]
            markup = InlineKeyboardMarkup(replay_keyboard)
            await query.message.reply_text(
                "You are not regestered", reply_markup=markup
            )
            return register_client


# register organization
async def register_org(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "register":
        await context.bot.send_message(
            chat_id=context._user_id,
            text="write your organization name",
        )
        return to_org_name
    else:
        await context.bot.send_message(chat_id=context._user_id, text="Bye")
        return ConversationHandler.END


# name of the organization
async def org_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["telegramId"] = str(context._user_id)
    org_profile["telegramUsername"] = str(context._user_id) + "@telegram"
    org_profile["name"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="type like PRIVATE OR GOVERNMENTAL"
    )
    return to_type


# type of the organization
async def org_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["type"] = str(update.message.text)
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your email"
    )
    return to_email_org


# register email
async def org_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["email"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your phone number"
    )
    return to_phone_number_org


# register phone number
async def org_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["phoneNumber"] = update.message.text
    org_profile["houseNumber"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="tell us about your organization"
    )
    return to_description


# about the organization
async def org_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["description"] = update.message.text
    await context.bot.send_message(chat_id=context._user_id, text="send your linkdin")
    return to_linkedin_org


async def org_linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["linkedin"] = update.message.text
    await context.bot.send_message(chat_id=context._user_id, text="send your website")
    return to_website


# register website
async def org_website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["website"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id,
        text="where we can find you for example 'addis ababa, bole, 01'",
    )
    return to_address


# register address
async def org_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    org_profile["city"], *org = [k.strip() for k in update.message.text.split(",")]
    await context.bot.send_message(
        chat_id=context._user_id, text="do you agree tell me"
    )
    return to_save


# register client
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

# name of the client
async def full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["telegramId"] = str(context._user_id)
    client_profile["telegramUsername"] = str(context._user_id) + "@telegram"
    client_profile["firstName"], client_profile["lastName"] = update.message.text.split(
        " "
    )
    await context.bot.send_message(
        chat_id=context._user_id, text="date of birth '2001-11-05'"
    )
    return to_date_of_birth

# register date of birth
async def date_of_birth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["dateOfBirth"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your email like "
    )
    return to_email

# register email
async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["email"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send your phone number"
    )
    return to_phone_number

# register phone number
async def phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["phoneNumber"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id,
        text="what is your highest education level eg:  'HIGHSCHOOL', 'BSC', 'MSC', 'PHD'",
    )
    return to_highest_education_level

# register highest education level
async def highest_education_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["highestEducationLevel"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="link of your protfolio"
    )
    return to_portfolio

# register portfolio
async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["portfolio"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your cv"
    )
    return to_cv

# register cv
async def cv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["cv"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your github account"
    )
    return to_github

# register github
async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["github"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="please send link of your linkedin account"
    )
    return to_linkedin

# register linkedin
async def linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client_profile["linkedin"] = update.message.text
    await context.bot.send_message(
        chat_id=context._user_id, text="do you agree tell me"
    )
    return to_save

# save the data
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    replay_keyboard = [
        [InlineKeyboardButton("YES", callback_data="save")],
        [InlineKeyboardButton("EXIT", callback_data="exit")],
    ]
    markup = InlineKeyboardMarkup(replay_keyboard)
    await context.bot.send_message(
        chat_id=context._user_id,
        text="are you sure?",
        reply_markup=markup,
    )
    return to_done

# save the data
async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "save":
        if client_profile != {}:
            profile = {"telegramId": str(context._user_id)}
            for i in ["highestEducationLevel", "portfolio", "cv", "github", "linkedin"]:
                if i in client_profile:
                    profile[i] = client_profile[i]
                    del client_profile[i]
            request = Request_to_Django(
                endpoint="http://localhost:5000/api/v1/employee/register"
            )
            res = request.post_request(client_profile)
            request = Request_to_Django(
                endpoint="http://localhost:5000/api/v1/profile/create"
            )
            res_pro = request.post_request(profile)
            await context.bot.send_message(chat_id=context._user_id, text="test")

        if org_profile != {}:  # register organization
            request = Request_to_Django(
                endpoint="http://localhost:5000/api/v1/org/register"
            )
            res_org = request.post_request(org_profile)
            print(org_profile, res_org.text)
            if res_org.status_code == 200:
                await context.bot.send_message(chat_id=context._user_id, text="Done")
            else:
                await context.bot.send_message(
                    chat_id=context._user_id, text="some thing went wrong"
                )
        return ConversationHandler.END
    else:
        await context.bot.send_message(chat_id=context._user_id, text="Bye")
        return ConversationHandler.END

# exit the conversation
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
        register_client: [
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
        register_org: [
            CallbackQueryHandler(
                register_org,
            ),
            CallbackQueryHandler(
                exit,
            ),
        ],
        to_org_name: [MessageHandler(~filters.COMMAND, org_name)],
        to_type: [MessageHandler(~filters.COMMAND, org_type)],
        to_email_org: [MessageHandler(~filters.COMMAND, org_email)],
        to_description: [MessageHandler(~filters.COMMAND, org_description)],
        to_phone_number_org: [MessageHandler(~filters.COMMAND, org_phone_number)],
        to_website: [MessageHandler(~filters.COMMAND, org_website)],
        to_address: [MessageHandler(~filters.COMMAND, org_address)],
        to_linkedin_org: [MessageHandler(~filters.COMMAND, org_linkedin)],
    },
    fallbacks=[CommandHandler("cancel", start)],
)


app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

app.add_handler(conversation_one)

app.run_polling()
