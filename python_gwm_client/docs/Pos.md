# Pos


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos** | [**PosPoint**](PosPoint.md) |  | [optional] 
**yaw** | **float** |  | [optional] 
**map** | **Dict[str, object]** |  | [optional] 

## Example

```python
from gwm_client.models.pos import Pos

# TODO update the JSON string below
json = "{}"
# create an instance of Pos from a JSON string
pos_instance = Pos.from_json(json)
# print the JSON string representation of the object
print Pos.to_json()

# convert the object into a dict
pos_dict = pos_instance.to_dict()
# create an instance of Pos from a dict
pos_form_dict = pos.from_dict(pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


