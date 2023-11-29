import requests
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import imaplib
import json
import time
import sys
import os
import numpy as np
import smtplib
# инициализация colorama
print("Успешная проверка библиотек.")
init()
python = sys.executable
while True:
    # выбор
    print(Fore.BLUE + "Меню:")
    print(Fore.YELLOW + "1. Показать статус страницы")
    print(Fore.GREEN + "2. Парсинг")
    print(Fore.CYAN + "3. [HTML] Быстрый просмотр коды страницы [TEST]")
    print(Fore.GREEN + "4. GithubAPI Парсинг")
    print(Fore.CYAN + "5. Рассылка(gmail) " + Fore.RED + "{НУЖЕН ПАРОЛЬ ПРИЛОЖЕНИЯ}")
    print(Fore.RED + "6. Выйти")
    print(Style.RESET_ALL)
    

    choice = input("Выберите пункт меню (1-5): ")

    if choice == "1":
        url = input("Введите URL: ")
        print("Операция может долго выполняться")
        if url:
            if not url.startswith('http'):
                url = 'https://' + url
            if not url.endswith(('com', 'ru', 'pro', 'net', 'рус')):
                url = url + '.com'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(Fore.GREEN + "Сайт работает")
                else:
                    print(Fore.RED + f"Сайт недоступен. Код ошибки: {response.status_code}")
            except Exception:
                print(Fore.RED + "Невозможно получить доступ к сайту")
        else:
            print(Fore.RED + "URL не может быть пустым")
        back = input("Введите 'назад', чтобы вернуться в предыдущее меню: ")
        if back == 'назад':
            continue


    elif choice == "2":
        url = input("Введите URL: ")
        print("Операция может долго выполняться")

        # проверяем URL и получаем HTML-страницу
        if url:
            if not url.startswith('http'):
                url = 'https://' + url
            if not url.endswith(('com', 'ru', 'pro', 'net', 'рус')):
                url = url + '.com'

        try:
            #проверка работает ли сайт?
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + "Сайт работает")
                soup = BeautifulSoup(response.text, 'html.parser')

                # получаем название страницы (title)
                title = soup.title.string
                print(Fore.YELLOW + f"Название страницы: {title}")

                # получаем все изображения на сайте
                images = soup.find_all('img')
                print(Fore.YELLOW + f"Количество изображений на сайте: {len(images)}")

                # подсчет эмодзи на странице
                emojis = soup.select('span.emoji')
                num_emojis = len(emojis)
                print(f'Количество эмодзи на странице: {num_emojis}')

                # получаем все текстовые данные на сайте и считаем количество символов
                text = soup.get_text().strip()
                chars = len(text)
                print(Fore.YELLOW + f"Количество символов на сайте: {chars}")
                #коливество тегов p
                count_p = len(soup.find_all('p'))
                print('Количество тегов "p":', count_p)
                #количество тегов h1
                # поиск количества тегов 'h'
                count_h1 = len(soup.find_all('h1'))
                print('Количество тегов "h1":', count_h1)
                # h2
                count_h2 = len(soup.find_all('h2'))
                print('Количество тегов "h2":', count_h2)
                #h3
                count_h3 = len(soup.find_all('h3'))
                print('Количество тегов "h3":', count_h3)
                #h4
                count_h4 = len(soup.find_all('h4'))
                print('Количество тегов "h4":', count_h4)
                #h5
                count_h5= len(soup.find_all('h5'))
                print('Количество тегов "h5":', count_h5)

                count_h6= len(soup.find_all('h6'))
                print('Количество тегов "h6":', count_h6)

                #a

                count_a= len(soup.find_all('a'))
                print('Количество тегов "a":', count_a)

                #wbr
                count_wbr= len(soup.find_all('wbr'))
                print('Количество тегов "wbr":', count_wbr)
                #video

                count_video = len(soup.find_all('video'))
                print('Количество тегов "video":', count_video)       

                count_var= len(soup.find_all('var'))
                print('Количество тегов "var":', count_var)

                #ul
                count_ul= len(soup.find_all('ul'))
                print('Количество тегов "ul":', count_ul)
                #u
                count_u= len(soup.find_all('u'))
                print('Количество тегов "u":', count_u)
                #track
                count_track= len(soup.find_all('track'))
                print('Количество тегов "track":', count_track)
                #tr
                count_tr= len(soup.find_all('tr'))
                print('Количество тегов "tr":', count_tr)
        

    






                # получаем все теги div на странице и выводим их количество
                divs = soup.find_all('div')
                print(Fore.YELLOW + f"Количество тегов div на странице: {len(divs)}")



                   # парсим количество скриптов на странице
                script_tags = soup.find_all("script")
                print(f"Количество скриптов на странице: {len(script_tags)}")

