from selenium.webdriver.common.by import By


def test_saucedemo_successful_purchase(browser, base_url):
    # 1. Открытие страницы по полученному из фикстуры адресу
    browser.get(base_url)

    # 2. Авторизация под standard_user
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавление товара Sauce Labs Backpack в корзину
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 4. Переход в корзину и клик по кнопке Checkout
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()

    # 5. Заполнение контактных данных
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("101000")
    browser.find_element(By.ID, "continue").click()

    # 6. Завершение оформления заказа
    browser.find_element(By.ID, "finish").click()

    # 7. Проверка успешного завершения покупки
    complete_header = browser.find_element(By.CLASS_NAME, "complete-header")
    assert complete_header.text == "Thank you for your order!", (
        f"Ожидался текст 'Thank you for your order!', но был получен: '{complete_header.text}'"
    )