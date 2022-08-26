from aiogram import types,Dispatcher
from create import dp



async def echo_send(message : types.message):
   if message.text=='543000':
    try:
      await message.reply('Приветствую в комнате по управлению мной\n 1.Не забудь запустить меня! \nhttps://t.me/EvolveShop_bot \n2.Введи команду доступа к модерированию в этот чат!')
      await message.delete()
    except:
       await message.reply('Напишите боту в личку')

    #await message.reply(message.text)
   # await bot.send_message(message.from_user.id,message.text)


def register_hendlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)