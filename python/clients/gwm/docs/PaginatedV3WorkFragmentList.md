# PaginatedV3WorkFragmentList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[V3WorkFragment]**](V3WorkFragment.md) |  | [optional] 

## Example

```python
from gwm.models.paginated_v3_work_fragment_list import PaginatedV3WorkFragmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedV3WorkFragmentList from a JSON string
paginated_v3_work_fragment_list_instance = PaginatedV3WorkFragmentList.from_json(json)
# print the JSON string representation of the object
print PaginatedV3WorkFragmentList.to_json()

# convert the object into a dict
paginated_v3_work_fragment_list_dict = paginated_v3_work_fragment_list_instance.to_dict()
# create an instance of PaginatedV3WorkFragmentList from a dict
paginated_v3_work_fragment_list_form_dict = paginated_v3_work_fragment_list.from_dict(paginated_v3_work_fragment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


