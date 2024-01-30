# W pliku environment.py

from selenium import webdriver
from behave import fixture, use_fixture
import logging

# Inicjalizacja logera
logger = logging.getLogger('web_testing')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

@fixture
def browser_chrome(context):
    # Ustaw ścieżkę do sterownika Chrome na pulpit
    chrome_driver_path = r'C:\Users\m.pretki\Desktop\chromedriver.exe'
    context.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    context.logger = logger
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chrome, context)
    context.logger = logger
