# Layer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | Type of the layer | 
**order** | **int** | Layer height of the small integer (0 indicates default and on the bottom) | [optional] 
**resolution** | **float** | Resolution of the map, meters / pixel | [optional] 
**origin_pos** | [**LayerOriginPos**](LayerOriginPos.md) |  | [optional] 
**origin_yaw** | **float** | Orientation of the map in radians | [optional] 
**negate** | **bool** | Whether the white/black free/occupied semantics should be reversed (interpretation of thresholds is unaffected) | [optional] 
**occupied_thresh** | **float** | Pixels with occupancy probability greater than this threshold are considered completely occupied. | [optional] 
**image** | **str** | Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file | [readonly] 
**data** | **str** |  | [readonly] 
**properties** | **Dict[str, object]** | Additional properties for this layer in JSON format | [optional] 
**free_thresh** | **float** | Pixels with occupancy probability less than this threshold are considered completely free. | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**version** | **int** | System generated monotonic integer that is updated for each mutation to layer properties or image | [readonly] 
**created_at** | **datetime** | Timestamp at which this layer was created | [readonly] 

## Example

```python
from io_amr_gwm.models.layer import Layer

# TODO update the JSON string below
json = "{}"
# create an instance of Layer from a JSON string
layer_instance = Layer.from_json(json)
# print the JSON string representation of the object
print Layer.to_json()

# convert the object into a dict
layer_dict = layer_instance.to_dict()
# create an instance of Layer from a dict
layer_form_dict = layer.from_dict(layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


