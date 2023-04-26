Feature: Search on Google

  Scenario: Search for a term on Google
    Given I am on the Google homepage
    When I search for "test automation"
    Then I should see search results for "test automation"