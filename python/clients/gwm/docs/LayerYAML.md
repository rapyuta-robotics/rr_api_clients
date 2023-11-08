# LayerYAML


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file | [optional] 
**resolution** | **float** | Resolution of the map, meters / pixel | [optional] 
**origin_pos** | [**LayerOriginPos**](LayerOriginPos.md) |  | [optional] 
**origin_yaw** | **float** | Orientation of the map in radians | [optional] 
**negate** | **bool** | Whether the white/black free/occupied semantics should be reversed (interpretation of thresholds is unaffected) | [optional] 
**occupied_thresh** | **float** | Pixels with occupancy probability greater than this threshold are considered completely occupied. | [optional] 
**free_thresh** | **float** | Pixels with occupancy probability less than this threshold are considered completely free. | [optional] 

## Example

```python
from gwm.models.layer_yaml import LayerYAML

# TODO update the JSON string below
json = "{}"
# create an instance of LayerYAML from a JSON string
layer_yaml_instance = LayerYAML.from_json(json)
# print the JSON string representation of the object
print LayerYAML.to_json()

# convert the object into a dict
layer_yaml_dict = layer_yaml_instance.to_dict()
# create an instance of LayerYAML from a dict
layer_yaml_form_dict = layer_yaml.from_dict(layer_yaml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


