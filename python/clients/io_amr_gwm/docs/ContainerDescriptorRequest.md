# ContainerDescriptorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**type** | **str** | Type of the object | [optional] 
**length** | **float** |  | 
**width** | **float** |  | 
**height** | **float** |  | 
**groups** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.container_descriptor_request import ContainerDescriptorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerDescriptorRequest from a JSON string
container_descriptor_request_instance = ContainerDescriptorRequest.from_json(json)
# print the JSON string representation of the object
print ContainerDescriptorRequest.to_json()

# convert the object into a dict
container_descriptor_request_dict = container_descriptor_request_instance.to_dict()
# create an instance of ContainerDescriptorRequest from a dict
container_descriptor_request_form_dict = container_descriptor_request.from_dict(container_descriptor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


