import os, time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # Полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматирование времени
        filesize = os.path.getsize(filepath)  # Размер файла
        parent_dir = os.path.dirname(filepath)  # Получение родительской директории файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')