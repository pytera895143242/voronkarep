import asyncio
import json
from pyrogram import errors
from aiogram import types
from misc import dp, bot
from .sqlit import change_status,cheak_black
import random


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001802786457

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    if call.data == 'sprint_online':
        print('123')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ГОООУ🚀', callback_data='go_1')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 11,reply_markup=markup)

    if call.data == 'go_1':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Давай🤔', callback_data='go_2')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id = 13)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=14)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=15,reply_markup=markup)

    if call.data == 'go_2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='А как?🧐', callback_data='go_3')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=17, reply_markup=markup)

    if call.data == 'go_3':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_4')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=19, reply_markup=markup)

    if call.data == 'go_4':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='КАК?🧐', callback_data='go_5')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=21)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=22,reply_markup=markup)

    if call.data == 'go_5':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🤑СПРИНТ🤑', callback_data='go_6')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=24)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=25, reply_markup=markup)

    if call.data == 'go_6':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔥ДАЛЬШЕ🔥', callback_data='go_7')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=27, reply_markup=markup)

    if call.data == 'go_7':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🚀Начинаем🚀', callback_data='go_8')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=29, reply_markup=markup)

    if call.data == 'go_8':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🚀Начинаем🚀', callback_data='go_9')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=31, reply_markup=markup)

    if call.data == 'go_9':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔎ТЕСТ🔍', callback_data='go_10')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=33, reply_markup=markup)

    if call.data == 'go_10':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='1️⃣', callback_data='ans_t')
        bat_b = types.InlineKeyboardButton(text='2️⃣', callback_data='ans_f')
        bat_c = types.InlineKeyboardButton(text='3️⃣', callback_data='ans_f')
        markup.add(bat_a, bat_b, bat_c)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=35, reply_markup=markup)

    if call.data == 'ans_f':
        await bot.send_message(chat_id=call.message.chat.id, text= 'Нет, это не арбитраж. Попробуй ещё раз')

    if call.data == 'ans_t':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Готово✅', callback_data='go_11')
        markup.add(bat_a)

        await bot.send_message(chat_id=call.message.chat.id, text='Красава😎 Двигаемся дальше')
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=38)
        await asyncio.sleep(10)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=39)
        await asyncio.sleep(10)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=40,reply_markup=markup)

    if call.data == 'go_11':
        change_status(call.message.chat.id)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=42)
        await asyncio.sleep(120) #120
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=44)
        await asyncio.sleep(300) #300
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=46)
        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=48)
        await asyncio.sleep(21600)  #21 600
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=50)
        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=52)
        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=54)
        await asyncio.sleep(43200)  # 43 200
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=56)
        await asyncio.sleep(21600)  #21 600
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=58)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=59)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=60)


    if call.data == 'bat_video2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='12-17', callback_data='sprint_online')
        bat_b = types.InlineKeyboardButton(text='18+', callback_data='bat_video3')
        markup.add(bat_a, bat_b)
        await bot.send_message(chat_id=call.message.chat.id, text= 'Сколько тебе лет?',reply_markup=markup)

    if call.data == 'bat_video3':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Да', callback_data='bat_video4')
        bat_b = types.InlineKeyboardButton(text='Нет', callback_data='sprint_online')
        markup.add(bat_a, bat_b)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты из Ташкента?', reply_markup=markup)

    if call.data == 'bat_video4':
        await bot.send_message(chat_id=call.message.chat.id, text="""Для жителей Ташкента, есть специальное предложение🔥
Подробности тут👉https://t.me/TashkentTelebot""")



    try:
        await bot.answer_callback_query(call.id)
    except:
        pass