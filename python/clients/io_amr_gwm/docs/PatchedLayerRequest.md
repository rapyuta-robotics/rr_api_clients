# PatchedLayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | Type of the layer | [optional] 
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
from io_amr_gwm.models.patched_layer_request import PatchedLayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLayerRequest from a JSON string
patched_layer_request_instance = PatchedLayerRequest.from_json(json)
# print the JSON string representation of the object
print PatchedLayerRequest.to_json()

# convert the object into a dict
patched_layer_request_dict = patched_layer_request_instance.to_dict()
# create an instance of PatchedLayerRequest from a dict
patched_layer_request_form_dict = patched_layer_request.from_dict(patched_layer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


