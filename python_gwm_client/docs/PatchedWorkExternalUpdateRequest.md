# PatchedWorkExternalUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority of the work | [optional] 
**cut_off_time** | **datetime** | Cut off time of the work | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm_client.models.patched_work_external_update_request import PatchedWorkExternalUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWorkExternalUpdateRequest from a JSON string
patched_work_external_update_request_instance = PatchedWorkExternalUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PatchedWorkExternalUpdateRequest.to_json()

# convert the object into a dict
patched_work_external_update_request_dict = patched_work_external_update_request_instance.to_dict()
# create an instance of PatchedWorkExternalUpdateRequest from a dict
patched_work_external_update_request_form_dict = patched_work_external_update_request.from_dict(patched_work_external_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


