from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class BaseClass:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)


    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def _find_many(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def _wait_until_element_is_clickable(self,locator):
        return self.wait.until((EC.element_to_be_clickable(locator)))

    def _click(self, locator):
        element = self._wait_until_element_is_clickable(locator)
        element.click()

    def _get_text(self, locator):
        element = self._find(locator)
        return element.text

    def _send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    