#класс
                    # находим все элементы с классами
                classes = soup.find_all(class_=True)
                    #выводим количество элементов с классами
                print(f'Количество классов: {len(classes)}')
                
                


                

            else:
                print(Fore.RED + f"Сайт недоступен. Код ошибки: {response.status_code}")
        except requests.exceptions.RequestException:
            print(Fore.RED + "Ошибка при обращении к сайту")
        back = input("Введите 'назад', чтобы вернуться в предыдущее меню: ")
        if back == 'назад':
            continue

#это не рабочая херня
    elif choice == "3":
        url = input("Введите адрес страницы: ")
        if not url.startswith('http'):
            url = 'https://' + url
        response = requests.get(url)
        print(response.status_code,'status_code')
        if 200 == 200:
            print(response.text,'text')

        else:
            print("Произошла непредвидимая ошибка.")
        back = input("Введите 'назад', чтобы вернуться в предыдущее меню: ")
        if back == 'назад':
            continue

               



    elif choice == "4":
        if choice == "4":
            username = input("Введите ваш username: ")
        try:
            response = requests.get(f"https://api.github.com/users/{username}/repos")
            if not response:
                print(Fore.RED + "Неверный username, попробуйте еще раз.")
                continue
            data = json.loads(response.text)
            for item in data:
                print("Ник: ", item["name"])
                print("Описание: ", item["description"])
                print("Язык: ", item["language"])
                print("Звезд: ", item["stargazers_count"])
            print(Fore.RED + "Если нечего не вывелось - проверьте юзернейм")
            back = input(Fore.GREEN + "Введите 'назад', чтобы вернуться в предыдущее меню: ").lower() == 'назад'
            continue
        except requests.exceptions.RequestException:
            print(Fore.RED + "Ошибка при обращении к API Github. Проверьте правильность написания username и наличие интернет-соединения.")
        if back == 'назад':
            continue



    elif choice == "5":
# Введите адрес электронной почты отправителя и получателя, а также пароль отправителя
# Открытие файла с данными
# Открытие файла с данными
        t = input("Введите текстовый документ(.txt)в формате: sender_email:sender_password:receiver_email (sender_email должен только быть 1: ")
        with open(f'{t}', 'r') as f:
            data = f.read().strip().split('\n')

# Цикл по каждой строке в файле
        for i in range(len(data)):
            sender_email, sender_password, receiver_email = data[i].split(':')
    
    # Попытка установления соединения с сервером почты
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)

            # Текст сообщения
                    message = input("введите сообщение: ")

            # Отправка сообщения получателям
                    for j in range(i+1, len(data)):
                        current_receiver = data[j].split(':')[2]
                        try:
                            server.sendmail(sender_email, current_receiver, message)
                            print(f'Письмо на: {current_receiver} с {sender_email} отправлено успешно')
                        except Exception as e:
                            print(f'Не удалось отправить письмо на: {current_receiver} с {sender_email}: {e}')

    # Обработка ошибки входа на почтовый ящик отправителя
            except smtplib.SMTPAuthenticationError as e:
                print(f'Не удалось отправить письмо на: {receiver_email} с {sender_email}: {e}')
                continue

        print('Рассылка завершена')
            



    






    elif choice == "6":
        print("Выход из программы")
    break

else:
    print("Некорректный выбор")





