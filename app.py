import telebot
from config import keys, TOKEN
from extensions import CryptoConverter, ConvertionException

bot=telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start','help'])
def help(message:telebot.types.Message):
    text='Для начала работы введите команду боту в формате:  \n<имя валюты> \
<название валюты для перевода><количество переводимой валюты>\nУвидеть  список всех валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message:telebot.types.Message):
    try:
        values= message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Неверное к-во заданных параметров.')

        quote, base, amount = values

        total_base= CryptoConverter.get_price(quote,base,amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text= f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

