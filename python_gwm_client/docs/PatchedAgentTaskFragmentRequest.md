# PatchedAgentTaskFragmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_task** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**work_fragment** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**id** | **int** |  | [optional] 
**status** | **str** | Current status of the agent task  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;ASSIGNED&#x60; - Assigned * &#x60;PREPARING_TO_PICK&#x60; - Preparing To Pick * &#x60;PICKING&#x60; - Picking * &#x60;PICKED&#x60; - Picked * &#x60;PREPARING_TO_DROP&#x60; - Preparing To Drop * &#x60;DROPPING&#x60; - Dropping * &#x60;PREPARING_ACTION&#x60; - Preparing Action * &#x60;ACTION_IN_PROGRESS&#x60; - Action In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped | [optional] 
**type** | **str** | Payload move type  * &#x60;ITEM_MOVE&#x60; - Item Move * &#x60;CONTAINER_MOVE&#x60; - Container Move * &#x60;ACTION&#x60; - Action | [optional] 
**quantity_requested** | **int** | Quantity requested to deliver for this task fragment | [optional] 
**quantity_delivered** | **int** | Quantity delivered to destination | [optional] 
**quantity_picked** | **int** | Quantity picked | [optional] 
**payload_data** | **Dict[str, object]** | meta_data generated by work splitter to pass to Pick/Drop/RecognizePayload actions | [optional] 
**detection_data** | **Dict[str, object]** | Info recorded if RecognizePayload action is called | [optional] 
**action_data** | **Dict[str, object]** | optional JSON encoded action metadata | [optional] 
**pick_data** | **Dict[str, object]** | Info recorded when picking from PickDrop server | [optional] 
**drop_data** | **Dict[str, object]** | Info recorded when dropping from PickDrop server | [optional] 
**from_location** | **Dict[str, object]** | From location | [optional] 
**to_location** | **Dict[str, object]** | To location | [optional] 
**action_location** | [**LocationRequest**](LocationRequest.md) |  | [optional] 
**name** | **str** | Fragment name | [optional] 
**workflow** | **str** | Examples: replenishment, transport | [optional] 

## Example

```python
from gwm_client.models.patched_agent_task_fragment_request import PatchedAgentTaskFragmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentTaskFragmentRequest from a JSON string
patched_agent_task_fragment_request_instance = PatchedAgentTaskFragmentRequest.from_json(json)
# print the JSON string representation of the object
print PatchedAgentTaskFragmentRequest.to_json()

# convert the object into a dict
patched_agent_task_fragment_request_dict = patched_agent_task_fragment_request_instance.to_dict()
# create an instance of PatchedAgentTaskFragmentRequest from a dict
patched_agent_task_fragment_request_form_dict = patched_agent_task_fragment_request.from_dict(patched_agent_task_fragment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


