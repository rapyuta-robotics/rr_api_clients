# PatchedWorkPayloadFragmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;ITEM_MOVE&#x60; - Item Move * &#x60;CONTAINER_MOVE&#x60; - Container Move | [optional] 
**id** | **int** |  | [optional] 
**status** | **str** | Status  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**rejection_reason** | **str** | Used as a rejection reason if the work payload fragment is rejected | [optional] 
**from_spot** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**to_spot** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**from_region** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**to_region** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**from_pos** | [**InternalWorkPayloadFragmentRequestToPos**](InternalWorkPayloadFragmentRequestToPos.md) |  | [optional] 
**to_pos** | [**InternalWorkPayloadFragmentRequestToPos**](InternalWorkPayloadFragmentRequestToPos.md) |  | [optional] 
**from_yaw** | **float** | Desired orientation in radians of the agent | [optional] 
**to_yaw** | **float** | Desired orientation in radians of the agent | [optional] 
**from_map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**to_map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**from_spot_query** | **Dict[str, object]** |  | [optional] 
**to_spot_query** | **Dict[str, object]** |  | [optional] 
**name** | **str** | Name | [optional] 
**quantity_requested** | **int** | How many was requested by the order | [optional] 
**quantity_delivered** | **int** | How much was actually delivered to the customer | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**workflow** | **str** | Examples: replenishment, transport | [optional] 

## Example

```python
from gwm.models.patched_work_payload_fragment_request import PatchedWorkPayloadFragmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWorkPayloadFragmentRequest from a JSON string
patched_work_payload_fragment_request_instance = PatchedWorkPayloadFragmentRequest.from_json(json)
# print the JSON string representation of the object
print PatchedWorkPayloadFragmentRequest.to_json()

# convert the object into a dict
patched_work_payload_fragment_request_dict = patched_work_payload_fragment_request_instance.to_dict()
# create an instance of PatchedWorkPayloadFragmentRequest from a dict
patched_work_payload_fragment_request_form_dict = patched_work_payload_fragment_request.from_dict(patched_work_payload_fragment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


