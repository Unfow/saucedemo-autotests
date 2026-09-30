import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Старт браузера
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

try:
    # Переход на сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товара в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # 4. Заполнение формы покупателя
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("101000")
    driver.find_element(By.ID, "continue").click()

    # 5. Покупка товара (кнопка Finish)
    driver.find_element(By.ID, "finish").click()

    # Проверка завершения заказа в консоли
    complete_header = driver.find_element(By.CLASS_NAME, "complete-header")
    print(f"Сообщение на странице: {complete_header.text}")
    time.sleep(2)

finally:
    # 6. Закрытие браузера
    driver.quit()