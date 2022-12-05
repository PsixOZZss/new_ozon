import logging

import os
import shutil

import random

import time

from BAN import BAN_WORD, BAN_CHEMIST, BAN_SEED, BAN_VAPE, BAN_OTHER

# импорты для настройки драйвера
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# для поиска элементов и взаимодействия с ними
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

# для ожидания загрузки страницы или элементов
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.wait import WebDriverWait

# скорость чтения и проверки
# брал как 240 слов в минуту + столько же на проверку
SPEED = 0.5

# причины для отклонения
REASONS = {'taboo': "//*[contains(text(), 'Товар запрещен')]",
           }

# вкладки
PAGES = {'now': 'now',
         'attributes': "//*[type='button' and [contains(text(), 'Атрибуты')]]",
         'media': "//*[type='button' and [contains(text(), 'Медиа')]]",
         }

# позиция аттрибутов
POSITIONS = {'now': "contains(@class, 'focused')]",
             'commercial': "//*[contains(text(), 'Коммерческий тип')]",
             }

# аргументы для ожидания
WAIT_ARG = {'attributes': "//*[contains(@class, 'attribute')]",
            'box': "//*[contains(@class, 'mark')]",
            'page': "//*[contains(text(), 'Снять текущие задания')]",
            'none': 'none',
            }

# без комментариев
OTHER_PATH = {'accept': "//*[contains(@class, 'button') and contains(@class, 'green')]",
              'decline': "//*[contains(@class, 'button') and contains(@class, 'red')]",
              'accept_final': "//*[text()[contains(.,'Завершить проверку')] and contains(@class, 'button')]",
              'accept_box': "//*[text()[contains(.,'Подтвердить')] and contains(@class, 'button')]",
              'images': "",
              'stock': "//*[contains(text(), 'Ничего не выбрано')]",
              'key': "//*[contains(@class, 'focused')]/div/div[contains(@class,'label')]",
              'value': "//*[contains(@class, 'focused')]/div/div[contains(@class,'value')]/span",
              'descriptions': "",
              'categories': "//*[contains(text(), 'Группа товара')]/..",
              }

# настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
debug = logger.debug

# настройка драйвера
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chrome/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def get_categories():
    categories = getter(OTHER_PATH['categories']).split('\n')[1]
    debug('categories: '+categories)
    return categories


def get_info():
    key = getter(OTHER_PATH['key'])
    value = getter(OTHER_PATH['value'])
    # descriptions = getter(OTHER_PATH['descriptions'])
    descriptions = 'no_value'
    return key, value, descriptions


def getter(path):
    try:
        element = driver.find_element(By.XPATH, path).text.lower()
    except NoSuchElementException:
        element = 'no_value'
    return element


def set_box(page, position, reason, *wait_args):
    if page != 'now':
        click(page, wait_args[0])
    click(position, wait_args[1])
    decline()
    if not is_box_accept(reason):
        click(reason, WAIT_ARG['none'])
    click(OTHER_PATH, WAIT_ARG['none'])


def is_box_accept(path):
    return False


def check_value(value, categories):
    for word in value:
        if word in BAN_WORD:
            return False
    if 'аптека' in categories or 'бады' in categories:
        for word in value:
            if word in BAN_CHEMIST or word in BAN_SEED:
                return False
    elif 'вейпинг' in categories:
        for word in value:
            if word in BAN_VAPE:
                return False
    else:
        for word in value:
            if word in BAN_OTHER:
                return False
    return True


def check_images():
    time.sleep(3)
    accept()
    # clear_img()


# пока не надо
def download_images():
    pass


def clear_img():
    shutil.rmtree('./images/download')
    os.makedirs('./images/download')


def play_video():
    while True:
        try:
            pass
        except Exception as e:
            debug('video exception')
            debug(str(e))
        else:
            break


def is_final():
    try:
        driver.find_element(By.XPATH, OTHER_PATH['accept_final'])
    except NoSuchElementException:
        return False
    else:
        return True


def accept():
    click(OTHER_PATH['accept'], WAIT_ARG['none'])


def decline():
    click(OTHER_PATH['decline'], WAIT_ARG['none'])


def accept_final():
    click(OTHER_PATH['accept_final'], WAIT_ARG['none'])


def is_in_stock():
    try:
        driver.find_element(By.XPATH, OTHER_PATH['stock'])
    except NoSuchElementException:
        return True
    else:
        return False


def refresh():
    driver.refresh()
    wait_for(WAIT_ARG['page'])
    time.sleep(3)


def wait_for(argument):
    if argument != 'none':
        timeout = 20
        WebDriverWait(driver, timeout).until(condition.presence_of_element_located((By.XPATH, argument)))
    else:
        time.sleep(0.5)


def click(path, wait_arg):
    element = driver.find_element(By.XPATH, path)
    driver.execute_script("arguments[0].click();", element)
    wait_for(wait_arg)


def main():
    count = 0
    rand_count = int(random.random() * 200) + 1400
    while count < rand_count:
        if is_in_stock():
            categories = get_categories()
            while not is_final():
                key, value, descriptions = get_info()
                if 'Видео' in key:
                    play_video()
                elif 'Изображ' in key:
                    download_images()
                    check_images()
                else:
                    words_count = len(value.split())
                    time.sleep(SPEED * words_count)
                    if check_value(value, categories):
                        accept()
                    else:
                        accept()
                        set_box(PAGES['now'], POSITIONS['commercial'], REASONS['taboo'],
                                WAIT_ARG['attributes'],
                                WAIT_ARG['box'])
            accept_final()
            count += 1
        else:
            refresh()


if __name__ == '__main__':
    main()
