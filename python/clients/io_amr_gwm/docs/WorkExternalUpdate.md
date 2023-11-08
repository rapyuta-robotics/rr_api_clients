# WorkExternalUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority of the work | [optional] 
**cut_off_time** | **datetime** | Cut off time of the work | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from openapi_client.models.work_external_update import WorkExternalUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkExternalUpdate from a JSON string
work_external_update_instance = WorkExternalUpdate.from_json(json)
# print the JSON string representation of the object
print WorkExternalUpdate.to_json()

# convert the object into a dict
work_external_update_dict = work_external_update_instance.to_dict()
# create an instance of WorkExternalUpdate from a dict
work_external_update_form_dict = work_external_update.from_dict(work_external_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


