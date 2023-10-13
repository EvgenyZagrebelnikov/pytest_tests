from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"



def test_adding_a_product_to_the_cart_through_the_catalog():
    add_to_card_fild = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_card_fild.click()

    text_before = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']").text
    # text_before = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link']>div[class='inventory_item_name']").text
    # text_before = driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]").text

    shopping_cart_container = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']")
    shopping_cart_container.click()

    text_after = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']").text
    # text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']>div[class='inventory_item_name']").text
    # text_after = driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]").text

    assert text_before == text_after

    driver.quit()
