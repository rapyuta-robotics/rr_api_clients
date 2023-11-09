# PatchedSpotAnnotationUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**node** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**type** | **str** | User defined spot type | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**external_device** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**allocatable** | **bool** | If True, spot can be allocated in response to agent queries | [optional] 
**preserve** | **bool** | If True, spot is excluded from deletion, unless deleted by force | [optional] 
**priority** | **int** | Associate a priority to the spot, e.g. for spot queries to allocatable spots | [optional] 
**pos** | [**PointSerializer3DRequest**](PointSerializer3DRequest.md) |  | [optional] 
**yaw** | **float** | Orientation of spot in radians | [optional] 
**nav_pos** | [**PatchedSpotAnnotationUpdateRequestNavPos**](PatchedSpotAnnotationUpdateRequestNavPos.md) |  | [optional] 
**nav_yaw** | **float** | Orientation of navigation position for interacting with the spot | [optional] 

## Example

```python
from gwm.models.patched_spot_annotation_update_request import PatchedSpotAnnotationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSpotAnnotationUpdateRequest from a JSON string
patched_spot_annotation_update_request_instance = PatchedSpotAnnotationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PatchedSpotAnnotationUpdateRequest.to_json()

# convert the object into a dict
patched_spot_annotation_update_request_dict = patched_spot_annotation_update_request_instance.to_dict()
# create an instance of PatchedSpotAnnotationUpdateRequest from a dict
patched_spot_annotation_update_request_form_dict = patched_spot_annotation_update_request.from_dict(patched_spot_annotation_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

