# MapRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**floor** | **int** | Floor of the site this map corresponds to | [optional] 
**warnings** | **List[object]** |  | [optional] 
**num_layers** | **int** |  | [optional] 
**graph_version** | **int** | System generated monotonic integer that is updated for each mutation to nodes or edges  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from io_amr_gwm.models.map_request import MapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapRequest from a JSON string
map_request_instance = MapRequest.from_json(json)
# print the JSON string representation of the object
print MapRequest.to_json()

# convert the object into a dict
map_request_dict = map_request_instance.to_dict()
# create an instance of MapRequest from a dict
map_request_form_dict = map_request.from_dict(map_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


