
from telebot import types
import telebot


bot = telebot.TeleBot('7639309400:AAGgQEymq5rj0hckQhPM7TrTx9T3gZTIWP0')

@bot.message_handler(commands=['start'])
def main(message):

    bot.send_message(message.chat.id, '<u>Правила игры:</u>\n\n<b>Успей поймать Глинча до 31. 12. 2024</b>\n\n1. <b>Отвечайте на вопросы Новогоднего эльфа</b> и ищите вместе мелкого воришку Глинча — жмите «В погоню!», чтобы начать.\n2. <b>Каждый ваш ответ важен:</b> он или приближает, или отдаляет вас от поимки подлеца.\n3. <b>По пути собирайте бонусы</b>, которые помогут вам привлекать новые лиды.\n\nИграйте, пока не поймаете Глинча, его должен кто-то остановить!\n\n4. <b>Дадим сверху еще 5 000 бонусных рублей</b> на наши обучающие курсы, если отправите ссылку на игру другу!\n• Копируйте ссылку на эту страницу: <a href="https://t.me/GlinchBot">@GlinchBot</a>\n• Отправляйте ее друзьям в соцсетях, на почту или в мессенджерах\n• Делайте скриншот сообщения или поста\n• И присылайте его нам на почту: <a href="mailto:admin@1ps.ru">admin@1ps.ru</a>', parse_mode='html')
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Начать игру', callback_data='start_game')
    markup.add(button)
    bot.send_message(message.chat.id, '<b>Новогодний эльф</b>, сейчас <em>онлайн</em>\n\nОбычно под Новый год случаются чудеса. Но не в этот раз....', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'start_game')
