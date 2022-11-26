import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class FavoritePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    favorite_button = "//*[@id='app-header']/div/div/header/div[5]/a[1]/span[2]"
    select_button = "//*[@id='gp5700472']/div[3]/button"

    # Getters

    def get_favorite_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.favorite_button)))

    def get_select_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button)))

    # Actions

    def click_favorite_button(self):
        self.get_favorite_button().click()
        print("Select favorite button")

    def click_select_button(self):
        self.get_select_button().click()
        print("Select button")

    # Methods

    def favorite(self):
        with allure.step("Favorite"):
            Logger.add_start_step(method="favorite")
            self.get_current_url()
            self.click_favorite_button()
            time.sleep(3)
            self.click_select_button()
            Logger.add_end_step(url=self.driver.current_url, method="favorite")
