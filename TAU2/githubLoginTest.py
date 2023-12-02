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

# Deklaracja zmiennych
INVALID_USERNAME = 'test@test.pl'
INVALID_PASSWORD = 'hasuo'

# Pobierz dane do logowania zmiennych środowiskowych
github_username = os.getenv('GITHUB_USERNAME')
github_password = os.getenv('GITHUB_PASSWORD')

if not (github_username and github_password):
    logger.error('Brak zdefiniowanych zmiennych środowiskowych GITHUB_USERNAME lub GITHUB_PASSWORD')
    exit()

# Test scenariusza dla GitHub w przeglądarce Firefox, jeśli Chrome nie jest dostępny
if 'driver' not in locals():
    logger.warning('Przeglądarka Chrome niedostępna. Próbuję uruchomić w przeglądarce Firefox.')
    try:
        driver = webdriver.Firefox()
    except Exception as e:
        logger.error(f'Nie udało się uruchomić przeglądarki Firefox. Błąd: {str(e)}')
        exit()

driver.get('https://github.com/')

logger.warning('Jakieś ostrzeżenie na GitHub')

# Zastosowanie oczekiwania na pojawienie się elementu "Sign up"
wait = WebDriverWait(driver, 10)
temp = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign up')))

temp.click()
logger.error('Jakiś Error na GitHub')

# Kliknij na "Sign in" używając klasy CSS
try:
    time.sleep(2)
    sign_in_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="/login"]')))
    sign_in_link.click()
    logger.info('Clicking on "Sign in" link')
except:
    logger.error('Could not find or click "Sign in" link')

# Poczekać krótko przed próbą znalezienia elementów logowania
time.sleep(2)

# Wprowadź nieprawidłowe dane do logowania
try:
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
    username_field.send_keys(INVALID_USERNAME)

    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_field.send_keys(INVALID_PASSWORD)

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
    login_button.click()

    # Sprawdź, czy pojawił się komunikat o błędzie
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.flash-error')))
    logger.error(f'Failed login attempt. Error message: {error_message.text}')
except Exception as e:
    logger.error(f'Error during login with incorrect credentials: {str(e)}')

# Poczekać krótko przed próbą znalezienia elementów logowania
time.sleep(2)

# Wprowadź poprawne dane do logowania
try:
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
    username_field.send_keys(github_username)

    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_field.send_keys(github_password)

    login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
    login_button.click()

    logger.info('Successfully logged in to GitHub')
except Exception as e:
    logger.error(f'Error while logging in: {str(e)}')

# Zamknij przeglądarkę
driver.quit()
