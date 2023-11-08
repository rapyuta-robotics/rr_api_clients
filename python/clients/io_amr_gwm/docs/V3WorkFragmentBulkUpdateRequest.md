# V3WorkFragmentBulkUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**quantity_delivered** | **int** |  | [optional] 
**status** | **str** | Status  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**rejection_reason** | **str** | Used as a rejection reason if the work payload fragment is rejected | [optional] 

## Example

```python
from io_amr_gwm.models.v3_work_fragment_bulk_update_request import V3WorkFragmentBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V3WorkFragmentBulkUpdateRequest from a JSON string
v3_work_fragment_bulk_update_request_instance = V3WorkFragmentBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print V3WorkFragmentBulkUpdateRequest.to_json()

# convert the object into a dict
v3_work_fragment_bulk_update_request_dict = v3_work_fragment_bulk_update_request_instance.to_dict()
# create an instance of V3WorkFragmentBulkUpdateRequest from a dict
v3_work_fragment_bulk_update_request_form_dict = v3_work_fragment_bulk_update_request.from_dict(v3_work_fragment_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


