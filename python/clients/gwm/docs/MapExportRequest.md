# MapExportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**floor** | **int** | Floor of the site this map corresponds to | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**layers** | [**List[LayerRequest]**](LayerRequest.md) |  | [optional] 
**nodes** | [**List[NodeRequest]**](NodeRequest.md) |  | [optional] 
**regions** | [**List[RegionExportRequest]**](RegionExportRequest.md) |  | [optional] 
**edges** | [**List[EdgeRequest]**](EdgeRequest.md) |  | [optional] 
**spots** | [**List[SpotAnnotationExportRequest]**](SpotAnnotationExportRequest.md) |  | [optional] 
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 

## Example

```python
from gwm.models.map_export_request import MapExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapExportRequest from a JSON string
map_export_request_instance = MapExportRequest.from_json(json)
# print the JSON string representation of the object
print MapExportRequest.to_json()

# convert the object into a dict
map_export_request_dict = map_export_request_instance.to_dict()
# create an instance of MapExportRequest from a dict
map_export_request_form_dict = map_export_request.from_dict(map_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


