# PaginatedWorkPayloadFragmentList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[WorkPayloadFragment]**](WorkPayloadFragment.md) |  | [optional] 

## Example

```python
from openapi_client.models.paginated_work_payload_fragment_list import PaginatedWorkPayloadFragmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkPayloadFragmentList from a JSON string
paginated_work_payload_fragment_list_instance = PaginatedWorkPayloadFragmentList.from_json(json)
# print the JSON string representation of the object
print PaginatedWorkPayloadFragmentList.to_json()

# convert the object into a dict
paginated_work_payload_fragment_list_dict = paginated_work_payload_fragment_list_instance.to_dict()
# create an instance of PaginatedWorkPayloadFragmentList from a dict
paginated_work_payload_fragment_list_form_dict = paginated_work_payload_fragment_list.from_dict(paginated_work_payload_fragment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


