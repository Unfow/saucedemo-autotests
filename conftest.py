import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Регистрация опций командной строки для запуска тестов."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера для запуска тестов: chrome, firefox, edge",
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/",
        help="Базовый адрес тестируемого веб-сайта",
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Фикстура для передачи базового URL в тесты."""
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    """Фикстура управления жизненным циклом браузера (мультибраузерность)."""
    browser_name = request.config.getoption("--browser").lower()
    driver = None

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError(
            f"Неподдерживаемый браузер: '{browser_name}'. "
            f"Допустимые варианты: chrome, firefox, edge."
        )

    driver.maximize_window()
    driver.implicitly_wait(10)

    # Передача объекта драйвера в тело теста
    yield driver

    # Завершение сессии браузера после выполнения теста
    driver.quit()