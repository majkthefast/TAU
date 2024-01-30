from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import os
import time

INVALID_USERNAME = 'test@test.pl'
INVALID_PASSWORD = 'hasuo'

github_username = os.getenv('GITHUB_USERNAME')
github_password = os.getenv('GITHUB_PASSWORD')

@given('I am on the GitHub homepage')
def step_given_goto_github_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get('https://github.com/')
    context.wait = WebDriverWait(context.driver, 10)

@when('I click on "{link_text}"')
def step_when_click_link(context, link_text):
    link = context.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
    link.click()

@when('I should enter invalid credentials')
def step_when_enter_invalid_credentials(context):
    time.sleep(2)
    username_field = context.wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
    username_field.send_keys(INVALID_USERNAME)

    password_field = context.wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_field.send_keys(INVALID_PASSWORD)

@when('I should click on "Sign in" button')
def step_when_click_sign_in(context):
    try:
        # Sprawdź, czy okno przeglądarki istnieje
        context.driver.title
    except NoSuchWindowException:
        # Jeśli okno nie istnieje, otwórz nowe okno
        context.driver = webdriver.Firefox()

    # Kliknij przycisk "Sign in" z oczekiwaniem na klikalność
    try:
        sign_in_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'commit'))
        )
        sign_in_button.click()
    except TimeoutException:
        # Przerywamy test i wypisujemy komunikat w przypadku TimeoutException
        print("TimeoutException: Sign in button not clickable within 10 seconds.")
        context.driver.quit()
        assert False

@then('I should see a failed login attempt message')
def step_then_failed_login_attempt(context):
    # Dodatkowe oczekiwanie na pojawienie się komunikatu o błędzie
    error_message = context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.js-flash-alert')))

    # Pobierz tekst komunikatu i usuń białe znaki na początku i końcu
    actual_error_text = error_message.text.strip()

    # Sprawdź, czy komunikat zawiera oczekiwany tekst (bez białych znaków na początku i końcu)
    assert 'Incorrect username or password.' in actual_error_text

@when('I should enter valid credentials')
def step_when_enter_valid_credentials(context):
    time.sleep(2)
    username_field = context.wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
    username_field.send_keys(github_username)

    password_field = context.wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_field.send_keys(github_password)

@then('I should successfully log in to GitHub')
def step_then_successful_login(context):
    # Oczekuj na pojawienie się elementu z nagłówkiem "Home"
    try:
        home_header = context.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-target="feed-container.feedTitle"]'))
        )
        assert home_header.text == 'Home'
    except TimeoutException:
        # Przerywamy test i wypisujemy komunikat w przypadku TimeoutException
        print("TimeoutException: Home header not visible within 10 seconds.")
        context.driver.quit()
        assert False