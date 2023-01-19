from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Это чат-бот технической поддержки ООО МТК "ТехноСофт"💻' 'Выберите необходимый раздел 👇', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/tssupport_bot')

@dp.message_handler(commands=['Режим_работы'])
async def tech_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'График работы: с 9:00 до 18:00')

@dp.message_handler(commands=['Адрес'])
async def tech_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Юридический адрес: 129626, Г.Москва, вн.тер.г. Муниципальный Округ Алексеевский, пр-кт Мира, д. 102, к. 1')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(tech_open_command, commands=['Режим_работы'])
    dp.register_message_handler(tech_place_command, commands=['Адрес'])
