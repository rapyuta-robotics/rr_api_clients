# Create


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**password** | **str** |  | [optional] 
**group** | **str** |  | 
**details** | **object** |  | 

## Example

```python
from auth_client.models.create import Create

# TODO update the JSON string below
json = "{}"
# create an instance of Create from a JSON string
create_instance = Create.from_json(json)
# print the JSON string representation of the object
print Create.to_json()

# convert the object into a dict
create_dict = create_instance.to_dict()
# create an instance of Create from a dict
create_form_dict = create.from_dict(create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


