import os

from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env\n'
         'Необходимо верно заполнить данные в файле .env.template и переименовать его в .env')
else:
    load_dotenv()

# Уникальный ключ телеграмм бота -> загружается из файла .env
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Уникальный ключ  для "hotels4.p.rapidapi.com" -> загружается из файла .env
RAPID_API_KEY = os.getenv('RAPID_API_KEY')

# Параметры HTML запросов к API Нotels
HOST = "hotels4.p.rapidapi.com"
HEADERS = {"X-RapidAPI-Host": HOST, "X-RapidAPI-Key": RAPID_API_KEY}
LANGUAGE = "ru_RU"
CURRENCY = "RUB"

URL = "https://" + HOST
URL_city = URL + "/locations/v2/search"
URL_hotels = URL + "/properties/list"
URL_hotel_photos = URL + "/properties/get-hotel-photos"

# URL API ЦБ РФ
URL_cbr = 'https://www.cbr-xml-daily.ru/daily_json.js'

# Параметр в секундах регулярности обновления курса USD при условии запроса от пользователя
RATE_UPDATE = 10800  # 3 часа

# Команды бота (также есть команда my_id в ответ возвращает id пользователя)
DEFAULT_COMMANDS = (('start', "запустить бота"),
                    ('help', "вывести справку"),
                    ('lowprice', "топ дешёвых отелей в городе"),
                    ('highprice', "топ дорогих отелей в городе"),
                    ('bestdeal', "топ дешёвых отелей ближе к центру"),
                    ('history', "история поиска отелей"),
                    ('reset', "сброс текущего запроса"),
                    )

# Относительный путь к базе данных
DATABASE_PATH = 'database/database.db'

# Относительный путь к файлу с логами
LOGFILE_PATH = 'logs/debug.log'

# Параметр уровня логирования
LOG_LEVEL = 'DEBUG'

# Формат логирования
LOG_FORMAT = '{time:DD-MM-YYYY at HH:mm:ss} | {level: <8} | file: {file: ^30} | ' \
             'func: {function: ^30} | line: {line: >3} | message: {message}'

# Cписок администраторов -> загружается из файла .env
ADMINS = os.getenv('ADMINS')

# Время в секундах между сообщениями от пользователя, для контроля и защиты от 'флуда'
ANTIFLOOD_TIME = 1.5

# Время, временного ограничения доступа пользователя в секундах
# (устанавливается приложением автоматически, если пользователь флудит)
LIMITED_TIME = 120

# Максимальное количество попыток перезапуска бота в случае если он "упал" после ошибки
MAX_RESTART_BOT = 5
