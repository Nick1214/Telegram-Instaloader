from Bot.config import token
from aiogram import Bot, Dispatcher, executor, types
import logging
import instaloader
import asyncio
import os

bot = Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
array_with_buttons_1 = ["Скачать фото/видео из аккаунта", "Получить информацию о профиле"]
keyboard.add(*array_with_buttons_1)

#
# @dp.message_handler(commands=["info"])
# async def get_bot_info(message: types.Message):
#     await message.answer("!!! ВНИМАНИЕ КРИСТИНОЧКА!!!")
#     await message.answer("Если ты хочешь парсить закрытые аккаунты, то ничего не получится")
#     await message.answer(
#         "Если хочешь, я могу сделать так чтобы ты в свой аккаунт входила и смотрела страницы, на которые подписана")
#     await message.answer("В том числе и закрытые")
#     await message.answer("А так только открытые")
#     await message.answer("Да и вообще, я этим ботом поиграться просто хотел, да  и я ленивый")
#     await message.answer("Так что пользуйся пока тем что есть")
#     await message.answer("😘")
#     await message.answer("Напиши /start для начала работы")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот для анализа инстаграм аккаунтов. Выберите команду:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == str(array_with_buttons_1[1]))
async def get_profile_name(message: types.Message):
    await message.answer("Введите название профиля для обработки")
    await message.answer("Примечание! Первым словом указываем #, а дальше имя профиля")
    await message.answer("Например: #bla-bla-bla")

    @dp.message_handler(lambda message: message.text[0] == "#")
    async def get_profile_info(message: types.Message):
        profile_name = message.text[1:]
        await message.answer("Получаем информацию...")
        try:
            insta = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(insta.context, profile_name)

            Fullname = profile.full_name
            Get_followers = profile.followers
            GetFollowings = profile.followees
            Biography = profile.biography
            AccountClosed = profile.is_private
            await message.answer(f"Полное имя: {Fullname}")
            await message.answer(f"Количество подписчиокв: {Get_followers}")
            await message.answer(f"Количество подписок: {GetFollowings}")
            if Biography is None:
                await message.answer("Доп информация отстуствует")
            else:
                await message.answer(f"Доп Информация: {Biography}")
            if AccountClosed is False:
                await message.answer("Аккаунт не закрыт")
            else:
                await message.answer("Аккаунт закрыт...")
            posts = profile.get_posts()
            count = 0
            dct = {}

            for post in posts:
                count += 1
                post_username = post.profile
                post_date = post.date
                post_likes = post.likes
                post_url = post.url
                post_comments = post.comments
                # print(f"Username: {post_username}, Date: {post_date}, Likes: {post_likes}, URL: {post_url}")
                dct = {
                    "post_date": post_date,
                    "post_likes": post_likes,
                    "post_url": post_url,
                    "The number of post": count,
                }
                for key, value in dct.items():
                    await message.answer(f"{key} -> {value}")
        except Exception:
            await message.answer(
                "Профиля не существует!")
            await message.answer("Если аккаунт закрыт, бот работать не будет")

    @dp.message_handler(lambda message: message.text[0] != "#")
    async def print_out_error(message: types.Message):
        await message.answer("Неправильно введено имя профиля! Поставьте # в начало!")


@dp.message_handler(lambda message: message.text == str(array_with_buttons_1[0]))
async def get_profile_name(message: types.Message):
    await message.answer("Введите название профиля для обработки")
    await message.answer("Примечание! Первым словом указываем #, а дальше имя профиля")
    await message.answer("Например: #bla-bla-bla")

    @dp.message_handler(lambda message: message.text[0] == "#")
    async def download_profile(message: types.Message):
        try:
            await message.answer("Получаем информацию....")
            insta = instaloader.Instaloader()
            profile_name = message.text[1:]
            insta.download_profile(profile_name)
            await message.answer("Получаем информацию....")
            await message.answer(
                "Скачиваем информацию..."
            )
            await message.answer(
                "Это может занять какое то время....")
            await message.answer("Скачано!")

        except Exception:
            await message.answer("Профиля не существует!")
            await message.answer("Если аккаунт закрыт, бот работать не будет")

    @dp.message_handler(lambda message: message.text != "#")
    async def print_out_error(message: types.Message):
        await message.answer("Неправильно введено имя профиля! Поставьте # в начало!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)