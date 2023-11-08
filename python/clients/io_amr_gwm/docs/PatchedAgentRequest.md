# PatchedAgentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**robot_id** | **int** |  | [optional] 
**robot_descriptor_id** | **int** |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**mode** | **str** | * &#x60;Manual&#x60; - Manual * &#x60;Automatic&#x60; - Automatic * &#x60;Offline&#x60; - Offline * &#x60;Paused&#x60; - Paused * &#x60;Emergency Stop&#x60; - Emergency Stop | [optional] 
**assigned_workflow** | **str** |  | [optional] 

## Example

```python
from io_amr_gwm.models.patched_agent_request import PatchedAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentRequest from a JSON string
patched_agent_request_instance = PatchedAgentRequest.from_json(json)
# print the JSON string representation of the object
print PatchedAgentRequest.to_json()

# convert the object into a dict
patched_agent_request_dict = patched_agent_request_instance.to_dict()
# create an instance of PatchedAgentRequest from a dict
patched_agent_request_form_dict = patched_agent_request.from_dict(patched_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


