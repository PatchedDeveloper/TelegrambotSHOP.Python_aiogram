from aiogram import types, Dispatcher
from create import dp,bot
from keyboards import kb_Klient
from data_base import sqlite_db


async def welcome (message:types.message):
    await bot.send_message(message.from_user.id,'Ассортимент товаров постепенно пополняется, управление ботом осуществляется кнопками ниже.',reply_markup=kb_Klient)


async def contacts(message:types.message):
    await bot.send_message(message.from_user.id,"<b>Для заказа товара, позвоните по одному из номеров ниже</b>\n\n 89063017555 - Михаил\n 89276229400 - Данила\n\n Примечание: Если вам нет 18 лет, сделка совершена не будет!❌",parse_mode='html')

async def evolve_menu_comand(message: types.Message):
    await sqlite_db.sql_read(message)

def register_hendlers_klient(dp : Dispatcher):
    dp.register_message_handler(welcome,commands=['start', 'help'])
    dp.register_message_handler(contacts,commands=['Связаться_с_нами📞'])
    dp.register_message_handler(evolve_menu_comand, commands=['Ассортимент_товаров📦'])

