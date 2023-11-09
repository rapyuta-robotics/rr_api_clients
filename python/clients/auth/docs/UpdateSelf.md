# UpdateSelf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from auth.models.update_self import UpdateSelf

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSelf from a JSON string
update_self_instance = UpdateSelf.from_json(json)
# print the JSON string representation of the object
print UpdateSelf.to_json()

# convert the object into a dict
update_self_dict = update_self_instance.to_dict()
# create an instance of UpdateSelf from a dict
update_self_form_dict = update_self.from_dict(update_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


