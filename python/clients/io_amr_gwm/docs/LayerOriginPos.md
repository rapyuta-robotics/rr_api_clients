# LayerOriginPos

Origin of map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from io_amr_gwm.models.layer_origin_pos import LayerOriginPos

# TODO update the JSON string below
json = "{}"
# create an instance of LayerOriginPos from a JSON string
layer_origin_pos_instance = LayerOriginPos.from_json(json)
# print the JSON string representation of the object
print LayerOriginPos.to_json()

# convert the object into a dict
layer_origin_pos_dict = layer_origin_pos_instance.to_dict()
# create an instance of LayerOriginPos from a dict
layer_origin_pos_form_dict = layer_origin_pos.from_dict(layer_origin_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


