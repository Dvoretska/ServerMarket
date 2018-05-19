Feature: Account authentication

  Scenario: Login user with credentials
    Given test user with test@test.com and test_password
    When user login with test@test.com  and test_password
    Then we have token in response
      And status code will be 200

  Scenario: Login user with wrong password
    When user login with test@test.com and wrong password
    Then we have non_field_errors error with Unable to log in with provided credentials.
      And status code will be 400

  Scenario: Login user with wrong email
    When user login with test@wrong.com and test_password
    Then we have non_field_errors error with Unable to log in with provided credentials.
      And status code will be 400

  Scenario: Login user invalid email
    When user login with tes/t@ and test_password
    Then we have email error with Enter a valid email address.
      And status code will be 400