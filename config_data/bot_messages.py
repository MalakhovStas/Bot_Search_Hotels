import inspect
from os.path import basename


class BotSays:
    """Класс методов возвращающих значения словаря SAYS сообщений от бота пользователю"""

    @staticmethod
    def old_keyboard():
        return SAYS.get('old keyboard')

    @staticmethod
    def say(key: str | None = None) -> str:
        """
        Метод извлекает из стека вызовов имя файла, в котором он был вызван и использует это имя в качестве первого
        ключа, если указан key, он используется в качестве второго ключа для извлечения значения словаря
        сообщений от бота пользователю.
        :param key: str | None -> второй параметр составного ключа.
        :return: str -> текстовое сообщение от бота пользователю.
        """
        file = basename(inspect.stack()[1].filename)
        if key:
            return SAYS[file][key]
        else:
            return SAYS[file]


SAYS = \
    {'get_calendar.py': {'travel_in': '&#128071 <b>Выбери дату заселения</b>',
                         'travel_out': '&#128071 <b>Выбери дату отъезда</b>',
                         'date order wrong': 'Дата отъезда должна быть позже даты заселения',
                         'date not valid': 'Дата не актуальна'},
     'get_location.py': {'ok hotels': 'Выбран город:  ',
                         'question': '&#128071 <b>Выбери, сколько отелей показать</b>',
                         'else': 'К сожалению, в этом городе не нашлось отелей',
                         },
     'get_show_num_hotels.py': {'ok state': 'Показать отелей:    ',
                                'question': '&#128071 <b>Показывать фотографии отелей?</b>',
                                },
     'get_show_num_photos_hotel.py': 'Показать фотографий отеля:    ',
     'get_yes_no_show_photos.py': {'yes show photos': '&#128071 <b>Сколько фотографий показать '
                                                      'к каждому отелю?</b>',
                                   'no show photos': 'Фотографии отелей:    <b>не показывать</b>',
                                   },
     'help.py': {'state is None': '&#129302 Помогу подобрать подходящий отель в любом городе планеты, по '
                                  'определенным критериям, нужно выбрать соответствующую команду:\n\n',
                 'command': '&#129302 Сейчас нужно написать город при помощи клавиатуры твоего устройства\n'
                            'или сбросить запрос &#128073 /reset',
                 'location': '&#129302 Сейчас нужно уточнить локацию, нажав одну из кнопок выше &#128070\n'
                             'или сбросить запрос &#128073 /reset',
                 'show_num_hotels': '&#129302 Сейчас нужно выбрать сколько отелей показать, '
                                    'нажав одну из кнопок выше &#128070\n'
                                    'или сбросить запрос &#128073 /reset',
                 'yes_no_show_photos': '&#129302 Сейчас нужно собраться с духом, решить и выбрать, показывать '
                                       'фотографии отелей или нет, нажав соответствующую кнопку выше &#128070\n'
                                       'или сбросить запрос &#128073 /reset',
                 'show_num_photos_hotel': '&#129302 А сейчас нужно выбрать, сколько фотографий к каждому отелю показать'
                                       'нажав одну из кнопок выше &#128070\nили сбросить запрос &#128073 /reset',
                 'travel_calendar': '&#129302 Тут всё совсем просто, выбираем даты заселения и отъезда в отель, '
                                    'посмотри внимательно на календаре &#128070 всё подробно написано.\n'
                                    'или сбросить запрос &#128073 /reset',
                 'history': '&#129302 Сейчас нужно выбрать, какую именно историю поиска показать, нажав одну из кнопок '
                            'выше &#128070\nили сбросить запрос &#128073 /reset',
                 'range_price': '&#129302 При помощи клавиатуры твоего устройства нужно ввести через пробел, диапазон '
                                'цен за сутки проживания, в котором будем искать отели. <b>Пример: 1251,5 2100</b>',
                 'range_distance': '&#129302 При помощи клавиатуры твоего устройства нужно ввести через пробел, '
                                   'диапазон расстояний в км, от отеля до центра города. <b>Пример: 0,75 5.5</b>',
                 'note': '\n\n*примечание: <i>к сожалению, по независящим от меня причинам подбор отелей '
                         'находящихся на территории Российской Федерации временно невозможен.</i>',
                 },
     'history.py': {'question': '&#128071 <b>Выбери какой запрос показать</b>',
                    'no history': 'Истории запросов пока нет'
                    },
     'reset.py': {'error state is None': '&#9888 В моей программе произошла непредвиденная ошибка, попробуй ещё раз '
                                         'или обратись к администратору',
                  'error in state': '&#9888 Упс, твой запрос сброшен &#9888\nВ моей программе произошла непредвиденная '
                                    'ошибка, попробуй ещё раз или обратись к администратору',
                  'not error state is None': '&#129302 Ты ничего не запрашивал, команды тут &#128073 /help',
                  'not error in state': '&#129302 Запрос сброшен, ожидаю новой команды &#128073 /help'

                  },
     'search_commands.py': '&#129302 Напиши в каком городе будем искать отели?',
     'start.py': {'user': 'Я уже давно запущен и жду твоей команды! Если нужно напомнить, '
                          'как со мной обращаться &#128073 /help',
                  'not user': 'Я твой верный друг и помощник! Создан помогать людям в поиске отелей по всему миру. '
                              'Чтобы узнать обо мне больше &#128073 /help'
                  },
     'get_city.py': {'city isdigit': '&#129302 Я не знаю городов с названием из цифр, напиши еще раз '
                                     'или сбрось запрос &#128073 /reset',
                     'city is rubbish': '&#129302 Какая-то белиберда, название города должно состоять из букв, '
                                        'напиши еще раз или сбрось запрос &#128073 /reset',
                     'question': '&#128071    <b>Уточни локацию</b>',
                     'cities is False': '&#129302 Hе нашлось городов с похожим названием, напиши еще раз '
                                        'или сбрось запрос &#128073 /reset'
                     },
     'any_text.py': '&#129302 Такой команды я не знаю, чтобы узнать о моих возможностях &#128073 /help',
     'any_contents_but_text.py': {'audio, voice': '&#129302 К сожалению, уши мне ещё не приделали, я пока умею только '
                                                  'читать, чтобы узнать о моих возможностях &#128073 /help',
                                  'document': '&#129302 Опять эта ваша бюрократия, всё документы шлёте, пиши по-'
                                              'русски. Чтобы узнать о моих возможностях &#128073 /help',
                                  'video': '&#129302 Спасибо, посмотрю на досуге, а сейчас давай ближе к делу, чтобы '
                                           'узнать о моих возможностях &#128073 /help',
                                  'photo': '&#129302 Прикольно, фоточка, у меня их много, со всего света &#128515, '
                                           'чтобы узнать о моих возможностях &#128073 /help',
                                  'sticker': '&#129302 Ох уж эти стикеры, они везде, будем искать отели? Чтобы узнать '
                                             'о моих возможностях &#128073 /help',
                                  'location': '&#129302 Так вот ты где находишься, буду знать, чтобы узнать о'
                                              ' моих возможностях &#128073 /help',
                                  'contact': '&#129302 Записал, будем созваниваться по праздникам, чтобы узнать о '
                                             'моих возможностях &#128073 /help'
                                  },
     'get_ranges.py': {'negative range': '&#129302 Какой-то у тебя отрицательный диапазон получается напиши нормально',
                       'not hotels': ' не нашлось подходящих отелей',
                       'not numbers': '&#129302 Попробуй ещё раз, нужно ввести диапазон от и до, '
                                      'два числа через пробел',
                       'exception': 'Попробуй ещё раз, нужно ввести диапазон от и до, два числа через пробел, '
                                    'постарайся в этот раз без лишних разделителей'},
     'flood_control.py': {'too fast': '&#129302 Не так быстро, пожалуйста',
                          'lot flooding': '&#129302 У тебя видимо что-то с клавиатурой, давай продолжим через '},
     'state_and_user_control.py': '&#129302 Нужно завершить текущий запрос &#128073 /help Или сбросить &#128073 /reset',
     'state_control_only_command_handlers.py': '&#129302 Нужно завершить текущий запрос &#128073 /help '
                                               'Или сбросить &#128073 /reset',
     'ranges.py': {'range price': 'Введи диапазон цен за сутки проживания в рублях, через пробел',
                   'range distance': 'Введи диапазон расстояний расположения отелей от центра города в км, '
                                     'через пробел'},
     'search_result.py': 'Результат поиска:\n',
     'old keyboard': 'Клавиатура устарела'
     }
