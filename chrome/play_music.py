import time
from selenium import webdriver  # pip install selenium


import conf


driver = webdriver.Chrome(
    executable_path=' '  # TODO: Прописать абсолютный путь к драйверу.
    # Драйвер chrome, скачать по ссылке: https://chromedriver.storage.googleapis.com/index.html.
    # Разархировать и положить в каталог .

)

try:
    driver.get(url='https://vk.com/')  # Получает и переходит по адресу.
    telephone_vk = driver.find_element_by_id('index_email')  # Получает элемент по id. (Input).
    telephone_vk.send_keys(conf.telephone_vk)  # Передает значение в элемент.
    time.sleep(2)  # Ожидание 2 секунды.
    password_vk = driver.find_element_by_id('index_pass')  # Получает элемент по id. (Input).
    password_vk.send_keys(conf.password_vk)  # Передает значение в элемент.
    time.sleep(2)  # Ожидание 2 секунды.
    login = driver.find_element_by_id('index_login_button')  # Получает элемент по id (Button).
    login.click()  # Имитирует нажатие по элементу.
    time.sleep(3)  # Ожидание 3 секунды.
    music = driver.find_element_by_id('l_aud')  # Получает элемент по id. (a link).
    music_link = music.find_element_by_class_name('left_row')  # Получает элемент по классу.
    music_link = str(music_link.get_attribute(
        'href')) + '?section=all'  # Получит значение атрибута href ссылки и  построит ссылку 'Моя музыка'.
    time.sleep(2)  # Ожидание 3 секунды.
    driver.get(url=music_link)  # Переходит по адресу.
    click_music = driver.find_element_by_class_name(
        'audio_row').click()  # Получает первый элмент по классу и имитирует нажатие.
    time.sleep(1800)  # Ожидание 30 минут.
except Exception as e:
    print(e)
finally:
    driver.close()  # Закрывает chrome.
    driver.quit()  # Завершает работу.
