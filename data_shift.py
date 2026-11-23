from datetime import datetime, timedelta

# 1. Исходная строка даты/времени
# date_string = "2025:04:30 08:02:17"
date_string = "2025:04:30 08:35:58"

# 2. Определяем формат исходной строки для парсинга
# %Y - год (4 цифры)
# %m - месяц (01-12)
# %d - день (01-31)
# %H - час (00-23)
# %M - минута (00-59)
# %S - секунда (00-59)
date_format = "%Y:%m:%d %H:%M:%S"

# 3. Преобразуем строку в объект datetime
try:
    dt_object = datetime.strptime(date_string, date_format)
    print(f"Исходная дата/время (объект datetime): {dt_object}")
except ValueError as e:
    print(f"Ошибка при парсинге даты: {e}")
    print("Убедитесь, что формат строки '%Y:%m:%d %H:%M:%S' соответствует вашей дате.")
    exit()

# 4. Определяем количество секунд, которое нужно прибавить
seconds_to_add = 86569  # Например, 150 секунд (это 2 минуты 30 секунд)

# 5. Создаем объект timedelta
time_delta = timedelta(seconds=seconds_to_add)
print(f"Добавляем {seconds_to_add} секунд.")

# 6. Прибавляем timedelta к объекту datetime
new_dt_object = dt_object + time_delta
print(f"Новая дата/время (объект datetime): {new_dt_object}")

# 7. (Опционально) Преобразуем новый объект datetime обратно в строку
# Используем тот же формат, что и для парсинга, или любой другой нужный формат.
new_date_string = new_dt_object.strftime(date_format)
print(f"Новая дата/время (строка в исходном формате): {new_date_string}")

# Пример с другим количеством секунд
seconds_to_add_2 = 3600  # 1 час
time_delta_2 = timedelta(seconds=seconds_to_add_2)
new_dt_object_2 = dt_object + time_delta_2
print(f"\nЕсли добавить {seconds_to_add_2} секунд: {new_dt_object_2.strftime(date_format)}")
