import sys,os
import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main
# from config import TOKEN
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
print(TOKEN)

async def main():
    await async_main()
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')