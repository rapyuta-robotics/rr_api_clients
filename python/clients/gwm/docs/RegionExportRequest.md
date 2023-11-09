# RegionExportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**geom** | [**PolygonRequest**](PolygonRequest.md) |  | 
**external_device** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**meta_data** | **Dict[str, object]** |  | [optional] 
**type** | **str** | User defined type of polygon | [optional] 

## Example

```python
from gwm_client.models.region_export_request import RegionExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegionExportRequest from a JSON string
region_export_request_instance = RegionExportRequest.from_json(json)
# print the JSON string representation of the object
print RegionExportRequest.to_json()

# convert the object into a dict
region_export_request_dict = region_export_request_instance.to_dict()
# create an instance of RegionExportRequest from a dict
region_export_request_form_dict = region_export_request.from_dict(region_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


