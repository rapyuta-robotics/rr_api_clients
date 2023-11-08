# PaginatedV3WorkList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[V3Work]**](V3Work.md) |  | [optional] 

## Example

```python
from gwm.models.paginated_v3_work_list import PaginatedV3WorkList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedV3WorkList from a JSON string
paginated_v3_work_list_instance = PaginatedV3WorkList.from_json(json)
# print the JSON string representation of the object
print PaginatedV3WorkList.to_json()

# convert the object into a dict
paginated_v3_work_list_dict = paginated_v3_work_list_instance.to_dict()
# create an instance of PaginatedV3WorkList from a dict
paginated_v3_work_list_form_dict = paginated_v3_work_list.from_dict(paginated_v3_work_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


