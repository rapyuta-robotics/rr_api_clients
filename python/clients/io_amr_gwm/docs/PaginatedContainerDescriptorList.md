# PaginatedContainerDescriptorList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ContainerDescriptor]**](ContainerDescriptor.md) |  | [optional] 

## Example

```python
from openapi_client.models.paginated_container_descriptor_list import PaginatedContainerDescriptorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContainerDescriptorList from a JSON string
paginated_container_descriptor_list_instance = PaginatedContainerDescriptorList.from_json(json)
# print the JSON string representation of the object
print PaginatedContainerDescriptorList.to_json()

# convert the object into a dict
paginated_container_descriptor_list_dict = paginated_container_descriptor_list_instance.to_dict()
# create an instance of PaginatedContainerDescriptorList from a dict
paginated_container_descriptor_list_form_dict = paginated_container_descriptor_list.from_dict(paginated_container_descriptor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


