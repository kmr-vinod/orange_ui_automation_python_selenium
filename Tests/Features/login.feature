Feature: Login to application
  Scenario:
    Given login to application
    Then verify if dashboard is displayed
    When click "Admin" link on side navigation
    When click "PIM" link on side navigation
    When click "Leave" link on side navigation

