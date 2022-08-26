from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btn1= KeyboardButton('/Связаться_с_нами📞')
btn2= KeyboardButton('/Ассортимент_товаров📦')

kb_Klient=ReplyKeyboardMarkup(resize_keyboard=True)

kb_Klient.row(btn1,btn2)