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
from selenium.common.exceptions import TimeoutException

# скорость чтения и проверки
SPEED = 0.1

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
              'video': "//video[@playsinline]",
              'stock': "//*[contains(text(), 'Ничего не выбрано')]",
              'liquid': "//*[contains(text(), 'Error)]",
              'key': "//*[contains(@class, 'focused')]/div/div[contains(@class,'label')]",
              'value': "//*[contains(@class, 'focused')]/div/div[contains(@class,'value')]/span",
              'descriptions': "//*[contains(@class, 'focused')]/../../div/div/div/"
                              "div[text()[contains(.,'Предыдущий модератор отклонил атрибут')]]/../div/span",
              'categories': "//*[contains(text(), 'Группа товара')]/..",
              'bot_test': "//*[text()[contains(.,'Checking if the site connection is secure')]]"
              }

# настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
debug = logger.debug


def get_categories():
    categories = getter(OTHER_PATH['categories']).split('\n')[1]
    return categories


def get_info():
    key = getter(OTHER_PATH['key'])
    value = getter(OTHER_PATH['value'])
    descriptions = getter(OTHER_PATH['descriptions'])
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
    try:
        time.sleep(2)
        element = driver.find_element(By.XPATH, OTHER_PATH['video'])
        driver.execute_script('arguments[0].play()', element)
        time.sleep(2)
        duration = driver.execute_script('return arguments[0].duration', element)
        time.sleep(duration)
        accept()
    except NoSuchElementException as e:
        debug('video exception')
        debug(str(e))


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


def is_liquid():
    try:
        driver.find_element(By.XPATH, OTHER_PATH['liquid'])
    except NoSuchElementException:
        return True
    else:
        return False


def is_bot_check():
    try:
        driver.find_element(By.XPATH, OTHER_PATH['bot_test'])
    except NoSuchElementException:
        return False
    else:
        return True


def refresh():
    driver.refresh()
    wait_for(WAIT_ARG['page'])
    time.sleep(random.random() * 2 + 2)


def wait_for(argument):
    if argument != 'none':
        timeout = 20
        try:
            WebDriverWait(driver, timeout).until(condition.presence_of_element_located((By.XPATH, argument)))
        except TimeoutException:
            refresh()
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
        if is_bot_check():
            print(100 / 0)
        elif is_in_stock():
            categories = get_categories()
            while not is_final():
                key, value, descriptions = get_info()
                if 'видео' in key:
                    play_video()
                elif 'изображ' in key:
                    download_images()
                    check_images()
                else:
                    words_count = len(value.split())
                    time.sleep(SPEED * words_count + 0.7 + random.random() * 5)
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


def open_browser():
    os.chdir('./')
    os.system('start browser.bat')
    time.sleep(5)
    setup_browser()


def setup_browser():
    global driver
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "./chrome/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def close_browser():
    while True:
        try:
            setup_browser()
            driver.close()
            driver.quit()
        except Exception:
            break


def starting_bot():
    try:
        open_browser()
        main()
    except Exception as e:
        driver.get_screenshot_as_file('./screens/test.png')
        close_browser()
        return str(e)

if __name__ == '__main__':
    open_browser()
    main()
