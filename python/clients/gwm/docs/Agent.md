# Agent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**robot_id** | **int** |  | 
**robot_descriptor_id** | **int** |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**mode** | **str** | * &#x60;Manual&#x60; - Manual * &#x60;Automatic&#x60; - Automatic * &#x60;Offline&#x60; - Offline * &#x60;Paused&#x60; - Paused * &#x60;Emergency Stop&#x60; - Emergency Stop | [optional] 
**assigned_workflow** | **str** |  | [optional] 

## Example

```python
from gwm_client.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


