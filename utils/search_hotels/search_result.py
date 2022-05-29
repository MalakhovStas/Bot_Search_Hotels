from datetime import datetime
from typing import List

from telebot.types import InputMediaPhoto, CallbackQuery

from loader import bot, logger
from utils.decorators import exception_control
from database import database_utility
from utils.search_hotels import sort_hotels, hotel_info, find_hotel_photos


@exception_control.func_exception_control
def func_result(call: CallbackQuery) -> None:
    """
    Отправляет пользователю результат поиска отелей согласно сценарию(command) от пользователя и
    записывает его в базу данных истории поиска.
    """

    with bot.retrieve_data(user_id=call.from_user.id) as data:
        hotels: dict = data['hotels']
        show_num_hotels: int = data['show_num_hotels']
        show_num_photos_hotel: int = data['show_num_photos_hotel']
        command: str = data['command']

    date = datetime.now().strftime("%d / %m / %Y  %H:%M:%S")
    total_info: str = f'Запрос:    {command}\n{date}\n{"-" * 60}\n'

    if show_num_hotels:
        hotels: List[dict] | None = sort_hotels.func_sort_hotels(command=command, hotels=hotels, user_data=call)

        if show_num_hotels > len(hotels):
            show_num_hotels = len(hotels)

        for number in range(show_num_hotels):
            bot.send_chat_action(chat_id=call.from_user.id, action='upload_document', timeout=2)

            hotel: dict = hotels[number]
            info_hotel: str = hotel_info.func_hotel_info(hotel=hotel, user_data=call)
            if show_num_photos_hotel:
                photos: List[str] | List[None] = find_hotel_photos.func_find_photos(hotel=hotel,
                                                                                    num_photos=show_num_photos_hotel,
                                                                                    user_data=call)

                bot.send_media_group(chat_id=call.message.chat.id, media=[InputMediaPhoto(photo) for photo in photos])

            bot.send_message(chat_id=call.message.chat.id, text=f'{info_hotel}', disable_web_page_preview=True)

            total_info += f'{info_hotel}{"-" * 60}\n'

    database_utility.insert_history(user_id=call.from_user.id, history=total_info, date=date, user_data=call)
    bot.delete_state(user_id=call.from_user.id)

    logger.info(f'-> OK -> command: {command} -> completed successfully')
