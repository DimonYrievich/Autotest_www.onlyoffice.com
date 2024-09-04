Используя Webdriver - https://github.com/SeleniumHQ/selenium/wiki/Ruby-Bindings
написать скрипт, который будет осуществлять указанные ниже действия:

1. Запуск браузера Mozilla Firefox
2. Открытие страницы www.onlyoffice.com
3. Переход по ссылке в шапке About -> Contacts
4. Распарсит данные об офисах на странице и составить csv файл формата

        Country;CompanyName;FullAddress
        U.S.A.;Ascensio Systems Inc; 13355 Noel Rd Suite 1100Dallas, TX, USA75240 Phone: +1(972) 301-8440
        Latvia;Ascensio Systems SIA; 20A-6 Ernesta Birznieka-Upish street,Riga, Latvia,
        EU,LV-1050Phone: +371 63399867
        ...

Скрипт должен корректно работать в случаях если количество офисов на странице увеличится\уменьшится
Входные данные: путь к выходному файлу
Выходные данные: csv файл с данными об офисах
Бонусное задание: Написать приемочные тесты с проверкой работы программы
Бонусное задание со звездочкой: Используя GitHub Actions добавить автозапуск приемочных тестов на каждом Pull Requests
