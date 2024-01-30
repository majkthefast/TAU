from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then

@given('the user is on the Wikipedia homepage')
def step_given_user_on_wikipedia_homepage(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna")

@when('the user enters "{search_term}" in the search bar')
def step_when_user_enters_search_term(context, search_term):
    search_input = context.driver.find_element(By.NAME, 'search')
    search_input.send_keys(search_term)

@when('the user clicks on the search button')
def step_when_user_clicks_search_button(context):
    search_input = context.driver.find_element(By.NAME, 'search')
    ActionChains(context.driver).move_to_element(search_input).send_keys(Keys.RETURN).perform()

@then('the search results page should be displayed')
def step_then_search_results_page_displayed(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#firstHeading')))

@then('the search results should contain the term "{expected_term}"')
def step_then_search_results_contain_term(context, expected_term):
    search_results = context.driver.find_elements(By.XPATH, "//div[@class='searchresults']/li")
    for result in search_results:
        assert expected_term.lower() in result.text.lower()

@then('the user finishes the search')
def step_then_user_finishes_search(context):
    context.driver.quit()
