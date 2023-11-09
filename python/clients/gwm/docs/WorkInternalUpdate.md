# WorkInternalUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**rejection_reason** | **str** | Used as a rejection reason if the work is rejected | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**fragments** | [**List[WorkPayloadFragment]**](WorkPayloadFragment.md) |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm_client.models.work_internal_update import WorkInternalUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkInternalUpdate from a JSON string
work_internal_update_instance = WorkInternalUpdate.from_json(json)
# print the JSON string representation of the object
print WorkInternalUpdate.to_json()

# convert the object into a dict
work_internal_update_dict = work_internal_update_instance.to_dict()
# create an instance of WorkInternalUpdate from a dict
work_internal_update_form_dict = work_internal_update.from_dict(work_internal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


