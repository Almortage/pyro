import telebot
import random

bot = telebot.TeleBot("توكن بوتك")

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, "ارسل ( تلاو ، تلاوات ، تلاوة )")
    
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "تلاو" or text == "تلاوات" or text == "تلاوة":
        voice_url = "https://t.me/ALMORTAGELRSK/" + str(random.randint(7, 276))
        bot.send_voice(message.chat.id, voice_url, caption="« صلي على سيدنا محمد ﷺ »", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton(text='✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton(text='✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech'),
            telebot.types.InlineKeyboardButton(text='✧ - قناة عالم البرمجه ♥', url='https://t.me/botatiiii')))

bot.polling()