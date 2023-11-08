# PatchedMapGraphUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**floor** | **int** | Floor of the site this map corresponds to | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm.models.patched_map_graph_update_request import PatchedMapGraphUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMapGraphUpdateRequest from a JSON string
patched_map_graph_update_request_instance = PatchedMapGraphUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PatchedMapGraphUpdateRequest.to_json()

# convert the object into a dict
patched_map_graph_update_request_dict = patched_map_graph_update_request_instance.to_dict()
# create an instance of PatchedMapGraphUpdateRequest from a dict
patched_map_graph_update_request_form_dict = patched_map_graph_update_request.from_dict(patched_map_graph_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


