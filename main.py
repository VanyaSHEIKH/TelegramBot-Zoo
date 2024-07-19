import telebot
from config import TOKEN
from telebot import types
from questions import questions
from totem_beast import totem_info
import random

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("👋 Поздороваться")
    button2 = types.KeyboardButton("❓ О викторине")
    button3=types.KeyboardButton("⚠️ Связь с сотрудником зоопарка")
    markup.add(button1, button2,button3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который поможет тебе подобрать твое 'тотемное животное'.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text=="👋 Поздороваться"):
        bot.send_message(message.chat.id,text="Привеееет...")
    elif (message.text=="❓ О викторине"):
        bot.send_message(message.chat.id,text="Чем я могу помочь?")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("💬 Кто я и для чего я нужен?")
        button2=types.KeyboardButton("🐬 Что за 'тотемное животное'?")
        button3=types.KeyboardButton("🤪 Нажми меня!")
        back=types.KeyboardButton("🏠︎ Вернуться в главное меню")
        markup.add(button1,button2,button3,back)
        bot.send_message(message.chat.id,text="Задай мне вопрос",reply_markup=markup)
    elif (message.text=="❗О викторине"):
        bot.send_message(message.chat.id, text="Чем я могу помочь?")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("💬 Кто я и для чего я нужен?")
        button2 = types.KeyboardButton("🐬 Что за 'тотемное животное'?")
        button3 = types.KeyboardButton("🤪 Нажми меня!")
        backer=types.KeyboardButton("🔙 Вернуться")
        markup.add(button1, button2, button3,backer)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    elif (message.text=="🔙 Вернуться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("❗О викторине")
        button2 = types.KeyboardButton("⚠️ Связь с сотрудником зоопарка")
        starter = types.KeyboardButton("👉 Давай начнем наш тест 👈")
        markup.add(button1, button2, starter)
        bot.send_message(message.chat.id,text="Вы вернулись в главное меню",reply_markup=markup)
    elif (message.text=="💬 Кто я и для чего я нужен?"):
        bot.send_message(message.chat.id,text="У меня нет имени, но, возможно, нам получится придумать мне имя 🤔.\
 Я был создан, чтобы помочь вам определиться со своим 'тотемным животным'.")
    elif (message.text=="🐬 Что за 'тотемное животное'?"):
        bot.send_message(message.chat.id,text="Всё вокруг нас является энергией, которая собирается в клубки. Она окутывает окружающие предметы, может давать им силу или, наоборот, отнимать её.\
 Существует также понятие «эгрегор» — это общее биополе, которое создается мыслями определенной группы.\
 На протяжении тысячелетий людьми создавались эгрегоры тотемных животных. Это тоже сгустки энергии, которые обладают характеристиками разных животных, птиц и насекомых. Они не умеют в прямом смысле прыгать как заяц или летать как голубь.\
 Тотемное животное — это покровитель, который наделяет человека теми качествами, которыми обладает сам.\
 Он даёт человеку энергию для выполнения конкретного действия в физическом мире.")
    elif (message.text=="🤪 Нажми меня!"):
        bot.send_message(message.chat.id,text="🗿")
    elif (message.text=="🏠︎ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ О викторине")
        button3=types.KeyboardButton("⚠️ Связь с сотрудником зоопарка")
        starter = types.KeyboardButton("👉 Давай начнем наш тест 👈")
        markup.add(button1, button2,button3,starter)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню, и теперь мы готовы приступить к тесту 'Какое у вас тотемное животное'!" ,reply_markup=markup)
    elif (message.text == "👉 Давай начнем наш тест 👈"):
        send_question(message)
    elif (message.text=="⚠️ Связь с сотрудником зоопарка"):
        contact_staff(message)
    elif (message.text=="➡️ Продолжить"):
        bot.send_message(message.chat.id,text="Спасибо за уделенное время!💖\
Надеемся вы нашли для себя свое 'тотемное животное'. Позвольте нам еще рассказать о программе опеки. Программа опеки от Московского зоопарка предоставляет уникальную возможность стать опекуном за \
конкретным животным, проживающим в зоопарке. Участвуя в этой программе, вы фактически поддерживаете выбранное вами \
животное, помогая обеспечить его уход, кормление и медицинское обслуживание.\n\nПроцесс участия в программе опеки \
обычно включает в себя выбор конкретного животного из числа доступных опекунству, заключение специального договора \
и уплату ежемесячного или ежегодного взноса. В качестве опекуна вы можете получить сертификат, фотографии вашего \
животного, регулярные обновления и информацию о жизни и благосостоянии вашего подопечного.\n\nДеньги, собранные от \
программы опеки, обычно направляются на улучшение условий содержания животных в зоопарке, их медицинское обслуживание, \
а также на проведение научных исследований и программы охраны природы.\n\nУчастие в программе опеки позволяет вам не \
только поддержать зоопарк, но и получить уникальный опыт взаимодействия с животным миру, а также быть частью \
благотворительной деятельности. Подробнее: https://moscowzoo.ru/")
    elif (message.text=="🚪 Вернуться в главное меню"):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("❗О викторине")
        button2 = types.KeyboardButton("⚠️ Связь с сотрудником зоопарка")
        starter = types.KeyboardButton("👉 Давай начнем наш тест 👈")
        markup.add(button1, button2, starter)
        bot.send_message(message.chat.id,text="Вы вернулсь в главное меню. Не забывайте рассказывать своим друзьям и близким о нашей программе. \
Поделитесь с ними нашим Телеграм-ботом: https://t.me/skillfacforZOO_bot. Возможно кто-то среди них и есть тот самый 'лев-тигр'🐯🐾 ❤ ",reply_markup=markup)
    elif (message.text=="🔄 Пройти тест заново"):
        send_question(message)
    else:
        bot.send_message(message.chat.id,text="Такой командой я пока не умею пользоваться")

@bot.message_handler(content_types=['text'])
def contact_staff(message):
    bot.send_message(message.chat.id,
                     "Если у вас возникли какие-то вопросы по функционалу Телеграм-бота или предложения по его улучшению, обращайтесь на почту: zoopark@culture.mos.ru. Наши специалисты обязательно ответят вам в ближайшее время.")


user_answers = []
questions_iterator = iter(questions)
def handle_answer(message):
    try:
        user_answers.append(message.text)
        send_question(message)
    except StopIteration:
        send_final_message(message)

def send_question(message):
    try:
        question_data = next(questions_iterator)
        question = question_data["question"]
        answers = question_data["answers"]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for answer in answers:
            markup.add(types.KeyboardButton(answer))
        msg = bot.send_message(message.chat.id, text=question, reply_markup=markup)
        bot.register_next_step_handler(msg, handle_answer)
    except StopIteration:
        send_final_message(message)

def send_final_message(message):
    totem_animal = determine_totem_animal(user_answers)
    if totem_animal in totem_info:
        info, image_url = totem_info[totem_animal]
        bot.reply_to(message, f"Твое тотемное животное - {totem_animal}: {info}")
        bot.send_photo(message.chat.id, image_url)
    else:
        bot.reply_to(message, "Кажется, что-то пошло не так. Не удалось определить твое тотемное животное.")
    bot.send_message(message.chat.id, f"Спасибо за участие в тесте! Ваши ответы: {', '.join(user_answers)}.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton("🚪 Вернуться в главное меню")
    button2=types.KeyboardButton("➡️ Продолжить")
    button3=types.KeyboardButton("🔄 Пройти тест заново")
    markup.add(button1,button2,button3)
    msg = bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
    bot.register_next_step_handler(msg, func)
    reset_bot()  # Сброс состояния бота для возможности повторного прохождения теста

def reset_bot():
    global user_answers
    global questions_iterator
    user_answers = []
    questions_iterator = iter(questions)

def determine_totem_animal(user_answers):
    return random.choice(list(totem_info.keys()))  # Ваша логика определения тотемного животного

bot.infinity_polling()
