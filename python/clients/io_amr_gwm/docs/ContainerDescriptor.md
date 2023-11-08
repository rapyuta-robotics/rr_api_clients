# ContainerDescriptor


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
from io_amr_gwm.models.container_descriptor import ContainerDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerDescriptor from a JSON string
container_descriptor_instance = ContainerDescriptor.from_json(json)
# print the JSON string representation of the object
print ContainerDescriptor.to_json()

# convert the object into a dict
container_descriptor_dict = container_descriptor_instance.to_dict()
# create an instance of ContainerDescriptor from a dict
container_descriptor_form_dict = container_descriptor.from_dict(container_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


