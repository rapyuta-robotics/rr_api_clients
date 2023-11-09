# PatchedInternalWorkPayloadFragmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**rejection_reason** | **str** | Used as a rejection reason if the work payload fragment is rejected | [optional] 
**to_spot** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**to_region** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**to_pos** | [**InternalWorkPayloadFragmentRequestToPos**](InternalWorkPayloadFragmentRequestToPos.md) |  | [optional] 
**to_yaw** | **float** | Desired orientation in radians of the agent | [optional] 
**to_map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**name** | **str** | Name | [optional] 
**quantity_delivered** | **int** | How much was actually delivered to the customer | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**quantity_requested** | **int** | How many was requested by the order | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm_client.models.patched_internal_work_payload_fragment_request import PatchedInternalWorkPayloadFragmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInternalWorkPayloadFragmentRequest from a JSON string
patched_internal_work_payload_fragment_request_instance = PatchedInternalWorkPayloadFragmentRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInternalWorkPayloadFragmentRequest.to_json()

# convert the object into a dict
patched_internal_work_payload_fragment_request_dict = patched_internal_work_payload_fragment_request_instance.to_dict()
# create an instance of PatchedInternalWorkPayloadFragmentRequest from a dict
patched_internal_work_payload_fragment_request_form_dict = patched_internal_work_payload_fragment_request.from_dict(patched_internal_work_payload_fragment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


