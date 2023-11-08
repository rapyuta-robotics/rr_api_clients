# WorkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | user provided name eg: &#x60;mywarehouse_move_2021-05-11T12:05:27Z&#x60; | [optional] 
**priority** | **int** | Priority of the work | [optional] 
**type** | **str** | Type of the work  * &#x60;CHARGE&#x60; - Charge * &#x60;EXPLORE&#x60; - Explore * &#x60;PAYLOAD_MOVE&#x60; - Payload Move * &#x60;ADHOC_MOVE_POSITION&#x60; - Adhoc Move Position * &#x60;ADHOC_MOVE_REGION&#x60; - Adhoc Move Region * &#x60;ADHOC_MOVE_SPOT&#x60; - Adhoc Move Spot | 
**status** | **str** | Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**cut_off_time** | **datetime** | Cut off time of the work | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**workflow** | **str** | Examples: replenishment, transport | [optional] 
**batch** | **str** |  | [optional] 
**assigned_agent** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**spot** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**pos** | [**InternalWorkPayloadFragmentRequestToPos**](InternalWorkPayloadFragmentRequestToPos.md) |  | [optional] 
**yaw** | **float** | Desired orientation in radians of the agent | [optional] 
**map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**fragments** | [**List[PatchedWorkPayloadFragmentRequest]**](PatchedWorkPayloadFragmentRequest.md) |  | [optional] 
**region** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm.models.work_request import WorkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRequest from a JSON string
work_request_instance = WorkRequest.from_json(json)
# print the JSON string representation of the object
print WorkRequest.to_json()

# convert the object into a dict
work_request_dict = work_request_instance.to_dict()
# create an instance of WorkRequest from a dict
work_request_form_dict = work_request.from_dict(work_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


