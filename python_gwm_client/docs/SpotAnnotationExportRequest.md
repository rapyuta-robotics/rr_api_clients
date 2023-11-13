# SpotAnnotationExportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pos** | [**PointSerializer3DRequest**](PointSerializer3DRequest.md) |  | 
**yaw** | **float** | Orientation of spot in radians | 
**node** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**allocatable** | **bool** | If True, spot can be allocated in response to agent queries | [optional] 
**priority** | **int** | Associate a priority to the spot, e.g. for spot queries to allocatable spots | [optional] 
**type** | **str** | User defined spot type | [optional] 
**external_device** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**nav_pos** | [**PatchedSpotAnnotationUpdateRequestNavPos**](PatchedSpotAnnotationUpdateRequestNavPos.md) |  | [optional] 
**nav_yaw** | **float** | Orientation of navigation position for interacting with the spot | [optional] 
**preserve** | **bool** | If True, spot is excluded from deletion, unless deleted by force | [optional] 

## Example

```python
from gwm_client.models.spot_annotation_export_request import SpotAnnotationExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpotAnnotationExportRequest from a JSON string
spot_annotation_export_request_instance = SpotAnnotationExportRequest.from_json(json)
# print the JSON string representation of the object
print SpotAnnotationExportRequest.to_json()

# convert the object into a dict
spot_annotation_export_request_dict = spot_annotation_export_request_instance.to_dict()
# create an instance of SpotAnnotationExportRequest from a dict
spot_annotation_export_request_form_dict = spot_annotation_export_request.from_dict(spot_annotation_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


