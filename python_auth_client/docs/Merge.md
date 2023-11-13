# Merge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**username** | **str** |  | 
**password** | **str** |  | [optional] 

## Example

```python
from auth_client.models.merge import Merge

# TODO update the JSON string below
json = "{}"
# create an instance of Merge from a JSON string
merge_instance = Merge.from_json(json)
# print the JSON string representation of the object
print Merge.to_json()

# convert the object into a dict
merge_dict = merge_instance.to_dict()
# create an instance of Merge from a dict
merge_form_dict = merge.from_dict(merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


