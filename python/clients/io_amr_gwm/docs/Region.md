# Region


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**geom** | [**Polygon**](Polygon.md) |  | 
**external_device** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | [optional] 
**map** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**meta_data** | **Dict[str, object]** |  | [optional] 
**type** | **str** | User defined type of polygon | [optional] 
**preserve** | **bool** | If True, region is excluded from deletion, unless deleted by force | [optional] 

## Example

```python
from io_amr_gwm.models.region import Region

# TODO update the JSON string below
json = "{}"
# create an instance of Region from a JSON string
region_instance = Region.from_json(json)
# print the JSON string representation of the object
print Region.to_json()

# convert the object into a dict
region_dict = region_instance.to_dict()
# create an instance of Region from a dict
region_form_dict = region.from_dict(region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


