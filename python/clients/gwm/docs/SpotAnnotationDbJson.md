# SpotAnnotationDbJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**pos** | **Dict[str, object]** |  | [readonly] 
**yaw** | **float** | Orientation of spot in radians | 
**nav_pos** | **Dict[str, object]** |  | [readonly] 
**nav_yaw** | **float** | Orientation of navigation position for interacting with the spot | [optional] 
**node** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**type** | **str** | User defined spot type | [optional] 
**external_device** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**allocatable** | **bool** | If True, spot can be allocated in response to agent queries | [optional] 
**preserve** | **bool** | If True, spot is excluded from deletion, unless deleted by force | [optional] 
**priority** | **int** | Associate a priority to the spot, e.g. for spot queries to allocatable spots | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm.models.spot_annotation_db_json import SpotAnnotationDbJson

# TODO update the JSON string below
json = "{}"
# create an instance of SpotAnnotationDbJson from a JSON string
spot_annotation_db_json_instance = SpotAnnotationDbJson.from_json(json)
# print the JSON string representation of the object
print SpotAnnotationDbJson.to_json()

# convert the object into a dict
spot_annotation_db_json_dict = spot_annotation_db_json_instance.to_dict()
# create an instance of SpotAnnotationDbJson from a dict
spot_annotation_db_json_form_dict = spot_annotation_db_json.from_dict(spot_annotation_db_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


