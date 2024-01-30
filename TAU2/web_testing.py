from selenium import webdriver
import os
from behave.__main__ import main as behave_main

# Wprowadź dane do logowania bezpośrednio w kodzie
github_username = "s22982"
github_password = "Quakk9988!"

# Ustaw zmienne środowiskowe dla Cucumbera
os.environ['GITHUB_USERNAME'] = github_username
os.environ['GITHUB_PASSWORD'] = github_password

# Uruchom testy Behave (Cucumber)
behave_main(["features"])
