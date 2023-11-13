# AutoRecoveryAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**content** | **Dict[str, object]** | Information to fill in that should match the schema of the recovery action | 
**first_attempt_after** | **float** | Amount of time before making the first attempt | 
**retry_interval** | **float** | Amount of time between subsequent attempts | 
**max_attempts** | **int** | Number of times to retry the specific action | [optional] 

## Example

```python
from gwm_client.models.auto_recovery_action import AutoRecoveryAction

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRecoveryAction from a JSON string
auto_recovery_action_instance = AutoRecoveryAction.from_json(json)
# print the JSON string representation of the object
print AutoRecoveryAction.to_json()

# convert the object into a dict
auto_recovery_action_dict = auto_recovery_action_instance.to_dict()
# create an instance of AutoRecoveryAction from a dict
auto_recovery_action_form_dict = auto_recovery_action.from_dict(auto_recovery_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


