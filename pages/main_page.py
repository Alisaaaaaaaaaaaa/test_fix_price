import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    url = 'https://fix-price.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Покупка товаров самовывозом"""
    """Покупка салфеток"""
    for_home_category = "//*[@id='app-header']/div/div/div[3]/div/a[3]"
    cleaning_category = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/aside/li/ul/li[1]/a"
    price_199 = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/aside/div/div[2]/div[1]/div[9]/label"
    filtration = "//select[@class='select']"
    alphabet_filtr = "//option[@value='abc']"
    select_wipes = "//*[@id='cp5040257']/div[2]/div[1]/img"
    confirmation_button = "//button[@class='button choose-obtain']"
    """Покупка машинки"""
    toys_category = "//*[@id='app-header']/div/div/div[3]/div/a[7]"
    boys_toys = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/aside/li/ul/li[4]/a"
    price_299 = "//*[@for='price_30029900']"
    car = "//*[@id='cp5601379']/div[2]/div[1]/div/div/div[1]/div[1]/img"
    select_color_car = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/button[1]"
    """Покупка гирлянды"""
    new_year_category = "//*[@id='app-header']/div/div/div[3]/div/a[2]"
    garlands = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/aside/li/ul/li[9]/a"
    max_price_filtr = "//option[@value='max']"
    metallic_garland = "//*[@id='cp5312543']/div[2]/div[1]/div/div/div[1]/div[1]/img"

    """Покупка ручек из каталога, c добавлением в избранное, с доставкой"""
    catalog_button = "//*[@id='app-header']/div/div/header/a[2]/span"
    stationery = "//*[@id='app-header']/div/div/header/div[3]/div/div[1]/div/div[1]/div[3]/a/div"
    show_full_list_button = "//button[@class='toggle-list']"
    berlingo_brand = "//label[@for='brand_136']"
    set_of_pens = "//*[@id='cp5700486']/div[2]/div[1]/div/div/div[1]/div[1]/img"
    add_to_favorite = "//button[@class='favorites favorites']"

    """Покупка шампуня с доставкой"""
    beauty_category = "//*[@id='app-header']/div/div/div[3]/div/a[5]"
    hair_category = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/aside/li/ul/li[5]/a"
    next_list = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[2]/main/div[3]/div/a[2]"
    shampoo_dove = "//*[@id='cp3220458']/div[2]/div[1]/div/div/div[1]/div[1]/img"
    assert_word_shampoo_page = "//*[@id='__layout']/div/div/div[3]/div/div/div/div/div[1]/div[2]/h1"

    # Getters

    """Салфетки"""

    def get_for_home_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_home_category)))

    def get_cleaning_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cleaning_category)))

    def get_price_199(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_199)))

    def get_filtration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filtration)))

    def get_alphabet_filtr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.alphabet_filtr)))

    def get_select_wipes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_wipes)))

    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmation_button)))

    """Машинка"""

    def get_toys_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.toys_category)))

    def get_boys_toys(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.boys_toys)))

    def get_price_299(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_299)))

    def get_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.car)))

    def get_select_color_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_color_car)))

    """Гирлянда"""

    def get_new_year_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_year_category)))

    def get_garlands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.garlands)))

    def get_max_price_filtr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price_filtr)))

    def get_metallic_garland(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metallic_garland)))

    """Набор ручек"""

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_stationery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stationery)))

    def get_show_full_list_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_full_list_button)))

    def get_berlingo_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.berlingo_brand)))

    def get_set_of_pens(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.set_of_pens)))

    def get_add_to_favorite(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_favorite)))

    """Шампунь"""

    def get_beauty_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.beauty_category)))

    def get_hair_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hair_category)))

    def get_next_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_list)))

    def get_shampoo_dove(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shampoo_dove)))

    def get_assert_word_shampoo_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.assert_word_shampoo_page)))

    # Actions

    """Салфетки"""

    def click_for_home_category(self):
        self.get_for_home_category().click()
        print("Select for home category")

    def click_cleaning_category(self):
        self.get_cleaning_category().click()
        print("Select Cleaning Category")

    def click_price_199(self):
        self.get_price_199().click()
        print("Select price 199")

    def click_filtration(self):
        self.get_filtration().click()
        print("Select filtration")

    def click_alphabet_filtr(self):
        self.get_alphabet_filtr().click()
        print("Alphabet filtration")

    def click_select_wipes(self):
        self.get_select_wipes().click()
        print("Select Wipes")

    def click_confirmation_button(self):
        self.get_confirmation_button().click()
        print("Confirmation button")

    """Машинка"""

    def click_toys_category(self):
        self.get_toys_category().click()
        print("Select toys category")

    def click_boys_toys(self):
        self.get_boys_toys().click()
        print("Select boys toys")

    def click_price_299(self):
        self.get_price_299().click()
        print("Select price 79")

    def click_car(self):
        self.get_car().click()
        print("Select car")

    def click_select_color_car(self):
        self.get_select_color_car().click()
        print("Select color car")

    """Гирлянда"""

    def click_new_year_category(self):
        self.get_new_year_category().click()
        print("Select new year category")

    def click_garlands(self):
        self.get_garlands().click()
        print("Select garlands")

    def click_max_price_filtr(self):
        self.get_max_price_filtr().click()
        print("Select max price filtration")

    def click_metallic_garland(self):
        self.get_metallic_garland().click()
        print("Select metallic garland")

    """Набор ручек"""

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Select catalog button")

    def click_stationery(self):
        self.get_stationery().click()
        print("Select stationery")

    def click_show_full_list_button(self):
        self.get_show_full_list_button().click()
        print("Select show full list button")

    def click_berlingo_brand(self):
        self.get_berlingo_brand().click()
        print("Select berlingo brand")

    def click_set_of_pens(self):
        self.get_set_of_pens().click()
        print("Select set of pens")

    def click_add_to_favorite(self):
        self.get_add_to_favorite().click()
        print("Added to favorite")

    """Шампунь"""

    def click_beauty_category(self):
        self.get_beauty_category().click()
        print("Select beauty category")

    def click_hair_category(self):
        self.get_hair_category().click()
        print("Select hair category")

    def click_next_list(self):
        self.get_next_list().click()
        print("Select next list")

    def click_shampoo_dove(self):
        self.get_shampoo_dove().click()
        print("Select shampoo Dove")

    # Methods

    def buy_c_wipes(self):
        with allure.step("Buy Wipes"):
            Logger.add_start_step(method="buy_c_wipes")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_for_home_category()
            self.click_cleaning_category()
            time.sleep(2)
            self.click_price_199()
            self.click_filtration()
            self.click_alphabet_filtr()
            time.sleep(2)
            self.click_select_wipes()
            self.get_screenshot()
            time.sleep(2)
            self.assert_url(
                'https://fix-price.com/catalog/dlya-doma/p-5040257-salfetki-universalnye-onome-25h21-sm-120-sht')
            self.click_confirmation_button()
            Logger.add_end_step(url=self.driver.current_url, method="buy_c_wipes")

    def buy_car(self):
        with allure.step("Buy Car"):
            Logger.add_start_step(method="buy_car")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_toys_category()
            self.click_boys_toys()
            time.sleep(3)
            self.click_price_299()
            self.click_car()
            self.get_screenshot()
            self.click_confirmation_button()
            Logger.add_end_step(url=self.driver.current_url, method="buy_car")

    def buy_garland(self):
        with allure.step("Buy Garland"):
            Logger.add_start_step(method="buy_garland")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_new_year_category()
            self.click_garlands()
            time.sleep(2)
            self.click_filtration()
            self.click_max_price_filtr()
            time.sleep(2)
            self.click_metallic_garland()
            self.get_screenshot()
            time.sleep(2)
            self.assert_url(
                'https://fix-price.com/catalog/vse-dlya-novogo-goda/p-5312543-girlyanda-novogodnyaya-metallik-snejnoe-krujevo-2-m-v-assortimente')
            self.click_confirmation_button()
            Logger.add_end_step(url=self.driver.current_url, method="buy_garland")

    def buy_pens(self):
        with allure.step("Buy Pens"):
            Logger.add_start_step(method="buy_pens")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_catalog_button()
            self.click_stationery()
            self.click_show_full_list_button()
            self.click_berlingo_brand()
            time.sleep(3)
            self.click_set_of_pens()
            self.get_screenshot()
            self.click_add_to_favorite()
            self.assert_url(
                'https://fix-price.com/catalog/kantstovary/p-5700486-nabor-gelevyh-ruchek-erlingo-6-sht-v-assortimente')
            Logger.add_end_step(url=self.driver.current_url, method="buy_pens")

    def buy_shampoo(self):
        with allure.step("Buy Shampoo"):
            Logger.add_start_step(method="buy_shampoo")
            self.get_current_url()
            self.click_beauty_category()
            self.click_hair_category()
            time.sleep(3)
            # self.driver.execute_script("window.scrollTo(0, 200)")
            # self.click_next_list()
            self.click_shampoo_dove()
            self.assert_word(self.get_assert_word_shampoo_page(), "Шампунь, Dove, 250 мл")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="buy_shampoo")
