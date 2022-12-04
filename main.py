import os
import shutil
import random
import logging

from BAN import BAN_WORD, BAN_CHEMIST, BAN_SEED, BAN_VAPE, BAN_OTHER

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.wait import WebDriverWait

REASONS = {'taboo': '',
           }

PAGES = {'now': '',
         'attributes': '',
         }

POSITIONS = {'now': '',
             'categories': '',
             'commercial': '',
             }

WAIT_ARG = {'attributes': '',
            'box': '',
            'page': '',
            'none': 'none',
            }

OTHER_PATH = {'final': "//*[text()[contains(.,'Завершить проверку')] and contains(@class, 'button')]",
              'accept': "",
              'decline': "",
              'accept_final': "",
              'images': "",
              'stock': "//*[contains(text(), 'не найден')]"
              }

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chrome/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


def get_categories():
    categories = 'no_categories'
    try:
        categories = driver.find_element(By.XPATH, POSITIONS['categories']).text
    except NoSuchElementException:
        pass
    return categories


def get_info():
    key = value = images = descriptions = 'no_value'
    return key.lower(), value, images, descriptions


def set_box(page, position, reason, *wait_args):
    click(page, wait_args[0])
    click(position, wait_args[1])
    if not is_box_accept(reason):
        click(reason, WAIT_ARG['none'])
    accept()


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
            logger.debug('video exception')
            logger.debug(str(e))
        else:
            break


def is_final():
    try:
        driver.find_element(By.XPATH, OTHER_PATH['final'])
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


def wait_for(argument):
    timeout = 20
    WebDriverWait(driver, timeout).until(condition.presence_of_element_located((By.XPATH, argument)))


def click(path, wait_arg):
    element = driver.find_element(By.XPATH, path)
    driver.execute_script("arguments[0].click();", element)
    if wait_arg != 'none':
        wait_for(wait_arg)


def main():
    count = 0
    rand_count = int(random.random() * 200) + 1400
    while count < rand_count:
        if is_in_stock():
            categories = get_categories()
            while not is_final():
                key, value, images, descriptions = get_info()
                if 'видео' in key:
                    play_video()
                elif '' in key:
                    download_images()
                    check_images()
                else:
                    if check_value(value, categories):
                        accept()
                    else:
                        decline()
                        set_box(PAGES['attributes'], POSITIONS['commercial'], REASONS['taboo'],
                                WAIT_ARG['attributes'],
                                WAIT_ARG['box'])
            accept_final()
            count += 1
        else:
            refresh()


if __name__ == '__main__':
    main()
