# PatchedContainerDescriptorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**type** | **str** | Type of the object | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**groups** | **List[str]** |  | [optional] 

## Example

```python
from gwm.models.patched_container_descriptor_request import PatchedContainerDescriptorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedContainerDescriptorRequest from a JSON string
patched_container_descriptor_request_instance = PatchedContainerDescriptorRequest.from_json(json)
# print the JSON string representation of the object
print PatchedContainerDescriptorRequest.to_json()

# convert the object into a dict
patched_container_descriptor_request_dict = patched_container_descriptor_request_instance.to_dict()
# create an instance of PatchedContainerDescriptorRequest from a dict
patched_container_descriptor_request_form_dict = patched_container_descriptor_request.from_dict(patched_container_descriptor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


