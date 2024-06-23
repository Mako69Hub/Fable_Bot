import asyncio

from aiogram import Bot, Dispatcher

from app.handlers import router
from confige import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit bot')
