import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.client_information_page import Client_information_page
from pages.favorite_page import FavoritePage
from pages.main_page import MainPage

"""Покупка с вводом адреса доставки и добавлением в корзину"""

@allure.description("Test buy shampoo with delivery")
def test_buy_product_with_delivery(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='E:\\pythonProject\\resource\\chromedriver.exe', chrome_options=options)

    cip = Client_information_page(driver)
    cip.input_address()
    print("Clients address is added")
    mp = MainPage(driver)
    mp.buy_shampoo()
    cp = CartPage(driver)
    cp.product_confirmation()
    print("Shampoo in cart")


"""Добавление товара в избранное"""

@allure.description("Test put product to favorite")
def test_put_product_to_favorite(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='E:\\pythonProject\\resource\\chromedriver.exe', chrome_options=options)

    mp = MainPage(driver)
    mp.buy_pens()
    print("Pens added to favorite")


"""Покупка товаров самовывозом, с выбором магазина"""

@allure.description("Test buy products in shop")
def test_buy_products_in_shop(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='E:\\pythonProject\\resource\\chromedriver.exe', chrome_options=options)

    """Покупка салфеток"""
    mp = MainPage(driver)
    mp.buy_c_wipes()
    cip = Client_information_page(driver)
    cip.shop_address()
    print("Purchase Wipes Good")

    """Покупка машинки"""
    mp = MainPage(driver)
    mp.buy_car()
    cip = Client_information_page(driver)
    cip.shop_address()
    print("Purchase Car Good")

    """Покупка гирлянды"""
    mp = MainPage(driver)
    mp.buy_garland()
    cip = Client_information_page(driver)
    cip.shop_address()
    print("Purchase Garland Good")
