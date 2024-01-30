from datetime import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I navigate to the GitHub login page')
def step_impl(context):
    context.driver.get('https://github.com/login')
    time.sleep(2)  # Poczekaj 2 sekundy, aby dać stronie czas na załadowanie
    pass

@when('I enter invalid credentials')
def step_impl(context):
    # Implementacja kroków do wprowadzenia nieprawidłowych danych
    username_field = context.driver.find_element(By.ID, 'login_field')
    password_field = context.driver.find_element(By.ID, 'password')
    login_button = context.driver.find_element(By.NAME, 'commit')

    username_field.send_keys('INVALID_USERNAME')
    password_field.send_keys('INVALID_PASSWORD')
    login_button.click()
    pass

@then('I should see an error message')
def step_impl(context):
    # Implementacja kroków do sprawdzenia komunikatu o błędzie
    wait = WebDriverWait(context.driver, 10)
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.flash-error')))
    assert 'Incorrect username or password.' in error_message.text
    pass

@when('I enter valid credentials')
def step_impl(context):
    # Implementacja kroków do wprowadzenia prawidłowych danych
    username_field = context.driver.find_element(By.ID, 'login_field')
    password_field = context.driver.find_element(By.ID, 'password')
    login_button = context.driver.find_element(By.NAME, 'commit')

    username_field.send_keys(context.github_username)
    password_field.send_keys(context.github_password)
    login_button.click()
    pass

@then('I should be successfully logged in')
def step_impl(context):
    # Implementacja kroków do sprawdzenia sukcesu logowania
    assert context.driver.current_url == 'https://github.com/'
    pass