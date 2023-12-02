import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger('web_testing')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Test scenariusza dla Wikipedii w przeglądarce Firefox, jeśli Chrome nie jest dostępny
if 'driver' not in locals():
    logger.warning('Przeglądarka Chrome niedostępna. Próbuję uruchomić w przeglądarce Firefox.')
    try:
        driver = webdriver.Firefox()
    except Exception as e:
        logger.error(f'Nie udało się uruchomić przeglądarki Firefox. Błąd: {str(e)}')
        exit()

# Otwórz przeglądarkę w trybie pełnoekranowym
driver.maximize_window()

driver.get('https://pl.wikipedia.org/')

# Oczekiwanie na pole wyszukiwania
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'cdx-text-input__input')))

# Aktualizacja elementu przed użyciem
search_box = driver.find_element(By.CLASS_NAME, 'cdx-text-input__input')
search_box.send_keys('Python')

# Kliknij przycisk "Szukaj"
search_button = driver.find_element(By.CLASS_NAME, 'cdx-search-input__end-button')
search_button.click()

time.sleep(2)

logger.info(f'Aktualny URL strony Wikipedia: {driver.current_url}')

# Zamknij przeglądarkę dla Wikipedii
driver.quit()
