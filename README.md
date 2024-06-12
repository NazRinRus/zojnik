Развернуть локальный сервер

1. Загрузить архив проека по ссылке: https://github.com/NazRinRus/zojnik/archive/refs/heads/dev_rinat.zip;
2. Извлечь архив в папку zojnik;
3. В терминалей перейти в папку zojnik;
4. Установить pithon в linux:
   sudo apt-get install python3
   В Windows скачать установочный файл на сайте https://www.python.org/
5. Создать виртуальное окружение: python3 -m venv venv_zojnik;
6. Активировать виртуальное окружение:
   Linux: source venv_zojnik/bin/activate
   Windows: venv_zojnik\scripts\activate
7. Установить пакеты и связи из файла zojnik/requirements.txt: pip install -r requirements.txt;
8. Перейти в папку с файлом manage.py (zojnik/manage.py);
9. Создать суперюзер: python3 manage.py createsuperuser (в Windows команды python пишутся без версии 3: python manage.py createsuperuser);
10. Создать миграции: python3 manage.py makemigrations;
11. Провести миграции: python3 manage.py migrate;
12. Запустить сервер: python3 manage.py runserver; 
