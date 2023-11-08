# LayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | Type of the layer | 
**order** | **int** | Layer height of the small integer (0 indicates default and on the bottom) | [optional] 
**resolution** | **float** | Resolution of the map, meters / pixel | [optional] 
**origin_pos** | [**LayerRequestOriginPos**](LayerRequestOriginPos.md) |  | [optional] 
**origin_yaw** | **float** | Orientation of the map in radians | [optional] 
**negate** | **bool** | Whether the white/black free/occupied semantics should be reversed (interpretation of thresholds is unaffected) | [optional] 
**occupied_thresh** | **float** | Pixels with occupancy probability greater than this threshold are considered completely occupied. | [optional] 
**properties** | **Dict[str, object]** | Additional properties for this layer in JSON format | [optional] 
**free_thresh** | **float** | Pixels with occupancy probability less than this threshold are considered completely free. | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm.models.layer_request import LayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LayerRequest from a JSON string
layer_request_instance = LayerRequest.from_json(json)
# print the JSON string representation of the object
print LayerRequest.to_json()

# convert the object into a dict
layer_request_dict = layer_request_instance.to_dict()
# create an instance of LayerRequest from a dict
layer_request_form_dict = layer_request.from_dict(layer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


