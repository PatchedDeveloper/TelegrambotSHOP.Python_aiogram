from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot(token='5637146398:AAH8UnbcGjqeulOUToL7_wjRW-ucAD0OV6A')
dp = Dispatcher(bot,storage=storage)