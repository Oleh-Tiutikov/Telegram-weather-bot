from email import message
import telebot
import pyowm

owm = pyowm.OWM('8dbaabb6be69f2b55d5d908c1118e254')
bot = telebot.TeleBot("5221406376:AAEWZBHqCUidNP7hEzisyWqthvjcIRvs3dw") 
mgr = owm.weather_manager()



@bot.message_handler(content_types=['text'])
def send_echo(message):

    observation = mgr.weather_at_place('Lviv')
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "У Львові зараз: " + w.detailed_status + "\n"
    answer += "Температура " + str(temp) + " градусів" + "\n\n"

    
    if temp < 10:
        answer += ("Зараз дуже холодно, вдягайся тепліше!")
    elif temp < 15:
        answer += ("Зараз нормальна погода, вдягай що хочеш!")
    else:
        answer += ("Зараз дуже тепло, вдягайся у легкий одяг")

    bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
