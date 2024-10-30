import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '' 


    
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(TOKEN) 

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("red", callback_data="cb_red"),
                               InlineKeyboardButton("blue", callback_data="cb_blue"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_blue":
        bot.answer_callback_query(call.id, "Answer is blue")
    elif call.data == "cb_red":
        bot.answer_callback_query(call.id, "Answer is red")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "red/blue?", reply_markup=gen_markup())

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "salam alekum")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "aliwiderchi")
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
