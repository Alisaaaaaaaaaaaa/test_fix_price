from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Client_information_page(Base):
    url = 'https://fix-price.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Выбор адрес магазина для самовывоза"""
    select_address_shop = "//*[@id='modal']/div/div/div[3]/div/div[2]"
    confirmation_button = "//button[@class='button save button']"

    """Ввод адреса для доставки"""
    select_address_for_delivery = "//*[@id='app-header']/div/div/div[2]/div[1]/div[2]/div"
    enter_address = "//*[@id='modal']/div/div/div[1]/div[2]/div[2]"
    city_street = "//*[@id='modal']/div/div/div/div[2]/div/div[1]/div/div/input"
    confirm_city_street = "//*[@id='modal']/div/div/div/div[2]/div/div[2]/li/div[1]"
    building = "//*[@id='modal']/div/div/div/div[3]/div/div[1]/div/div/input"
    confirm_building = "//*[@id='modal']/div/div/div/div[3]/div/div[2]/li/div"
    entrance = "//*[@id='modal']/div/div/div/div[4]/div[1]/div/input"
    floor = "//*[@id='modal']/div/div/div/div[4]/div[2]/div/input"
    appartement = "//*[@id='modal']/div/div/div/div[4]/div[3]/div/input"
    save_button = "//button[@class='button save']"

    # Getters

    def get_select_address_shop(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_address_shop)))

    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirmation_button)))

    def get_select_address_for_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_address_for_delivery)))

    def get_enter_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.enter_address)))

    def get_city_street(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.city_street)))

    def get_confirm_city_street(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_city_street)))

    def get_building(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.building)))

    def get_confirm_building(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_building)))

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_floor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_appartement(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.appartement)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_button)))

    # Actions

    def click_select_address_shop(self):
        self.get_select_address_shop().click()
        print("Click address shop")

    def click_confirmation_button(self):
        self.get_confirmation_button().click()
        print("Click confirmation button")

    def click_select_address_for_delivery(self):
        self.get_select_address_for_delivery().click()
        print("Click select address for delivery")

    def click_enter_address(self):
        self.get_enter_address().click()
        print("Click enter address")

    def input_city_street(self, city_and_street):
        self.get_city_street().send_keys(city_and_street)
        print("Input City and Street")

    def click_confirm_city_street(self):
        self.get_confirm_city_street().click()
        print("Confirm city street")

    def input_building(self, building):
        self.get_building().send_keys(building)
        print("Input building")

    def click_confirm_building(self):
        self.get_confirm_building().click()
        print("Confirm building")

    def input_entrance(self, entrance):
        self.get_entrance().send_keys(entrance)
        print("Input entrance")

    def input_floor(self, floor):
        self.get_floor().send_keys(floor)
        print("Input floor")

    def input_appartement(self, appartement):
        self.get_appartement().send_keys(appartement)
        print("Input appartement")

    def click_save_button(self):
        self.get_save_button().click()
        print("Click save button")

    # Methods

    def shop_address(self):
        with allure.step("Shop address"):
            Logger.add_start_step(method="shop_address")
            self.get_current_url()
            self.click_select_address_shop()
            self.click_confirmation_button()
            Logger.add_end_step(url=self.driver.current_url, method="shop_address")

    def input_address(self):
        with allure.step("Input address"):
            Logger.add_start_step(method="input_address")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_select_address_for_delivery()
            self.click_enter_address()
            self.click_confirmation_button()
            self.input_city_street("г. Москва, ул. Зименковская (п Сосенское)")
            self.click_confirm_city_street()
            self.input_building("30")
            self.click_confirm_building()
            self.input_entrance("2")
            self.input_floor("3")
            self.input_appartement("9")
            self.click_save_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_address")

