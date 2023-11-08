# EdgeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**directed** | **bool** | If True, edge direction is from node1 to node2 | [optional] [default to False]
**node1** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**node2** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**speed_scale_estimate** | **float** |  | [optional] 
**preserve** | **bool** | If True, edge is excluded from deletion, unless deleted by force | [optional] 

## Example

```python
from openapi_client.models.edge_request import EdgeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRequest from a JSON string
edge_request_instance = EdgeRequest.from_json(json)
# print the JSON string representation of the object
print EdgeRequest.to_json()

# convert the object into a dict
edge_request_dict = edge_request_instance.to_dict()
# create an instance of EdgeRequest from a dict
edge_request_form_dict = edge_request.from_dict(edge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


