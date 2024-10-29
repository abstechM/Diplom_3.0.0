import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    yield browser

    browser.quit()


"""@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()"""

