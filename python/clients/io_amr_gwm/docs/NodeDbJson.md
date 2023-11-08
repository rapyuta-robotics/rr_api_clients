# NodeDbJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**pos** | **Dict[str, object]** |  | [readonly] 
**radius** | **float** | Node radius | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**parkable** | **bool** |  | [optional] 
**preserve** | **bool** | If True, node is excluded from deletion, unless deleted by force | [optional] 
**type** | **str** | User defined node type | [optional] 
**map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [readonly] 

## Example

```python
from io_amr_gwm.models.node_db_json import NodeDbJson

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDbJson from a JSON string
node_db_json_instance = NodeDbJson.from_json(json)
# print the JSON string representation of the object
print NodeDbJson.to_json()

# convert the object into a dict
node_db_json_dict = node_db_json_instance.to_dict()
# create an instance of NodeDbJson from a dict
node_db_json_form_dict = node_db_json.from_dict(node_db_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


