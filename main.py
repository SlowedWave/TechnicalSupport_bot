
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
from db import Database
import functions as fc
from keyboards import kb_client

from config import TOKEN, ADMIN

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Это чат-бот технической поддержки ООО МТК "ТехноСофт"💻\n🔲 Используйте необходимый раздел на клавиатуре 🔲.\n💬 Вы также можете задать свои вопросы 💬.\n<b>--------------- Например ---------------</b>\n📞 <em>"Как я могу с вами связаться ?"</em> 📞\n📚 <em>"О компании/Об организации"</em> 📚', parse_mode="HTML", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/tgtechsoftsupport_bot')


@dp.message_handler(commands=['Режим_работы'])
async def tech_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'График работы: <b>с 9:00 до 18:00</b>', parse_mode="HTML")

@dp.message_handler(commands=['Адрес'])
async def tech_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, '<b>Юридический адрес:</b> 129626, Г.Москва, вн.тер.г. Муниципальный Округ Алексеевский, пр-кт Мира, д.102, к.1', parse_mode="HTML")

@dp.message_handler(commands=['send'])
async def send_user(message : types.Message):
    await message.answer(f'Приветствую <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!')

@dp.message_handler()
async def mess(message : types.Message):
    try:
        answer_id = fc.recognize_questions(message.text, db.get_questions())
        await bot.send_message(message.from_user.id, db.get_answer(answer_id))
    except:
        await message.reply('<b>К сожалению, не найден ответ в БД.</b>\n<b>Свяжитесь с менеджером по поводу данного вопроса.</b>', parse_mode="HTML")


@dp.message_handler(content_types=['any'])
async def p2p_handler(message : types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN:
            if not message.reply_to_message:
                return

            await  bot.forward_message(message.reply_to_message.forward_from_message_id, message.chat.id, message.message_id)


        else:
            await  bot.forward_message(ADMIN, message.chat.id, message.message_id)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

    def register_handlers_client(dp: Dispatcher):
        dp.register_message_handler(start, commands=['start'])
        dp.register_message_handler(tech_open_command, commands=['Режим_работы'])
        dp.register_message_handler(tech_place_command, commands=['Адрес'])