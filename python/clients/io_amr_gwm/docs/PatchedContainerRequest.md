# PatchedContainerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**descriptor** | **int** |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**type** | **str** | Specifies logical type since physical type is specified by descriptor. | [optional] 

## Example

```python
from io_amr_gwm.models.patched_container_request import PatchedContainerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedContainerRequest from a JSON string
patched_container_request_instance = PatchedContainerRequest.from_json(json)
# print the JSON string representation of the object
print PatchedContainerRequest.to_json()

# convert the object into a dict
patched_container_request_dict = patched_container_request_instance.to_dict()
# create an instance of PatchedContainerRequest from a dict
patched_container_request_form_dict = patched_container_request.from_dict(patched_container_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


