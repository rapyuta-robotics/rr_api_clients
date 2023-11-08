# ContainerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**descriptor** | **int** |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**type** | **str** | Specifies logical type since physical type is specified by descriptor. | [optional] 

## Example

```python
from gwm.models.container_request import ContainerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRequest from a JSON string
container_request_instance = ContainerRequest.from_json(json)
# print the JSON string representation of the object
print ContainerRequest.to_json()

# convert the object into a dict
container_request_dict = container_request_instance.to_dict()
# create an instance of ContainerRequest from a dict
container_request_form_dict = container_request.from_dict(container_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


