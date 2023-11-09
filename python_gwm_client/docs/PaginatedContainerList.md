# PaginatedContainerList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Container]**](Container.md) |  | [optional] 

## Example

```python
from gwm_client.models.paginated_container_list import PaginatedContainerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContainerList from a JSON string
paginated_container_list_instance = PaginatedContainerList.from_json(json)
# print the JSON string representation of the object
print PaginatedContainerList.to_json()

# convert the object into a dict
paginated_container_list_dict = paginated_container_list_instance.to_dict()
# create an instance of PaginatedContainerList from a dict
paginated_container_list_form_dict = paginated_container_list.from_dict(paginated_container_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


