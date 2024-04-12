import telebot

with open("token.txt", 'r') as token_file:
    token = token_file.read()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):  #Стартовая функция


    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = telebot.types.InlineKeyboardButton("🐤Когда работает 'Птичка'?")
    button2 = telebot.types.KeyboardButton("🫱🏿‍🫲🏻Хотите посотрудничать?")
    button3 = telebot.types.KeyboardButton("🚯Как сдавать вторсырье?")
    button4 = telebot.types.KeyboardButton("♻️Что можно сдать?")
    button5 = telebot.types.KeyboardButton("🤑Вознаграждение за вторсырье?")
    button6 = telebot.types.InlineKeyboardButton("👔Мероприятия")
    button7 = telebot.types.KeyboardButton("🤔Не нашлось ответа?")

    keyboard.add(button1)

    keyboard.row(button3, button4, button5)

    keyboard.add(button6)

    keyboard.row(button2, button7)


    bot.send_photo(message.chat.id, "https://cdn.discordapp.com/attachments/1038793739818238063/1228279150780088380/image.png?ex=662b7719&is=66190219&hm=6706214f9ffd7b7f1cd10c4cdf8ec5a9f76a1a3f7ca18215d7886de6bc31db9e&", caption="Сделайте мир чище вместе с «Птичкой»! Присоединяйтесь к нам и станьте героями экологии уже сегодня!", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Выберите действие:")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):     #Основная функция которая вызовает другие функции при нажатии кнопок
    if message.text == "🐤Когда работает 'Птичка'?":
        get_text_message_street(message)

    elif message.text == "🫱🏿‍🫲🏻Хотите посотрудничать?":
        get_text_message_contact(message)

    elif message.text == "🤑Вознаграждение за вторсырье?":
        get_text_message_money(message)

    elif message.text == "👔Мероприятия":
        get_text_message_event(message)

    elif message.text == "🤔Не нашлось ответа?":
        get_text_message_ans(message)

    elif message.text == "♻️Что можно сдать?":
        get_photo_message_deal(message)

    elif message.text == "🚯Как сдавать вторсырье?":
        get_photo_message_right(message)

    elif message.text == "🏠Вернуться в меню":
        send_welcome(message)


    else:

        subfunctions(message)


def subfunctions(message):   #Функция для второстепенных кнопок
    user_id = message.from_user.id

    markup = telebot.types.InlineKeyboardMarkup()

    if message.text == "Пр. Набережный, 5 стр. 2":

        bot.send_location(user_id, latitude=61.2485657, longitude=73.3603845)

        bot.send_message(user_id, """Вт, Чт, Пт: 14:00 – 19:00

            Сб, Вс.: 11:00 – 16:00

            Пн, Ср.: выходной""")


    elif message.text == "Ул. 30 лет Победы, 21/3":

        bot.send_location(user_id, latitude=61.2546035, longitude=73.4215377)

        bot.send_message(user_id, """Ср, Чт: 14:00 – 19:00

    Сб, Вс: 10:00 – 15:00

    Пн, Вт, Пт: выходной""")


    elif message.text == "Ул. Фармана Салманова, 2":

        bot.send_location(user_id, latitude=61.2411933, longitude=73.4642182)

        bot.send_message(user_id, """Вт, Чт, Пт: 14:00 – 19:00

    Сб, Вс.: 11:00 – 16:00

    Пн, Ср.: выходной""")

        # Мероприятия


    elif message.text == "💸СВОП":

        btnundertext = telebot.types.InlineKeyboardButton('🎉Посмотреть пример мероприятия🎉',
                                                          url="https://vk.com/ptichka_punkt?"

                                                              "w=wall-216486932_967")

        markup.add(btnundertext)

        bot.send_message(user_id, 'Обмен хорошими, но ненужными вещами. '

                                  'Это отличный способ подарить '

                                  'ненужным вещам нового '

                                  'хозяина и самому найти то, что '

                                  'может точно пригодиться! '

                                  'Когда проходят? Стараемся '

                                  'проводить один раз в месяц.', reply_markup=markup)



    elif message.text == "🤠Мастер — классы":

        btnundertext = telebot.types.InlineKeyboardButton('🎉Посмотреть пример мероприятия🎉',

                                                          url="https://vk.com/ptichka_punkt?w=wall-216486932_917")

        markup.add(btnundertext)

        bot.send_message(user_id, 'В рамках наших СВОПов и других '

                                  'мероприятий обычно проходят '

                                  'различные интересные мастер-'

                                  'классы, такие как: роспись одежды, '

                                  'роспись деревянных значков, '

                                  'создание картин из вторсырья и т.п.', reply_markup=markup)


    elif message.text == "🌎Эко - уроки":

        btnundertext = telebot.types.InlineKeyboardButton('🎉Посмотреть пример мероприятия🎉',

                                                          url="https://vk.com/ptichka_punkt?w=wall-216486932_984")

        markup.add(btnundertext)

        bot.send_message(user_id, 'Эко-уроки проводим '

                                  'преимущественно в '

                                  'образовательных учреждениях, '

                                  'включает в себя знакомство с '

                                  'нашим пунктом, процессом сбора и '

                                  'сортировки вторсырья, информация '

                                  'о существующих фракциях и какие '

                                  'принимаем именно мы и т.п. '

                                  'Когда проходят? Можем провести '

                                  'по запросу, а также в рамках других '

                                  'эко-мероприятий.', reply_markup=markup)


    elif message.text == "📚Обмен книгами":

        bot.send_photo(user_id,
                       'https://media.discordapp.net/attachments/1038793739818238063/1228241233630072842/image.png?ex=662b53c9&is=6618dec9&hm=3c666ee28f01dda1ea2ec91d81943b5bfaa3ca915dcabfd9037c0a185fdbb159&=&format=webp&quality=lossless&width=450&height=600',

                       caption='Буккроссинг — на территории '

                               'пунктов у нас существует обмен '

                               'книгами, можно принести свои '

                               'ненужные книги и забрать себе '

                               'приглянувшиеся. Нередко '

                               'получается найти нашему '

                               'посетителю что-то интересное для чтения!', reply_markup=markup)


    elif message.text == "🥰Благотворительность":

        btnundertext1 = telebot.types.InlineKeyboardButton('📌Пример #1',
                                                           url="https://vk.com/ptichka_punkt?w=wall-216486932_923")

        btnundertext2 = telebot.types.InlineKeyboardButton('📌Пример #2',
                                                           url="https://vk.com/ptichka_punkt?w=wall-216486932_1030")

        btnundertext3 = telebot.types.InlineKeyboardButton('📌пример #3',
                                                           url="https://vk.com/ptichka_punkt?w=wall-216486932_1000")

        markup.row(btnundertext1, btnundertext2)

        markup.row(btnundertext3)

        bot.send_message(user_id, 'Каждый месяц мы собираем '

                                  'продуктовые наборы и средства '

                                  'личной гигиены и доставляем '

                                  'одиноким пожилым людям '

                                  'совместно с центром поддержки '

                                  'семей «Круг надежд». '

                                  '\nОрганизовываем сборы для '

                                  'животных приютов корма, '

                                  'амуниции и всех необходимостей, а '

                                  'также проводим акцию «Елки,щепа, '

                                  'добрые дела», в рамках которых '

                                  'собираем елки после нового года и '

                                  'делаем из них щепу, которую '

                                  'перенаправляем ботаническому саду '

                                  '(для утепления растений зимой и '

                                  'т.п.), животным приютам (для '

                                  'настила в вольерах и т.п)', reply_markup=markup)


    elif message.text == "🌠Ещё":

        btnundertext1 = telebot.types.InlineKeyboardButton('📌Мы в ВК',

                                                           url="https://vk.com/ptichka_punkt")

        btnundertext2 = telebot.types.InlineKeyboardButton('📌Наш ТГ',

                                                           url="https://t.me/ptichka_punkt")

        markup.row(btnundertext1, btnundertext2)

        bot.send_message(user_id, 'Наша деятельность очень обширна, '

                                  'мы стараемся создавать много всего '

                                  'интересного и полезного! '

                                  '\nАкции, конкурсы, различные сборы, '

                                  'полезная информация из мира '

                                  'экологии все это можно найти в '

                                  'нашей группе Вконтакте: '

                                  '\nhttps://vk.com/ptichka_punkt \nи '

                                  'Телеграм-канале: '

                                  '\nhttps://t.me/ptichka_punkt '

                                  '\n\nНе упустите много всего классного '

                                  'вместе с «Птичкой»!', reply_markup=markup)


def get_text_message_street(message):   #Функция для графика работы (Кнопка(и ниже я буду писать так же комментарии к
                                        # таким функция))
    user_id = message.from_user.id

    if message.text == "🐤Когда работает 'Птичка'?":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = telebot.types.KeyboardButton('Пр. Набережный, 5 стр. 2')
        btn2 = telebot.types.KeyboardButton('Ул. 30 лет Победы, 21/3')
        btn3 = telebot.types.KeyboardButton('Ул. Фармана Салманова, 2')
        btn4 = telebot.types.InlineKeyboardButton("🏠Вернуться в меню")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(user_id, '❓ Задайте интересующий вопрос', reply_markup=markup)  # ответ бота


def get_text_message_money(message):         #Функция для вознаграждения
    user_id = message.from_user.id

    if message.text == "🤑Вознаграждение за вторсырье?":
        bot.send_message(user_id,"""Рады сообщить, что раз в несколько месяцев в пунктах приема вторсырья будут запускаться акции по сбору определенной фракции, за которую можно будет получить баллы, а баллы обменять на приятные подарки! 
С 13 апреля по 31 мая в пункте приема вторсырья по адресу: ул. Фармана Салманова, 2 будет действовать акция на фракцию «1 ПЭТ (бутылки)» 
Подробнее следить за акцией можно на странице «Птички»:
https://vk.com/ptichka_punkt
И ЕЩЕ! Очень важно, что благотворительный проект « С заботой о старшем поколении» (помощь одиноким людям в виде продуктов, средств личной гигиены и прочих нужд) реализуется на регулярной основе благодаря посетителям экологического проекта АО «Полигон-ЛТД» - пунктов приема вторсырья «Птичка» и жителями, которые складывают крышечки в Чудо-деревья.""")



def get_text_message_event(message):        #Функция для мероприятий
    user_id = message.from_user.id

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("💸СВОП")
    button2 = telebot.types.KeyboardButton("🤠Мастер — классы")
    button3 = telebot.types.KeyboardButton("🌎Эко - уроки")
    button4 = telebot.types.KeyboardButton("📚Обмен книгами")
    button5 = telebot.types.KeyboardButton("🥰Благотворительность")
    button6 = telebot.types.KeyboardButton("🌠Ещё")
    button7 = telebot.types.KeyboardButton("🏠Вернуться в меню")

    markup.row(button1, button2, button3)
    markup.row(button4, button5, button6)
    markup.add(button7)

    bot.send_message(user_id, "Выберите мероприятие", reply_markup=markup)


def get_text_message_ans(message):   #Функция если клиент не нашёл ответ в боте
    user_id = message.from_user.id
    if message.text == "🤔Не нашлось ответа?":
        bot.send_message(user_id, """Способы связи
Номер телефона пунктов: 89322484552 (общая линия, отвечает менеджер
эко-проектов в рабочее время)
Группа Вконтакте: https://vk.com/ptichka_punkt""")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global current_index, current_photo_index_deal

    # Проверяем, была ли нажата кнопка "Следующее фото" для сценария "Правильная сдача"
    if call.data == 'next_photo_r':
        # Обновляем индекс текущей фотографии для сценария "Правильная сдача"
        current_index = (current_index + 1) % len(custom_photos)
        # Отправляем следующую фотографию для сценария "Правильная сдача"
        bot.send_photo(call.message.chat.id, custom_photos[current_index], reply_markup=create_keyboard())

    # Проверяем, была ли нажата кнопка "Следующее фото" для сценария "Сдача вторсырья"
    elif call.data == 'next_photo':
        # Обновляем индекс текущей фотографии для сценария "Сдача вторсырья"
        current_photo_index_deal = (current_photo_index_deal + 1) % len(photos_deal)
        # Отправляем следующую фотографию для сценария "Сдача вторсырья"
        bot.send_photo(call.message.chat.id, photos_deal[current_photo_index_deal], reply_markup=create_keyboard_deal())


# Функция для создания клавиатуры для сценария "Правильная сдача"
def create_keyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Следующее фото', callback_data='next_photo_r')
    markup.add(btn1)
    return markup


# Функция для создания клавиатуры для сценария "Сдача вторсырья"
def create_keyboard_deal():
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Следующее фото', callback_data='next_photo')
    markup.add(btn1)
    return markup

def get_photo_message_right(message):   # Функция для отправки фотографии для сценария "Правильная сдача"
    bot.send_photo(message.chat.id, custom_photos[current_index], reply_markup=create_keyboard())


def get_photo_message_deal(message):    # Функция для отправки фотографии для сценария "Сдача вторсырья"
    bot.send_photo(message.chat.id, photos_deal[current_photo_index_deal], reply_markup=create_keyboard_deal())



def get_text_message_contact(message):      #Функция, если клиент хочет сотрудничать
    user_id = message.from_user.id

    if message.text == "🫱🏿‍🫲🏻Хотите посотрудничать?":
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Написать нам', url="https://tinyurl.com/3nnvm7ku")
        markup.add(btn1)
        bot.send_message(user_id, 'Почта для направления письма с Вашим предложением: info@poligonltd.ru', reply_markup=markup)


photos_deal = [
    'https://sun9-63.userapi.com/impg/PLQztrLXroR34ezSkgz-ZHMhhiEXXyPfqhQbNg/COe3CS5uKvU.jpg?size=604x604&quality=96&sign=c7a6704b24468b3cf4c6fe3244d7a977&c_uniq_tag=9K_0mWlU85Sa770QHpqa0oVkb1qX4FCm1_9F-63UqMI&type=album',
    'https://sun9-6.userapi.com/impg/YflFXUkuxu-qapzNXm2uFQYO7gJZvUgpXlCWyQ/TBdocZw2wnI.jpg?size=604x604&quality=96&sign=a98586fe017a2848c65dd60272e9001e&c_uniq_tag=W-ysQTkoHMMUKY2MZUNwpOudEf5CZhGFVCjjRvMKh54&type=album',
    'https://sun3-23.userapi.com/impg/zyCtMBR7ArEWqXOJ3e7Jh2XH-jAfpTKyj2DWtA/PPEZ-t_vcew.jpg?size=604x604&quality=96&sign=66b5222a97caf06c0fead57accbdd236&c_uniq_tag=ygPt2k3FKFBsv-ZaOY4T7YXhhey498aNGr2LKZyhIwY&type=album',
    'https://sun3-13.userapi.com/impg/ZldO72wrySE_H2dPgVEKKHl6Awis6mrpQUye2A/ygq23Heo-EU.jpg?size=604x604&quality=96&sign=c698b843c84489971837b1d07d658e6d&c_uniq_tag=szweBSdFjZhJ3kjYykJaTm17BXLare-GeXW5OuQ_YJg&type=album',
    'https://sun3-18.userapi.com/impg/k2suP7CcSd3mEmJhvMejXeene14wFTD2y9GQ7g/tKGIlvK78d4.jpg?size=604x604&quality=96&sign=e43a7d1b4cf04f6a0db752d8f664277d&c_uniq_tag=UNe9wZ-cyi2XyfI76zIHnJx75Pm7o0McOCE6RslxwuI&type=album',
    'https://sun9-26.userapi.com/impg/b7HESCPkkXsL9H7UhBUyLjlt7p5RMb6akEUjnw/czYgU44a7AI.jpg?size=604x604&quality=96&sign=847762d29ae407ec27a4249f4487f2e3&c_uniq_tag=n89Uy24_mpFX-VQ20hH0wO_2IUbKWwOPp_MPChVgFtc&type=album',
    'https://sun3-23.userapi.com/impg/_3yoae6qHi5fgQTAf_z-1iEDtKFaMFI_L-DEIw/Ycn5wQrAZmk.jpg?size=604x604&quality=96&sign=32010d75be659958c6724dea8303894c&c_uniq_tag=z6HnO9USRCWHey9IEHKQ5IVjLexnLRPcQBesinlE3B0&type=album',
    'https://sun3-20.userapi.com/impg/w5P7I88OKVyDyN0RMrHZRkwib8jm3EUqUxxkBg/xCZwK5K80Xg.jpg?size=604x604&quality=95&sign=80170a57d81253a620aee59a91e5b209&c_uniq_tag=6eiHG4q7ULkM2Qj6u2M7YSTNvW25ywg9hBDz16Syi2g&type=album'
]       #Массив для фото, которые используется "Сдача вторсырья"

# Индекс текущей фотографии для сценария "Сдача вторсырья"
current_photo_index_deal = 0



custom_photos = [
    'https://sun9-2.userapi.com/impg/ahcfpre7gBIPL6T2MVTWO6FHGB-w6JJluptkWQ/3Rfi7Cj2taE.jpg?size=1080x1080&quality=95&sign=4684b4314f58df1df2e2be40a2f02e19&type=album',
    'https://sun9-75.userapi.com/impg/ZqLKmud9HKkT9fv2T94ra3R6AE6MnkksfpL7wg/uNA0GWVJ6hI.jpg?size=807x807&quality=95&sign=8cb15b508bb720496f66ebedf1bd2e56&c_uniq_tag=CIPhfKoOz_l2wifgiKpQoxb8PaUrNU5u0eDTmXrEinw&type=album',
    'https://sun9-78.userapi.com/impg/8WzXCoywFrC6VnYj88EVS1gpTICWiKWZPeQUzw/-FEBqFyhVt4.jpg?size=807x807&quality=95&sign=1ce8522b3dab95be8c5b060629fba76f&c_uniq_tag=maFXUSeObmp3LN6vUwLx_-JJvm6qsRUEMny2bjtXDXE&type=album',
    'https://sun9-48.userapi.com/impg/BUaJmeLxhUx1w2AVnE5Z9X5B5_NGz_63OiAe8w/QbvjOei_bpQ.jpg?size=807x807&quality=95&sign=364bef4402e4833896a38ba695cf60c8&c_uniq_tag=ZSvAHFw0KIYVakFL0M2B1THtQ0XWYCUNJmjLtjwphy4&type=album',
    'https://sun9-1.userapi.com/impg/sfoLsYjVyr9anF8fxm_hAfra_B-RQI5gSbxXtQ/zyBmJzKT-Eg.jpg?size=807x807&quality=95&sign=9b2f815709ace4a03578dbc5f9e3522f&c_uniq_tag=FEb-Y2NjbOUUwXMJqKFH2HkpNBO5YO1pThoWs9-zYoI&type=album',
    'https://sun9-24.userapi.com/impg/jakud3jTaWNqgIMHyJ2_aDonFZ0BLFMguLr-7Q/ZYKxaUpEv10.jpg?size=807x807&quality=95&sign=d383bec64cff68c61ead0930fe10247b&c_uniq_tag=4Gk-2Mwp6cEjh11hiyTrJIld4Yz01cFKRM543peYFDY&type=album'
]       #Массив для фото, которые используется "Правильная сдача"

# Индекс текущей фотографии для сценария "Правильная сдача"
current_index = 0




if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
