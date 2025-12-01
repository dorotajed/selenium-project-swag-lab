import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from datetime import datetime
from pytest_html import extras


load_dotenv()
URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def url():
    return URL


@pytest.fixture(scope="session")
def standard_user():
    return USERNAME


@pytest.fixture(scope="session")
def password():
    return PASSWORD


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     help="Browser to run tests on: chrome or firefox")


@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="function")
def browser(browser_name):
    if browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def standard_user_login_to_products_page(browser, url, standard_user, password):
    LoginPage(browser).open_page(url)
    LoginPage(browser).attempt_login(standard_user,password)
    yield ProductsPage(browser)



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        if "browser" in item.fixturenames:
            browser = item.funcargs["browser"]
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"screenshots/{item.name}_{timestamp}.png"

            try:
                browser.save_screenshot(path)
                print(f"Screenshot saved: {path}")

                # Attach to HTML report
                if path:
                    pytest_html = item.config.pluginmanager.getplugin("html")
                    extra.append(pytest_html.extras.image(path))

            except Exception as e:
                print(f"Failed to save screenshot: {e}")

    report.extra = extra

