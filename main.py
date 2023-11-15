import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
TOKEN = ""
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def on_startup(_):
    print('бот запущен')

ADMIN_NAME = 'Real_gray_butch'
users = []
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text = "⚪Меню⚪")
    keyboard.add(button_1)
    await message.answer(
        '<em>/start-<b>запуск бота</b>\n<b>/media-наши сотц.сети</b>\n<b>/help-список всех коман</b></em>',
        parse_mode='HTML',
        reply_markup=keyboard)
    await message.delete()

@dp.message_handler(commands=['media'])
async def send_media(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=3)
    btn1 = InlineKeyboardButton(text="🟦Наш VK🟦",
                                url='https://vk.com/club218336196')
    ikb.add(btn1)
    btn2 = InlineKeyboardButton(text="🔷Наш telegram канал🔷",
                                url='https://t.me/+2blsFBK73_1iMTgy')
    ikb.add(btn2)

    btn3 = InlineKeyboardButton(text="🌄Наш instagram 🌄",
                                url='https://instagram.com/galinanumerolog?igshid=ZDdkNTZiNTM=')
    ikb.add(btn3)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Можете перейти в наши сотц.сети:', reply_markup=ikb)
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_7 = types.KeyboardButton(text="⚪Меню⚪")
    keyboard.add(button_7)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Можете вернуться в меню нажав на кнопну ниже",
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button_1 = types.KeyboardButton(text="Подарок🎁")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text='Консультация🌺')
        keyboard.add(button_2)
        await bot.send_message(chat_id=message.from_user.id,
                           text=f"Здравствуйте, {message.from_user.first_name}."
                                "Я помогу вам с помощью нумерологии разобраться в себе,получить ответы на волнующие вопросы."
                                "А ещё я умею дарить подарки🙂.",
                           reply_markup=keyboard)
        await message.delete()

