Feature: GitHub Login

  Scenario: Attempt to login with invalid credentials
    Given I navigate to the GitHub login page
    When I enter invalid credentials
    Then I should see an error message

  Scenario: Login with valid credentials
    Given I navigate to the GitHub login page
    When I enter valid credentials
    Then I should be successfully logged in
