# PosPoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Point']
**coordinates** | **List[float]** |  | 

## Example

```python
from gwm_client.models.pos_point import PosPoint

# TODO update the JSON string below
json = "{}"
# create an instance of PosPoint from a JSON string
pos_point_instance = PosPoint.from_json(json)
# print the JSON string representation of the object
print PosPoint.to_json()

# convert the object into a dict
pos_point_dict = pos_point_instance.to_dict()
# create an instance of PosPoint from a dict
pos_point_form_dict = pos_point.from_dict(pos_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


