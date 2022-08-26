from aiogram.utils import executor
from create import dp
from data_base import sqlite_db

###message from developer or host checker
async def on_startup(_):
    print('Bot online')
    sqlite_db.sql_start()

from hendlers import klient,admin,other

klient.register_hendlers_klient(dp)
admin.register_handlers_admin(dp)
other.register_hendlers_other(dp)


executor.start_polling(dp,skip_updates=True,on_startup=on_startup)