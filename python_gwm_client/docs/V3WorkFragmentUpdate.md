# V3WorkFragmentUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity_delivered** | **int** |  | [optional] 
**status** | **str** | Status  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**rejection_reason** | **str** | Used as a rejection reason if the work payload fragment is rejected | [optional] 

## Example

```python
from gwm_client.models.v3_work_fragment_update import V3WorkFragmentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of V3WorkFragmentUpdate from a JSON string
v3_work_fragment_update_instance = V3WorkFragmentUpdate.from_json(json)
# print the JSON string representation of the object
print V3WorkFragmentUpdate.to_json()

# convert the object into a dict
v3_work_fragment_update_dict = v3_work_fragment_update_instance.to_dict()
# create an instance of V3WorkFragmentUpdate from a dict
v3_work_fragment_update_form_dict = v3_work_fragment_update.from_dict(v3_work_fragment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


