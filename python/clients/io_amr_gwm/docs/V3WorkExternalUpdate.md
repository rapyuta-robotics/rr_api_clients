# V3WorkExternalUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority of the work | [optional] 
**cut_off_time** | **datetime** | Cut off time of the work | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for this object | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from io_amr_gwm.models.v3_work_external_update import V3WorkExternalUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of V3WorkExternalUpdate from a JSON string
v3_work_external_update_instance = V3WorkExternalUpdate.from_json(json)
# print the JSON string representation of the object
print V3WorkExternalUpdate.to_json()

# convert the object into a dict
v3_work_external_update_dict = v3_work_external_update_instance.to_dict()
# create an instance of V3WorkExternalUpdate from a dict
v3_work_external_update_form_dict = v3_work_external_update.from_dict(v3_work_external_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


