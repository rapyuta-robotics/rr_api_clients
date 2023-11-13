# AgentModeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | * &#x60;Manual&#x60; - Manual * &#x60;Automatic&#x60; - Automatic * &#x60;Offline&#x60; - Offline * &#x60;Paused&#x60; - Paused * &#x60;Emergency Stop&#x60; - Emergency Stop | 

## Example

```python
from gwm_client.models.agent_mode_request import AgentModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentModeRequest from a JSON string
agent_mode_request_instance = AgentModeRequest.from_json(json)
# print the JSON string representation of the object
print AgentModeRequest.to_json()

# convert the object into a dict
agent_mode_request_dict = agent_mode_request_instance.to_dict()
# create an instance of AgentModeRequest from a dict
agent_mode_request_form_dict = agent_mode_request.from_dict(agent_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


