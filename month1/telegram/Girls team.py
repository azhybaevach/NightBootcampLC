import logging
from aiogram import Bot, Dispatcher, executor, types
import random
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
#from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

markup = ReplyKeyboardMarkup()
markup.add(KeyboardButton('/start'), KeyboardButton('/help'), KeyboardButton('/adv'))

API_TOKEN = '5821815346:AAHCKz_zDtrGlDqaiBfarzNJlY0E3cJcqwc'


# messagemarkup = InlineKeyboardMarkup()
# messagemarkup.add(InlineKeyboardButton('интеллектуальное', callback_data='intel'),
#                   InlineKeyboardButton('физическое', callback_data='physic'),
#                   InlineKeyboardButton('развлечение', callback_data='fun'))



LIST_COMMANDS = '''
/intel📚 - список задач связанных с интеллектуальной работой
/physic💪🏻 - список задач связанных с физической работой
/fun🥳 - задачи для веселья
'''



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешно запущен')

intel = {
  "читай": "прочитай одну статью в интернете",
  "стихотворение": "выучи одно стихотворение",
  "шахматы": "поиграй шахматы с ботом"
}

physic = {
    "приседание": "сделай 20 приседаний",
    "йога": "поделй йогу 40 минут",
    "пробежка": "пробежка 30 минут"
}

fun = {
    "кино": "посмотри свой любимый фильм",
    "music": "послушай свою любимую музыку",
    "звонок другу": "позвони лучшему другу"
}

#@dp.message_handler(commands=['start', 'help'])
#async def send_welcome(message: types.Message):
#    await message.answer('Начинаем игру "Эрудит"', reply_markup=markup)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(text=f'Начинаем игру{LIST_COMMANDS}', reply_markup=markup)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer(text='"Привет, друг!\nЯ помогу тебе выбрать случайные задания\nТы согласен? Тогда нажми /start.")', reply_markup=markup)

@dp.message_handler(commands=['adv'])
async def send_welcome(message: types.Message):
    await message.answer('Команда девчонок вперед! 👊', reply_markup=markup)
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIm05kO_VM7kobIm2lnv91GSyyZVxI3wACkRIAAvzw4UodOfjG8l2Msy8E')

# @dp.callback_query_handler()
# async def help_command(call: types.callback_query):
#     await bot.send_message(chat_id=call.from_user.id, )
#     # await call.answer()


@dp.message_handler(commands=['intel'])
async def help_command(message: types.Message):
    await message.answer(random.choice(list(intel.values())))

@dp.message_handler(commands=['physic'])
async def help_command(message: types.Message):
    await message.reply(random.choice(list(physic.values())))

@dp.message_handler(commands=['fun'])
async def help_command(message: types.Message):
    await message.reply(random.choice(list(fun.values())))
    if message == random.choice(list(fun["music"])):
        await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIm05kO_VM7kobIm2lnv91GSyyZVxI3wACkRIAAvzw4UodOfjG8l2Msy8E')







if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