@dp.message_handler(content_types=['text'])
async def lucke_funck(message: types.Message ):
    if message.text == "Подарок🎁":
        await bot.send_message(chat_id=message.from_user.id,
                                text="""Вы получаете подарок в виде рассчета вашего личного ангела-хранителя🎁

Хранители следят за жизнью «подопечного», помогают с трудностями и спасают от опасностей и негатива.🧘‍♀️ 
Чтобы узнать, кто вас оберегает, напишите дату вашего рождения полностью.
(Например: 12.03.2003)
""")

    elif len(message.text) == 10 and message.text[2] == '.' and message.text[5] == '.':
        date = message.text
        sum = 0
        for digit in date:
            if digit.isdigit():
                sum += int(digit)
        while sum > 9:
            new_sum = 0
            for digit in str(sum):
                new_sum += int(digit)
            sum = new_sum
        if sum == 1:
            await message.reply('''Ваш ангел-хранитель под номером 1🧚‍♀️

Пол Ангела-хранителя —женский. 
Святой ангел, считается наиболее быстрым защитни­ком, приходящим на помощь еще до того, как об этом опросят Ваша покровительница —Казанская Божья Ма­терь. Она к вам относится, как к дитю, которого нужно лелеять и холить, оберегать в сложных ситуациях и вести по жизни за руку. Но вы, как любой ребёнок, хотите са­мостоятельности, которая чаще всего заканчивается неприятностями —долги, травмы и ссоры, проблемы со здоровьем. Но Божья Матерь простит и поймёт, если вы осознаете свои проступки. Когда они постоянно будут повторяться, то можете получить большое наказание —серьёзные недуги, удары судьбы с потерей близкого че­ловека и многое другое. Попросите прощения у своего ангела-покровителя, сходите в церковь и поставьте свечу около его иконы. Всё наладится —Казанская Божья Ма­терь не может долго злиться.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 2:
            await message.reply('''Ваш ангел-хранитель под номером 2🫂

Пол Ангела-хранителя —мужской. 
Светлый ангел (или ангел света), имеет обыкновение являться во сне. Ангелы света оставляют своим подопеч­ным родинки, зачастую на лице Вам помогают идти по жизни ангелы света. Знаком их любви являются вес­нушки на вашем теле, а также родинки: чем их больше, тем сильнее чувства к вам. Они дают советы спомощью сновидений. Поэтому, если есть какие-то важные вопро­сы, встаньте перед сном у окна и протяните руки к небу, задайте мысленно вопрос и ложитесь спать. Вы увидите вещее сновидение. Постарайтесь его запомнить, если же оно вылетит из вашей головы, значит ангелы считают, что вы не нуждаетесь в их совете и вам стоит полагаться только на себя. Но вы всё равно поблагодарите их.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 3:
            await message.reply('''Ваш ангел-хранитель под номером 3🪁️

Воздушный ангел, сопровождает людей,склонных к авантюрам и риску. Оказываясь рядом, нередко выдает свое присутствие шорохом крыльев.
Она довольно строгая, поэтому не любит, когда её не слушают. Обычно о своём неудовольствии она сообщает простым способом —неудачный день, полный различных казусов: потеря небольшой суммы денег, спотыкание, по­рванная обувь или одежда, но всё это можно легко испра­вить. Обязательно посетите на следующий день храм,поставьте свечку. Что­бы ваш ангел-хранитель могл давать вам советы, сблизьтесь с девушкой по имени Варя, через неё вы сможете получать необходимую информацию. Она будет верной
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 4:
            await message.reply('''Ваш ангел-хранитель под номером 4👁

Пол Ангела-хранителя —мужской. 
Мудрый ангел общается со своим подопечным с помо­щью подсказок и верных решений, что положительно сказывается на интеллекте и карьере человека.
Вашего ангела-хранителя, как гово­рится, не побалуешь, он не терпит подопечных, которые сорят деньгами, сквернословят и ведут неприличный об­раз жизни.
Таких он наказывает строго, но по совести, у транжир отнимает деньги, лодырей заставляет работать, делая всё для этого, а на тех, кто выражается нецензурной речью, насылает болезни, связанные с голосовыми связками.
И только осознание неправильного поведения даёт шанс начать жизнь по-новому-без проблем и хлопот. Те же, кто нравится ему, ни в чём никогда не нуждают­ся, он старается их благодарить за их благие деяния и ста­рания. Но и им стоит не забывать его благодарить за это, ходить в церковь хотя бы по большим праздникам.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 5:
            await message.reply('''Ваш ангел-хранитель под номером 5🫧

Пол Ангела-хранителя —женский. 
Металлический ангел наделяет человека долгими го­дами жизни. Получает особую подпитку от слез, поэтому приходит на помощь, когда подопечный плачет. Если вы не чисты на руку и на язык, то вам будет тяжело по жиз­ни, так как ваш ангел-хранитель,не терпит тех, кто ворует и врёт. Её наказание жестоко —она может устроить человеку тяжёлую жизнь с лишением свободы или же с постоянными серьёзными проблемами.Если же вы человек честный,то ангел только добавит приятных сюрпризов в вашу жизнь.
Молиться за ангела надо только 28 августа.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 6:
            await message.reply('''Ваш ангел-хранитель под номером 7💝

Пол Ангела-хранителя — женский.
Энергетический ангел — самый обидчивый.
Нуждается в постоянной благодарности, не терпит 
грубых слов и непризнания своих заслуг Вам достался са­
мый добрый ангел-хранитель.
Она всегда помогает всем, и не только своим подопеч­
ным, а их она особенно любит и жалеет их, даже там, где 
человек и сам мог бы справиться, если постарается. Одна­ко,если она разозлится, то наказание у неё серьёзное-за обиды делает человека изгоем, за обман-серьёзное заболевание и т.п.Поэтому её нельзя выводить из терпе­ния.В день её памяти-2 мая, подопечный обязатель­но должен поднести дары нуждающимся-деньги бед­ным или же заняться благотворительностью, например, посетив дом ребёнка или престарелых людей.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 7:
            await message.reply('''Ваш ангел-хранитель под номером 8🎆

Пол Ангела-хранителя — мужской.
Милосердный ангел,является воплощением души умерших предков,внимательно заботится,но испытыва­ет потребности в воспоминаниях о нем.Вас оберегают ан­гелы умерших родственников,которые знали вас хорошо и при жизни,поэтому они могут вас наказывать как и в земном мире и за те же провинности, которые им не нравились при жизни.Обратите внимание, после чего у вас наступает чёрная полоса и кому из умерших родных могло не понравиться ваше поведение. За покой души этого человека и ставьте свечу в поминальные дни и дни его смерти. Он смягчится и поможет в решении проблем, 
как малых, так и серьёзных.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 8:
            await message.reply('''Ваш ангел-хранитель под номером 8🎆

Пол Ангела-хранителя — мужской.
Милосердный ангел,является воплощением души умерших предков,внимательно заботится,но испытыва­ет потребности в воспоминаниях о нем.Вас оберегают ан­гелы умерших родственников,которые знали вас хорошо и при жизни,поэтому они могут вас наказывать как и в земном мире и за те же провинности, которые им не нравились при жизни.Обратите внимание, после чего у вас наступает чёрная полоса и кому из умерших родных могло не понравиться ваше поведение. За покой души этого человека и ставьте свечу в поминальные дни и дни его смерти. Он смягчится и поможет в решении проблем, 
как малых, так и серьёзных.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)
        elif sum == 9:
            await message.reply('''Ваш ангел-хранитель под номером 9🌤

Пол Ангела-хранителя — женский.
Теплый ангел обеспечивает подопечного гармонией с миром и пониманием сути вещей.Именно ангелы Тепла чаще других воплощаются в жи­вотных.Ваш ангел-хранитель всегда будет рядом с целеустремлёнными, поможет им достичь желаемого. А вот те, кто не привык бороться за своё счастье,будут ею наказаны мелкими неприятно­стями, которые должны сподвигнуть на большие дела. Но, если и после такой встряски ничего не получится,стоит 
ждать беды- тяжёлые болезни, ссоры, потеря дорогих людей и другое.
За помощью к ангелу нужно обращаться в женские дни и мужчинам и женщинам,поставьте свеч­ку за своё здравие.
''')
            keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            button_5 = types.KeyboardButton(text="🟢Да🟢")
            keyboard.add(button_5)
            button_6 = types.KeyboardButton(text="🔴Нет🔴")
            keyboard.add(button_6)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)

    elif message.text == "Консультация🌺":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button_5 = types.KeyboardButton(text="🟢Да🟢")
        keyboard.add(button_5)
        button_6 = types.KeyboardButton(text="🔴Нет🔴")
        keyboard.add(button_6)
        await bot.send_message(chat_id=message.from_user.id,
                               text="Желаете получить личный нумерологический разбор?💫", reply_markup=keyboard)

    elif message.text == "🟢Да🟢":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button_7 = types.KeyboardButton(text="⚪Меню⚪")
        keyboard.add(button_7)
        ikb = InlineKeyboardMarkup(row_width=2)
        btn1 = InlineKeyboardButton(text="❇️Наш WhatsApp❇️",
                                url='https://api.whatsapp.com/send?phone=79370806995')
        ikb.add(btn1)
        btn2 = InlineKeyboardButton(text="🔷Наш telegram🔷",
                                    url='https://t.me/galinasimonova1979')
        ikb.add(btn2)
        await bot.send_message(chat_id=message.from_user.id,
                               text='''Я рад, что ваша жизнь вам интересна и вы стремитесь ее улучшить. Самая сложная работа, это работа над собой!
Консультация проходит в любом удобном мессенджере путем голосовых сообщений. Это дает возможность слушать их в удобном для вас режиме.🙃
Как желаете продолжить?
''', reply_markup=ikb)
        await bot.send_message(chat_id=message.from_user.id,
                               text= 'Теперь можете вернуться в главное меню', reply_markup=keyboard)
    elif message.text == "🔴Нет🔴":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button_7 = types.KeyboardButton(text="⚪Меню⚪")
        keyboard.add(button_7)
        await bot.send_message(chat_id=message.from_user.id,
                           text="В таком случае вы можете вернуться в меню нажав на кнопну ниже",
                           reply_markup=keyboard)



    elif message.text == "⚪Меню⚪":
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button_1 = types.KeyboardButton(text="Подарок🎁")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text='Консультация🌺')
        keyboard.add(button_2)
        await bot.send_message(chat_id=message.from_user.id,
                           text=f"{message.from_user.first_name},вы вернулись в главное меню, выберите дальнейшие действия",
                           reply_markup=keyboard)

    #else:
        #await message.reply("❗НЕВЕРНАЯ ФОРМА ДАТЫ РОЖДЕНИЯ, ВВЕДИТЕ ПО ФОРМЕ (ДД.ММ.ГГГГ)❗")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=on_startup)


