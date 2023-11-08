# NodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**pos** | [**PointRequest**](PointRequest.md) |  | 
**radius** | **float** | Node radius | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**parkable** | **bool** |  | [optional] 
**preserve** | **bool** | If True, node is excluded from deletion, unless deleted by force | [optional] 
**type** | **str** | User defined node type | [optional] 

## Example

```python
from io_amr_gwm.models.node_request import NodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeRequest from a JSON string
node_request_instance = NodeRequest.from_json(json)
# print the JSON string representation of the object
print NodeRequest.to_json()

# convert the object into a dict
node_request_dict = node_request_instance.to_dict()
# create an instance of NodeRequest from a dict
node_request_form_dict = node_request.from_dict(node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


