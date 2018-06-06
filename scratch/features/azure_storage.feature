Feature: Azure Storage Policy

   These are policy statments that help to make sure that Azure Storage is configured appropriately 

Scenario: Storage Account should have encryption enabled 
    Given we have a valid subscription
    When we configure a Storage Account
    Then the Storage Account should have encryption enabled

Scenario: Storage Account should have https enabled
    Given we have a valid subscription
    When we configure a Storage Account
    Then the Storage Account should have https enabled

Scenario: Storage Account should have logging enabled
    Given we have a valid subscription
    When we configure a Storage Account
    Then the Storage Account should have logging enabled
