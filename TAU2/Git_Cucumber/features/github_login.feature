Feature: GitHub Login

  Scenario: Attempt to login with invalid credentials
    Given I am on the GitHub homepage
    When I click on "Sign in"
    And I should enter invalid credentials
    And I should click on "Sign in" button
    Then I should see a failed login attempt message

  Scenario: Successfully login with valid credentials
    Given I am on the GitHub homepage
    When I click on "Sign in"
    And I should enter valid credentials
    And I should click on "Sign in" button
    Then I should successfully log in to GitHub
