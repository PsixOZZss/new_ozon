import logging

import os
import shutil
import asyncio

import random

import time

from selenium.webdriver import ActionChains

from BAN import BAN_WORD, BAN_CHEMIST, BAN_SEED, BAN_VAPE, BAN_OTHER
from PATH import REASONS, PAGES, POSITIONS, WAIT_ARG, OTHER_PATH

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


class OzonManager(object):

    def __init__(self):
        self.driver = None
        self.message = None
        self.status = ''

        # настройка логов
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        self.debug = logger.debug

        # скорость чтения и проверки
        self.SPEED = 0.1

    def get_status(self):
        return self.status

    async def start(self, message, is_start_browser):
        if is_start_browser:
            self.message = message
            os.chdir('./')
            os.system('start browser.bat')
            time.sleep(5)
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "./chrome/chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        return await self.main()

    def screen(self):
        self.driver.get_screenshot_as_file('./screens/test.png')

    async def main(self):
        count = 0
        rand_count = int(random.random() * 200) + 1400
        try:
            while count < rand_count:
                if self.is_bot_check():
                    print(100 / 0)
                elif self.is_in_stock():
                    categories = self.get_categories()
                    while not self.is_final():
                        try:
                            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Пролистайте rich')]")
                            self.driver.execute_script("document.getElementsByClassName('rich_wScan')[0].scrollTo(0, document.getElementsByClassName('rich_wScan')[0].scrollHeight);")
                            self.accept()
                        except NoSuchElementException:
                            await asyncio.sleep(0.1)
                            key, value, descriptions = self.get_info()
                            if 'видео' in key:
                                self.status = 'video'
                                await self.play_video()
                            elif 'изображ' in key:
                                self.status = 'image'
                                self.download_images()
                                await self.check_images()
                            else:
                                self.status = 'text'
                                words_count = len(value.split())
                                await asyncio.sleep(self.SPEED * words_count + 0.7 + random.random() * 5)
                                if self.check_value(value, categories):
                                    self.accept()
                                else:
                                    self.accept()
                                    self.set_box(PAGES['now'], POSITIONS['commercial'], REASONS['taboo'],
                                                 WAIT_ARG['attributes'],
                                                 WAIT_ARG['box'])
                    self.accept_final()
                    count += 1
                else:
                    self.refresh()
        except Exception as e:
            return str(e)

    def get_categories(self):
        categories = self.getter(OTHER_PATH['categories']).split('\n')[1]
        return categories

    def get_info(self):
        key = self.getter(OTHER_PATH['key'])
        value = self.getter(OTHER_PATH['value'])
        descriptions = self.getter(OTHER_PATH['descriptions'])
        return key, value, descriptions

    def getter(self, path):
        try:
            element = self.driver.find_element(By.XPATH, path).text.lower()
        except NoSuchElementException:
            element = 'no_value'
        return element

    def set_box(self, page, position, reason, *wait_args):
        if page != 'now':
            self.click(page, wait_args[0])
        self.click(position, wait_args[1])
        self.decline()
        if not self.is_box_accept(reason):
            self.click(reason, WAIT_ARG['none'])
        self.click(OTHER_PATH, WAIT_ARG['none'])

    def is_box_accept(self, path):
        return False

    @staticmethod
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

    async def check_images(self):
        await asyncio.sleep(3)
        self.accept()
        # clear_img()

    # пока не надо
    def download_images(self):
        pass

    @staticmethod
    def clear_img():
        shutil.rmtree('./images/download')
        os.makedirs('./images/download')

    async def play_video(self):
        while True:
            try:
                # Bot.send_msg(self.message, 'Видео')
                await asyncio.sleep(2)
                element = self.driver.find_element(By.XPATH, OTHER_PATH['video'])
                self.driver.execute_script('arguments[0].play()', element)
                await asyncio.sleep(2)
                duration = self.driver.execute_script('return arguments[0].duration', element)
                await asyncio.sleep(duration+1)
                self.accept()
            except Exception as e:
                self.debug('video exception')
                self.debug(str(e))
            else:
                break

    async def video_click(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(100, 100).perform()
        await asyncio.sleep(5)
        actions.click().perform()

    def is_final(self):
        try:
            self.driver.find_element(By.XPATH, OTHER_PATH['accept_final'])
        except NoSuchElementException:
            return False
        else:
            return True

    def accept(self):
        try:
            self.click(OTHER_PATH['accept'], WAIT_ARG['none'])
        except NoSuchElementException:
            self.refresh()

    def decline(self):
        self.click(OTHER_PATH['decline'], WAIT_ARG['none'])

    def accept_final(self):
        self.click(OTHER_PATH['accept_final'], WAIT_ARG['none'])

    def is_in_stock(self):
        try:
            self.driver.find_element(By.XPATH, OTHER_PATH['stock'])
        except NoSuchElementException:
            return True
        else:
            return False

    def is_liquid(self):
        try:
            self.driver.find_element(By.XPATH, OTHER_PATH['liquid'])
        except NoSuchElementException:
            return True
        else:
            return False

    def is_bot_check(self):
        try:
            self.driver.find_element(By.XPATH, OTHER_PATH['bot_test'])
        except NoSuchElementException:
            return False
        else:
            return True

    def refresh(self):
        self.driver.refresh()
        self.wait_for(WAIT_ARG['page'])
        time.sleep(random.random() * 2 + 2)

    def wait_for(self, argument):
        if argument != 'none':
            timeout = 20
            try:
                WebDriverWait(self.driver, timeout).until(condition.presence_of_element_located((By.XPATH, argument)))
            except TimeoutException:
                self.refresh()
        else:
            time.sleep(0.5)

    def click(self, path, wait_arg):
        element = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_for(wait_arg)

    def close_browser(self):
        while True:
            try:
                self.driver.close()
                self.driver.quit()
            except Exception as e:
                self.debug('Browser close'+str(e))
                break
