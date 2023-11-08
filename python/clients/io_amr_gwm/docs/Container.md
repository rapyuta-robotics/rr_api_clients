# Container


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**descriptor** | **int** |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**descriptor_name** | **str** | Descriptor Name | [readonly] 
**descriptor_type** | **str** | Type of the object | [readonly] 
**type** | **str** | Specifies logical type since physical type is specified by descriptor. | [optional] 

## Example

```python
from io_amr_gwm.models.container import Container

# TODO update the JSON string below
json = "{}"
# create an instance of Container from a JSON string
container_instance = Container.from_json(json)
# print the JSON string representation of the object
print Container.to_json()

# convert the object into a dict
container_dict = container_instance.to_dict()
# create an instance of Container from a dict
container_form_dict = container.from_dict(container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


