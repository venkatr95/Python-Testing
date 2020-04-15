# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


# Fixture for Firefox
@pytest.fixture(params=["chrome", "firefox"] ,scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome('drivers/chromedriver.exe')
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=r'drivers/geckodriver.exe')
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.lambdatest.com/")
        print(self.driver.title)

        sleep(5)