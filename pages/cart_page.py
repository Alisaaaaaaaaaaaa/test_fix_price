from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    add_to_cart = "//button[@class='button in-cart']"
    go_to_cart = "//button[@class='button goto-cart']"

    # Getters

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click add to cart")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click go to cart")

    # Methods

    def product_confirmation(self):
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.click_add_to_cart()
            self.click_go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")

