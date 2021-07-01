import telebot

# Adding token
bot = telebot.TeleBot('1893641225:AAGO1n-Ib41ylzwH2roTS4Itq1bO8MJzFO0')

#formatting text
bot = telebot.TeleBot('1893641225:AAGO1n-Ib41ylzwH2roTS4Itq1bO8MJzFO0', parse_mode ="MarkdownV2")

#Handling incoming messages
@bot.message_handler(commands= ['start','help'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Shona's Bot")

#When message is sent to a group
@bot.message_handler(func= lambda message:True)
def handle_all_messages(message):
  if message.chat.type == "private":
      bot.reply_to(message, message.text)
  elif message.chat.type == "group":
        bot.reply_to(message, "Hey you")
       

#Replying when tagged in a group
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, message.text)
    elif message.chat.type == "group":   
        if('@ MwinBot' in message.text):
          bot.reply_to(message, "Hello there")



#Replying to other message content
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)


   

bot.polling()