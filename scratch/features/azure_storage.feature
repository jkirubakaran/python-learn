Feature: Azure Storage Policy

   These are policy statments that help to make sure that Azure Storage is configured appropriately 

Scenario Outline: Storage Account should have encryption enabled 
    Given we have a "<type>" subscription
    When we configure a Storage Account
    Then the Storage Account should have encryption enabled

    Examples:
    | type |
    | Connected  |
    | Dis-Connected | 

Scenario Outline: Storage Account should have https enabled
    Given we have a "<type>" subscription
    When we configure a Storage Account
    Then the Storage Account should have https enabled

    Examples:
    | type |
    | Connected  |
    | Dis-Connected |

Scenario Outline: Storage Account should have logging enabled
    Given we have a "<type>" subscription
    When we configure a Storage Account
    Then the Storage Account should have logging enabled

    Examples:
    | type |
    | Connected  |


    


