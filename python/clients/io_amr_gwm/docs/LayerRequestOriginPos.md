# LayerRequestOriginPos

Origin of map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from io_amr_gwm.models.layer_request_origin_pos import LayerRequestOriginPos

# TODO update the JSON string below
json = "{}"
# create an instance of LayerRequestOriginPos from a JSON string
layer_request_origin_pos_instance = LayerRequestOriginPos.from_json(json)
# print the JSON string representation of the object
print LayerRequestOriginPos.to_json()

# convert the object into a dict
layer_request_origin_pos_dict = layer_request_origin_pos_instance.to_dict()
# create an instance of LayerRequestOriginPos from a dict
layer_request_origin_pos_form_dict = layer_request_origin_pos.from_dict(layer_request_origin_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


