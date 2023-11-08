# PatchedAgentTaskRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**required_agent** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**work** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**id** | **int** |  | [optional] 
**status** | **str** | Current status of the agent task  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted | [optional] 
**type** | **str** | Agent task type  * &#x60;ADHOC_MOVE&#x60; - Adhoc Move * &#x60;CHARGE&#x60; - Charge * &#x60;EXPLORE&#x60; - Explore * &#x60;PAYLOAD_MOVE&#x60; - Payload Move * &#x60;DYNAMIC_PAYLOAD_MOVE&#x60; - Dynamic Payload Move | [optional] 
**assignment_data** | **Dict[str, object]** | Data set by the task assigner.  For example, the location on the robot corresponding to the task | [optional] 
**action_data** | **Dict[str, object]** | optional JSON encoded action metadata | [optional] 
**split_data** | **Dict[str, object]** | Data set by work splitter for the sake of task assignment | [optional] 
**workflow** | **str** | Examples: replenishment, transport | [optional] 
**priority** | **int** | Priority of the task | [optional] 
**location** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.patched_agent_task_request import PatchedAgentTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentTaskRequest from a JSON string
patched_agent_task_request_instance = PatchedAgentTaskRequest.from_json(json)
# print the JSON string representation of the object
print PatchedAgentTaskRequest.to_json()

# convert the object into a dict
patched_agent_task_request_dict = patched_agent_task_request_instance.to_dict()
# create an instance of PatchedAgentTaskRequest from a dict
patched_agent_task_request_form_dict = patched_agent_task_request.from_dict(patched_agent_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


