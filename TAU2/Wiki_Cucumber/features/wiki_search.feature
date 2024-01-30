Feature: Wikipedia Search

  Scenario: User searches for a term on Wikipedia
    Given the user is on the Wikipedia homepage
    When the user enters "Cucumber" in the search bar
    And the user clicks on the search button
    Then the search results page should be displayed
    And the search results should contain the term "Cucumber"
