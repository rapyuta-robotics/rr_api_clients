# PatchedNodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**pos** | [**PointRequest**](PointRequest.md) |  | [optional] 
**radius** | **float** | Node radius | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**parkable** | **bool** |  | [optional] 
**preserve** | **bool** | If True, node is excluded from deletion, unless deleted by force | [optional] 
**type** | **str** | User defined node type | [optional] 

## Example

```python
from gwm.models.patched_node_request import PatchedNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNodeRequest from a JSON string
patched_node_request_instance = PatchedNodeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedNodeRequest.to_json()

# convert the object into a dict
patched_node_request_dict = patched_node_request_instance.to_dict()
# create an instance of PatchedNodeRequest from a dict
patched_node_request_form_dict = patched_node_request.from_dict(patched_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


