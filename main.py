import random
import smtplib
import psycopg2
from psycopg2 import Error
from aiogram import types
import telebot
from tabulate import tabulate
from telebot import types

bot = telebot.TeleBot('5995765680:AAGvdCX9XW1gk7qHAtIdb4L065D6IUt8xdI') # токен лежит в файле config.py


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text="Вход")
    btn2 = types.KeyboardButton(text="Регистрация")
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, "Добрый день!\nЯ бот ТурИст\nВыберите действие ниже:", reply_markup=kb)


@bot.message_handler(commands=['Дa'])
def add_user_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Итак, начинаем тестирование", reply_markup=markup)

    bot.send_message(message.from_user.id, 'Любите русскую кухню?')
    bot.register_next_step_handler(message, get1)

    global conn
    conn = psycopg2.connect(user="postgres", password="FyeW123@123", host="127.0.0.5", port="5432", database="postgres")


def get1(message):
    global answer1
    answer1 = str(message.text)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer1 = '{answer1}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите грузинскую кухню?')
    bot.register_next_step_handler(message, get2)


def get2(message):
    global answer2
    answer2 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer2 = '{answer2}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите французскую кухню?')
    bot.register_next_step_handler(message, get3)


def get3(message):
    global answer3
    answer3 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer3 = '{answer3}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите итальянскую кухню?')
    bot.register_next_step_handler(message, get4)


def get4(message):
    global answer4
    answer4 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer4 = '{answer4}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите ходить по музеям?')
    bot.register_next_step_handler(message, get5)


def get5(message):
    global answer5
    answer5 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer5 = '{answer5}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите смотреть на памятники?')
    bot.register_next_step_handler(message, get6)


def get6(message):
    global answer6
    answer6 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer6 = '{answer6}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите ходить по скверам?')
    bot.register_next_step_handler(message, get7)


def get7(message):
    global answer7
    answer7 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer7 = '{answer7}' where id = (select max(id) from Email_code);")
    conn.commit()

    bot.send_message(message.from_user.id, 'Любите посещать места для занятия спортом?')
    bot.register_next_step_handler(message, get8)


def get8(message):
    global answer8
    answer8 = message.text

    cursor = conn.cursor()
    cursor.execute(f"UPDATE Email_code SET answer8 = '{answer8}' where id = (select max(id) from Email_code);")

    bot.send_message(message.from_user.id, 'Тестирование завершено\nРекомендуемые места к посещению:')

    str = """
       (SELECT name, coordinates FROM "Russian_cuisine", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer1 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Georgian_cuisine", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer2 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "French_cuisine", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer3 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Italian_cuisine", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer4 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Museums", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer5 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Monuments", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer6 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Squares", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer7 = 'Да' LIMIT 3)
        union
        (SELECT name, coordinates FROM "Sport", "email_code" WHERE email_code.id=(select max(id) from email_code) and Email_code.answer8 = 'Да' LIMIT 3)
     """

    cursor.execute(str)
    myresult = cursor.fetchall()
    bot.send_message(message.from_user.id, tabulate(myresult, headers=['Название', 'Адрес'], tablefmt='simple'))
    print(tabulate(myresult, headers=['Название', 'Адрес'], tablefmt='simple'))

    conn.commit()

    cursor.close()
    conn.close()

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text="Вход")
    btn2 = types.KeyboardButton(text="Регистрация")
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, "Спасибо за использование чат-бота!", reply_markup=kb)

@bot.message_handler(content_types=['text'])
def test(message):
    def start_email(message):
        global email
        global code

        try:
            print('Электронная почта пользователя:', message.text)
            email = str(message.text)
            code_to_email(email)
            if "@" in message.text:
                msg2 = bot.send_message(message.chat.id, 'Введите код проверки')
                bot.register_next_step_handler(msg2, start_code)
        except (Exception, Error) as error:
            print("Ошибка", error)

    def start_code(message):
        print('Код проверки: ', message.text)
        code_people = message.text
        print(email, code_people)

        if code_people == code_generate:
            bot.send_message(message.chat.id, 'Вы успешно авторизованы!')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("/Дa")
            btn2 = types.KeyboardButton("/Нeт")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Готовы пройти небольшое тестирование (8 вопросов)?", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'К сожалению, код неправильный.\nПожалуйста, выполните действия сначала')

    if message.text == 'Вход' or message.text == 'Регистрация':  # Если содержимое == 'One',то
        msg1 = bot.send_message(message.chat.id, 'Введите электронную почту')
        bot.register_next_step_handler(msg1, start_email)


def code_to_email(email):
    global code_generate
    code_generate = str(random.randint(111111, 999999))

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('backup.papers.cherkashin@gmail.com', 'ljbywtxjwejpebcv')
    try:
        smtpObj.sendmail('backup.papers.cherkashin@gmail.com', email, code_generate)
    except (Exception, Error) as error:
        print("Ошибка", error)
    BD_save_email_code(email, code_generate)


def BD_save_email_code(email, code):
    try:
        connection = psycopg2.connect(user="postgres", password="FyeW123@123", host="127.0.0.5", port="5432", database="postgres")

        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO Email_code (Email, Code)
                                           VALUES (%s,%s)"""
        record_to_insert = (email, code)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно добавлена таблицу")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


bot.polling(none_stop=True)





