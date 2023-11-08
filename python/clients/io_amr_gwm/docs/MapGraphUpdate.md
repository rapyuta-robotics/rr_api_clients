# MapGraphUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**created_at** | **datetime** | Timestamp at which this map was created | [readonly] 
**floor** | **int** | Floor of the site this map corresponds to | [optional] 
**graph_version** | **int** | System generated monotonic integer that is updated for each mutation to nodes or edges  | [readonly] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from openapi_client.models.map_graph_update import MapGraphUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MapGraphUpdate from a JSON string
map_graph_update_instance = MapGraphUpdate.from_json(json)
# print the JSON string representation of the object
print MapGraphUpdate.to_json()

# convert the object into a dict
map_graph_update_dict = map_graph_update_instance.to_dict()
# create an instance of MapGraphUpdate from a dict
map_graph_update_form_dict = map_graph_update.from_dict(map_graph_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


