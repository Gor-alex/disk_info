# disk_info
Disk info -  скрипт, который при запуске из командной строки без параметров выводит список жестких дисков с их размерами,
присутствующих в системе. Скрипт написан для Python 2.
Пример:

    python2 main.py

При запуске с ключём "-d" и одним числовым параметром скрипт выводит список партиций с их размерами,
содержащихся на диске с указанным номером. При попытке вывести диск с большим номером,
чем есть в системе, будет выведена соответствующая ошибка.
Пример:


    python2 main.py -d 0 # Скрипт выведет все партиции на диске 0

Указанный функционал реализован через класс-абстракцию и конкретные имплементации для ОС Windows + Linux.
Дополнительные библиотеки, необходимые для запуска на той или иной системе лежат в в виде файлов "dependecies.txt"

**Примечания :** Если вы испытываете проблемы при установке pyparted и у вас Debian, то данная библиотека,
есть в репозитории ("python-parted"). Если скрипт не выводит никакой информации, то необходимо запустить его с
привилегиями администратора системы. (Использовать пользователя root или приложение sudo)