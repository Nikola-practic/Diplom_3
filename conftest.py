import pytest
# import requests
import urls
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(urls.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(urls.BASE_URL)

    yield driver
    driver.quit()