def handle_start_game(call):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('В погоню!', callback_data='run')
    markup.add(button)
    bot.send_message(call.message.chat.id, 'Пока вы скупали мандарины и наряжали елку, все ваши лиды и сделки украл коварный преступник. Во дела! Но еще есть шанс спасти праздник и вернуть себе честно нажитое.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'run')
def handle_run(call):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Начать поиски воришки', callback_data='search')
    markup.add(button)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nПривет! Ну что, новости крайне печальные. Новогодний переполох сыграл на руку Глинчу – мелкому пакостнику. Он как-то проник в вашу воронку и украл все-все сделки и лиды.\n\nИ теперь в новогодние праздники вы рискуете просидеть без продаж! Нужно поймать Глинча, пока следы его ботинок еще виднеются на снегу…', parse_mode='html',reply_markup=markup)



    #Начало всех веток
@bot.callback_query_handler(func=lambda call: call.data == 'search')
def handle_search(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Попробую сам', callback_data='self')
    button2 = types.InlineKeyboardButton('Обращусь к профи', callback_data='professional')
    markup.row(button1, button2)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nПопробуешь поискать его сам или обратишься за помощью к опытным сыщикам?', parse_mode='html',reply_markup=markup)




    #Ветка "Попробую сам"
@bot.callback_query_handler(func=lambda call: call.data == 'self')
def handle_self(call):
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton('Опрошу подозреваемых', callback_data='suspects')
    markup.add(button3)
    button4 = types.InlineKeyboardButton('Осмотрю место преступления', callback_data='place')
    markup.add(button4)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nОтлично! Не будем терять времени. С чего начнешь?', parse_mode='html',reply_markup=markup)



    #Ветка "Опрошу подозреваемых"
@bot.callback_query_handler(func=lambda call: call.data == 'suspects')
def handle_suspects(call):
    markup = types.InlineKeyboardMarkup()
    button5 = types.InlineKeyboardButton('Когда пропали лиды?', callback_data='when')
    markup.add(button5)
    button6 = types.InlineKeyboardButton('Куда дел лиды? Признавайся!', callback_data='where')
    markup.add( button6)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nТэк-с, подумаем, кто как отче наш знает, откуда берутся лиды и где они хранятся? Неужели маркетолог мог быть в сговоре с Глинчем?! Надо срочно задать ему вопрос!', parse_mode='html', reply_markup=markup)



    #Ветка "Когда пропали лиды"
@bot.callback_query_handler(func=lambda call: call.data == 'when')
def handle_when(call):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Мда, понятнее не стало', callback_data='line')
    markup.add(button)
    bot.send_message(call.message.chat.id,'<em>«Вчера. Буквально отвернулся на секундочку, а они пропали»</em>, – всхлипывая произнес маркетолог. <em>«Видел, как что-то зеленое исчезает в окне. А ведь офис на 15 этаже. Чертовщина какая-то…»</em>', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'line')
def handle_line(call):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Осмотреть место преступления', callback_data='line1')
    markup.add(button)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nПостой, кажется, на компьютере, с помощью которого были варварски похищены лиды, есть кое-какая зацепка!',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'line1')
def handle_line1(call):
    markup = types.InlineKeyboardMarkup()
    button12 = types.InlineKeyboardButton('По-любому хомячил печенье с Глинчем', callback_data='cookies')
    markup.add(button12)
    button13 = types.InlineKeyboardButton('Что за вкладочки?', callback_data='tabs')
    markup.add( button13)
    photo_path = 'img/place.png'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id,photo=photo,caption='<b>Новогодний эльф</b>\n\nСледы ботинок на снегу уже замело, но на столе сеошника повсюду свежие крошки от рождественского печенья, в комнате витает какой-то знакомый, еле уловимый, запах, а на компьютере открыто несколько любопытных вкладочек!',parse_mode='html', reply_markup=markup)


    #Ветка "Куда дел лиды"
@bot.callback_query_handler(func=lambda call: call.data == 'where')
def handle_where(call):
    markup = types.InlineKeyboardMarkup()
    button7 = types.InlineKeyboardButton('Это же был единственный свидетель!', callback_data='line2')
    markup.add(button7)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nМаркетолог отказался говорить и расплакался. Неудивительно! Кто же так давит на бедного человека…',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'line2')
def handle_line2(call):
    markup = types.InlineKeyboardMarkup()
    button10 = types.InlineKeyboardButton('Грустно… Хочу сыграть снова', callback_data='replay')
    markup.add(button10)
    button11 = types.InlineKeyboardButton('Давайте чек-лист! Пойду новогоднюю акцию придумывать, не до игр...', callback_data='line3')
    markup.add(button11)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nМаркетолог убежал домой и вряд ли теперь вернется...\n\n\nНо не расстраивайтесь – держите *чек-лист по подготовке сайта к новому году*.\n\n\nВсе-таки вам теперь в одиночку придется устраивать новогоднюю акцию, чтобы привлечь хоть немножко клиентов. А надо было головой думать... или обращаться к профессионалам.',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'line3')
def handle_line3(call):
    url = "https://go.1ps.ru/promo/?fm_promocode=7393986585"
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nЗабирайте чек-лист даром:\n' '<a href="https://go.1ps.ru/promo/?fm_promocode=7393986585">Большой новогодний гайд: как подготовить сайт к празднику и получить продажи</a>\n\n' 'Еще успеете подготовить свой сайт к Новому году и привлечь новые лиды!\n\nУдачи! ',parse_mode='html'.format(url))


@bot.callback_query_handler(func=lambda call: call.data == 'replay')
def handle_replay(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Попробую сам', callback_data='self')
    button2 = types.InlineKeyboardButton('Обращусь к профи', callback_data='professional')
    markup.row(button1, button2)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nПопробуешь поискать его сам или обратишься за помощью к опытным сыщикам?',parse_mode='html', reply_markup=markup)




    #Ветка "Осмотрю место преступления"
@bot.callback_query_handler(func=lambda call: call.data == 'place')
def handle_place(call):
    markup = types.InlineKeyboardMarkup()
    button12 = types.InlineKeyboardButton('По-любому хомячил печенье с Глинчем', callback_data='cookies')
    markup.add(button12)
    button13 = types.InlineKeyboardButton('Что за вкладочки?', callback_data='tabs')
    markup.add(button13)
    photo_path = 'img/place.png'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo=photo, caption='<b>Новогодний эльф</b>\n\nСледы ботинок на снегу уже замело, но на столе сеошника повсюду свежие крошки от рождественского печенья, в комнате витает какой-то знакомый, еле уловимый, запах, а на компьютере открыто несколько любопытных вкладочек!',parse_mode='html', reply_markup=markup)



    #Ветка "По-любому хомячил печенье с Глинчем"
@bot.callback_query_handler(func=lambda call: call.data == 'cookies')
def handle_cookies(call):
    markup = types.InlineKeyboardMarkup()
    button14 = types.InlineKeyboardButton('Играть заново', callback_data='replay1')
    markup.add(button14)
    button15 = types.InlineKeyboardButton('Эх, пойду смотреть курс', callback_data='course')
    markup.add(button15)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nА сеошник, между прочим, честно работал ровно до 18:00. Крошки явно оставили позже. Подозреваете не того.\n\n\nВот утешительный приз в помощь:<em> *Курс SEO BASE *</em>\n\n\nВедь теперь вам придется самостоятельно выводить сайт в топ. Сеошник уволился и такого предательства не простил... Надо было обращаться к профессионалам.',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'replay1')
def handle_replay1(call):
        markup = types.InlineKeyboardMarkup()
        button12 = types.InlineKeyboardButton('По-любому хомячил печенье с Глинчем', callback_data='cookies')
        markup.add(button12)
        button13 = types.InlineKeyboardButton('Что за вкладочки?', callback_data='tabs')
        markup.add(button13)
        photo_path = 'img/place.png'
        with open(photo_path, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo=photo, caption='<b>Новогодний эльф</b>\n\nСледы ботинок на снегу уже замело, но на столе сеошника повсюду свежие крошки от рождественского печенья, в комнате витает какой-то знакомый, еле уловимый, запах, а на компьютере открыто несколько любопытных вкладочек!',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'course')
def handle_course(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Забрать SEO BASE бесплатно', url='https://go.1ps.ru/promo/?fm_promocode=738775ZG'))
    bot.send_message(call.message.chat.id,'Забрать SEO BASE бесплатно', reply_markup=markup)



    #Ветка "Что за вкладочки?"
@bot.callback_query_handler(func=lambda call: call.data == 'tabs')
def handle_tabs(call):
    markup = types.InlineKeyboardMarkup()
    button16 = types.InlineKeyboardButton('А вдруг сеошник дал ему пароли?', callback_data='password')
    markup.add(button16)
    button17 = types.InlineKeyboardButton('Хоть тут все в порядке!', callback_data='good')
    markup.add(button17)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nВебмастер, Яндекс Метрика, Яндекс.Директ, Googlе Search Console...\n\n\nХм... может, Глинч пытался узнать, как мы эти лиды получили. Но судя по тому, что войти в аккаунты не вышло, это ему не удалось!',parse_mode='html', reply_markup=markup)



    #Ветка "Хоть тут все в порядке!"
@bot.callback_query_handler(func=lambda call: call.data == 'good')
def handle_good(call):
    markup = types.InlineKeyboardMarkup()
    button18 = types.InlineKeyboardButton('Играть заново', callback_data='replay2')
    markup.add(button18)
    button19 = types.InlineKeyboardButton('Эх, пойду смотреть курс', callback_data='course1')
    markup.add(button19)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nНо лидов-то это вам не вернет! Пока вы радовались, Глинч сбежал безвозвратно с Вашими лидами.\n\n\nВот утешительный приз в помощь: <em>*Курс SEO BASE*</em>\n\n\nВедь теперь вам придется собирать лиды заново. Надо было обращаться к профессионалам.',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'replay2')
def handle_replay2(call):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Попробую сам', callback_data='self')
        button2 = types.InlineKeyboardButton('Обращусь к профи', callback_data='professional')
        markup.row(button1, button2)
        bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nПопробуешь поискать его сам или обратишься за помощью к опытным сыщикам?',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'course1')
def handle_course1(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Забрать SEO BASE бесплатно', url='https://go.1ps.ru/promo/?fm_promocode=738775ZG'))
    bot.send_message(call.message.chat.id,'Забрать SEO BASE бесплатно', reply_markup=markup)



    #Ветка "А вдруг сеошник дал ему пароли?"
@bot.callback_query_handler(func=lambda call: call.data == 'password')
def handle_password(call):
    markup = types.InlineKeyboardMarkup()
    button20 = types.InlineKeyboardButton('Очень стыдно', callback_data='shameful')
    markup.add(button20)
    button21 = types.InlineKeyboardButton('На войне как на войне', callback_data='war')
    markup.add(button21)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nА он, между прочим, служил вам верой и правдой...2 месяца! Не стыдно его в таком подозревать?',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'shameful')
def handle_shameful(call):
    markup = types.InlineKeyboardMarkup()
    button22 = types.InlineKeyboardButton('Сыграть еще раз', callback_data='replay3')
    markup.add(button22)
    bot.send_message(call.message.chat.id,'Сеошник и правда не виноват. Зря вы его подозревали.',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'replay3')
def handle_replay3(call):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Попробую сам', callback_data='self')
    button2 = types.InlineKeyboardButton('Обращусь к профи', callback_data='professional')
    markup.row(button1, button2)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nПопробуешь поискать его сам или обратишься за помощью к опытным сыщикам?',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'war')
def handle_war(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Забрать SEO BASE бесплатно', url='https://go.1ps.ru/promo/?fm_promocode=738775ZG'))
    bot.send_message(call.message.chat.id, 'Сеошник не смог простить такого предательства и уволился...Что ж, придется самостоятельно добывать лиды. Держите <em>*курс SEO BASE*</em>\n\n\nНо не переживайте, курс огненный, сможете разобраться во всем самостоятельно!', parse_mode='html', reply_markup=markup)





    #Ветка "Обращусь к профи"
@bot.callback_query_handler(func=lambda call: call.data == 'professional')
def handle_professional(call):
    markup = types.InlineKeyboardMarkup()
    button23 = types.InlineKeyboardButton('Обратиться в детективное агенство', callback_data='agency')
    markup.add(button23)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nПравильно! У нас нет времени на самодеятельность, ведь, если нет лидов - нет продаж... ',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'agency')
def handle_agency(call):
    markup = types.InlineKeyboardMarkup()
    button24 = types.InlineKeyboardButton('Огласите список подозреваемых', callback_data='list')
    markup.add(button24)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nЧто ж, придется ударить по свинке-копилке - детективные агентства берут немало. Но результат важнее! Кстати, детективы уже кое-что накопали.',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'list')
def handle_list(call):
    markup = types.InlineKeyboardMarkup()
    button25 = types.InlineKeyboardButton('SEO-специалист', callback_data='seo')
    markup.add(button25)
    button26 = types.InlineKeyboardButton('Маркетолог', callback_data='marketing')
    markup.add(button26)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nОказывается, у Глинча все-таки был сообщник среди ваших сотрудников, и это попало на камеры! Как думаете, кто это?',parse_mode='html', reply_markup=markup)



    #Ветка "SEO-специалист"
@bot.callback_query_handler(func=lambda call: call.data == 'seo')
def handle_seo(call):
    markup = types.InlineKeyboardMarkup()
    button27 = types.InlineKeyboardButton('Извиниться', callback_data='sorry')
    markup.add(button27)
    button28 = types.InlineKeyboardButton('Ну и ладно, он мне никогда не нравился', callback_data='never')
    markup.add(button28)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nА вот и нет! Вы заподозрили честного человека. Он ушел насовсем. И кто теперь будет заниматься вашим сайтом?',parse_mode='html', reply_markup=markup)


    #Ветка "Извиниться"
@bot.callback_query_handler(func=lambda call: call.data == 'sorry')
def handle_sorry(call):
    markup = types.InlineKeyboardMarkup()
    button24 = types.InlineKeyboardButton('Огласите список подозреваемых', callback_data='list')
    markup.add(button24)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nЧто ж, придется ударить по свинке-копилке - детективные агентства берут немало. Но результат важнее! Кстати, детективы уже кое-что накопали.',parse_mode='html', reply_markup=markup)


    #Ветка "Ну и ладно, он мне никогда не нравился"
@bot.callback_query_handler(func=lambda call: call.data == 'never')
def handle_never(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Забрать SEO BASE бесплатно', url='https://go.1ps.ru/promo/?fm_promocode=738775ZG'))
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nЧто ж, раз вы такой самостоятельный, то и сайт продвигать тоже будете сами.Надеюсь, наш подарок вам поможет. Ловите!',parse_mode='html', reply_markup=markup)
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nНе переживайте, курс огонь, сможете сделать и перелидоз, если будете прилежным учеником =)',parse_mode='html')



    #Ветка "Маркетолог"
@bot.callback_query_handler(func=lambda call: call.data == 'marketing')
def handle_marketing(call):
    markup = types.InlineKeyboardMarkup()
    button29 = types.InlineKeyboardButton('Отругать', callback_data='scold')
    markup.add(button29)
    button30 = types.InlineKeyboardButton('Вместе придумать решение', callback_data='decision')
    markup.add(button30)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nВ точку! Научите уже его закрывать офис. Глинч проник именно в тот момент, когда маркетолог отвлекся на очередной мем в соцсетях, еще и дверь придержал ему.',parse_mode='html', reply_markup=markup)



    #Ветка "Отругать"
@bot.callback_query_handler(func=lambda call: call.data == 'scold')
def handle_scold(call):
    markup = types.InlineKeyboardMarkup()
    button31 = types.InlineKeyboardButton('Вместе придумать решение', callback_data='together')
    markup.add(button31)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nОн очень-очень сожалеет и божится, что больше так не будет. Но лиды-то это вам не вернет...',parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'together')
def handle_together(call):
    markup = types.InlineKeyboardMarkup()
    button32 = types.InlineKeyboardButton('Да конечно, пусть!', callback_data='let')
    markup.add(button32)
    button33 = types.InlineKeyboardButton('Пожалеть маркетолога =(', callback_data='regret')
    markup.add(button33)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nПока еще не поздно, можно запустить контекст и привлечь новые лиды.\n\nРаз маркетолог накосячил, пусть теперь и отдувается.',parse_mode='html', reply_markup=markup)



    #Ветка "Вместе придумать решение"
@bot.callback_query_handler(func=lambda call: call.data == 'decision')
def handle_decision(call):
    markup = types.InlineKeyboardMarkup()
    button32 = types.InlineKeyboardButton('Да конечно, пусть!', callback_data='let')
    markup.add(button32)
    button33 = types.InlineKeyboardButton('Пожалеть маркетолога =(', callback_data='regret')
    markup.add(button33)
    bot.send_message(call.message.chat.id,
                     '<b>Новогодний эльф</b>\n\nПока еще не поздно, можно запустить контекст и привлечь новые лиды.\n\nРаз маркетолог накосячил, пусть теперь и отдувается.',
                     parse_mode='html', reply_markup=markup)

    #Ветка "Да конечно, пусть!"
@bot.callback_query_handler(func=lambda call: call.data == 'let')
def handle_let(call):
    markup = types.InlineKeyboardMarkup()
    button34 = types.InlineKeyboardButton('Реклама рекламой, а Глинча надо остановить!', callback_data='advertisement')
    markup.add(button34)
    button35 = types.InlineKeyboardButton('Остановлю погоню и сосредоточусь на рекламе', callback_data='stop')
    markup.add(button35)
    bot.send_message(call.message.chat.id,'<b>Новогодний эльф</b>\n\nУрок пошел на пользу, в следующий раз будет повнимательнее.\n\nЧтобы загладить свою вину, маркетолог предлагает абсолютно бесплатно запустить контекстную рекламу. Вам придется раскошелиться только на рекламный бюджет.',parse_mode='html', reply_markup=markup)



    #Ветка "Остановлю погоню и сосредоточусь на рекламе"
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def handle_stop(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Настроить контекстную рекламу бесплатно ', url='https://go.1ps.ru/promo/?fm_promocode=2725W695'))
    bot.send_message(call.message.chat.id, '<b>Новогодний эльф</b>\n\nНу тоже решение!\n\n\nС помощью догоняющей рекламы мы заберем лиды назад! Пока директолог будет все настраивать, вы можете расслабиться и наконец отдохнуть.',parse_mode='html', reply_markup=markup)



    #Ветка "Реклама рекламой, а Глинча надо остановить!"
@bot.callback_query_handler(func=lambda call: call.data == 'advertisement')
def handle_advertisement(call):
    markup = types.InlineKeyboardMarkup()
    button36 = types.InlineKeyboardButton('Вперед, в кофейню!', callback_data='coffee')
    markup.add(button36)
    button37 = types.InlineKeyboardButton('Разве эта улика? Подожду другую!', callback_data='evidence')
    markup.add(button37)
    bot.send_message(call.message.chat.id,'Как раз в это время детективы принесли новую улику - с помощью детектора запахов, определили, что в комнате сеошника пахло кофе и кокосом. Тут вы вспоминаете, что буквально за углом есть кофейня, где готовят кокосовый раф. ',parse_mode='html', reply_markup=markup)



    #Ветка "Вперед, в кофейню!"
@bot.callback_query_handler(func=lambda call: call.data == 'coffee')
def handle_coffee(call):
    markup = types.InlineKeyboardMarkup()
    button38 = types.InlineKeyboardButton('Верните мои лиды!', callback_data='lidy')
    markup.add(button38)
    button39 = types.InlineKeyboardButton('Всем здравствуйте! Поговорим?', callback_data='talk')
    markup.add(button39)
    photo_path = 'img/Glinch.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(call.message.chat.id, photo=photo, caption='Еще с порога вы увидели, что Глинч сидит и о чем-то беседует с вашим самым главным конкурентом, попивая кофе. АГА!',parse_mode='html', reply_markup=markup)




    #Ветка "Разве эта улика? Подожду другую!"
@bot.callback_query_handler(func=lambda call: call.data == 'evidence')
def handle_cevidence(call):
    markup = types.InlineKeyboardMarkup()
    button38 = types.InlineKeyboardButton('Играть заново', callback_data='replay4')
    markup.add(button38)
    button39 = types.InlineKeyboardButton('Эх, пойду смотреть курс', callback_data='course2')
    markup.add(button39)
    bot.send_message(call.message.chat.id,
                     'Пока вы ждали, Глинч продал ваши лиды конкуренту. Иногда каждая секунда дорога!Вот утешительный приз: <em>*Курс SEO BASE*</em>\n\nВедь теперь вам придется собирать лиды с нуля.',
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'replay4')
def handle_replay4(call):
    markup = types.InlineKeyboardMarkup()
    button29 = types.InlineKeyboardButton('Отругать', callback_data='scold')
    markup.add(button29)
    button30 = types.InlineKeyboardButton('Вместе придумать решение', callback_data='decision')
    markup.add(button30)
    bot.send_message(call.message.chat.id,
                     '<b>Новогодний эльф</b>\n\nВ точку! Научите уже его закрывать офис. Глинч проник именно в тот момент, когда маркетолог отвлекся на очередной мем в соцсетях, еще и дверь придержал ему.',
                     parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'course2')
def handle_course2(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('Забрать SEO BASE бесплатно', url='https://go.1ps.ru/promo/?fm_promocode=738775ZG'))
    bot.send_message(call.message.chat.id, 'Забрать SEO BASE бесплатно', reply_markup=markup)



    #Ветка "Пожалеть маркетолога =("
@bot.callback_query_handler(func=lambda call: call.data == 'regret')
def handle_regret(call):
    markup = types.InlineKeyboardMarkup()
    button42 = types.InlineKeyboardButton('Ладно, давайте хоть чек-лист…', callback_data='humility')
    markup.add(button42)
    button43 = types.InlineKeyboardButton('Какой чек-лист? Пусть пашет!', callback_data='outrage')
    markup.add(button43)
    bot.send_message(call.message.chat.id,
                     '<b>Новогодний эльф</b>\n\nИногда жалость – это плохое чувство, ведь придется все брать в свои руки. Но ничего, маркетолог оставил вам чек-лист, как подготовить сайт к новому году. Может, хоть так пару лидочков наскребете.',
                     parse_mode='html', reply_markup=markup)



    #Ветка "Ладно, давайте хоть чек-лист…"
@bot.callback_query_handler(func=lambda call: call.data == 'humility')
def handle_humility(call):
    bot.send_message(call.message.chat.id,
                     '<b>Новогодний эльф</b>\n\nДержите: <a href="https://go.1ps.ru/promo/?fm_promocode=7393986585"Большой новогодний гайд: как подготовить сайт к празднику и получить продажи</a>\n\nПусть за вашу доброту и сострадание придет много-много лидов! А в Новом году получится все задуманное!',
                     parse_mode='html')



    #Ветка "Какой чек-лист? Пусть пашет!"
@bot.callback_query_handler(func=lambda call: call.data == 'outrage')
def handle_outrage(call):
    markup = types.InlineKeyboardMarkup()
    button32 = types.InlineKeyboardButton('Да конечно, пусть!', callback_data='let')
    markup.add(button32)
    button33 = types.InlineKeyboardButton('Пожалеть маркетолога =(', callback_data='regret')
    markup.add(button33)
    bot.send_message(call.message.chat.id,
                     '<b>Новогодний эльф</b>\n\nПока еще не поздно, можно запустить контекст и привлечь новые лиды.\n\nРаз маркетолог накосячил, пусть теперь и отдувается.',
                     parse_mode='html', reply_markup=markup)




    #Ветка "Верните мои лиды!" и "Всем здравствуйте! Поговорим?" \ Конец игры
@bot.callback_query_handler(func=lambda call: call.data == 'lidy')
def handle_lidy(call):
    url = "https://go.1ps.ru/promo/?fm_promocode=8W3558499Z"
    bot.send_message(call.message.chat.id,'Ладно, что уж тянуть. Вы молодец! Поздравляем! Еще бы минутка и было поздно, но вы поймали воришек с поличным... Лиды вам вернули, Глинч извинился. Конкурент выплатил  неустойку 5000 рублей.' '<a href="https://go.1ps.ru/promo/?fm_promocode=8W3558499Z"> Забрать денежки!</a>',parse_mode='html'.format(url))
    markup = types.InlineKeyboardMarkup()
    button40 = types.InlineKeyboardButton('Правила получения подарка тут ', callback_data='rules')
    markup.add(button40)
    bot.send_message(call.message.chat.id, '<b>Отправляй игру другу – пусть тоже поищет преступника и спасет свои продажи!</b>\n\nА мы вам за это дадим 5 000 рублей на любые наши курсы по SEO, SMM, маркетингу и рекламе. Правила получения подарка тут :)', parse_mode='html',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'talk')
def handle_talk(call):
    url = "https://go.1ps.ru/promo/?fm_promocode=8W3558499Z"
    bot.send_message(call.message.chat.id,'Ладно, что уж тянуть. Вы молодец! Поздравляем! Еще бы минутка и было поздно, но вы поймали воришек с поличным... Лиды вам вернули, Глинч извинился. Конкурент выплатил  неустойку 5000 рублей.' '<a href="https://go.1ps.ru/promo/?fm_promocode=8W3558499Z"> Забрать денежки!</a>',parse_mode='html'.format(url))
    markup = types.InlineKeyboardMarkup()
    button40 = types.InlineKeyboardButton('Правила получения подарка тут ', callback_data='rules')
    markup.add(button40)
    bot.send_message(call.message.chat.id,'<b>Отправляй игру другу – пусть тоже поищет преступника и спасет свои продажи!</b>\n\nА мы вам за это дадим 5 000 рублей на любые наши курсы по SEO, SMM, маркетингу и рекламе. Правила получения подарка тут :)',parse_mode='html', reply_markup=markup)





    # Правила получение подарка
@bot.callback_query_handler(func=lambda call: call.data == 'rules')
def handle_rules(call):
        bot.send_message (call.message.chat.id,'<b>Как получить 5 000 бонусных рублей сверху</b>\n\n• Копируйте ссылку на эту страницу: <a href="https://t.me/GlinchBot">@GlinchBot</a>\n• Отправляйте ее друзьям в соцсетях, на почту или в мессенджерах\n• Делайте скриншот сообщения или поста\n• И присылайте его нам на почту: <a href="mailto:admin@1ps.ru">admin@1ps.ru</a>\n• В ответ мы отправим подарок\n\nБонусные рубли сможете потратить на оплату любого нашего обучающего курса!', parse_mode='html')







bot.polling(none_stop=True)