# SiteExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [readonly] 
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | type fo site (e.g. warehouse) | [optional] 

## Example

```python
from io_amr_gwm.models.site_export import SiteExport

# TODO update the JSON string below
json = "{}"
# create an instance of SiteExport from a JSON string
site_export_instance = SiteExport.from_json(json)
# print the JSON string representation of the object
print SiteExport.to_json()

# convert the object into a dict
site_export_dict = site_export_instance.to_dict()
# create an instance of SiteExport from a dict
site_export_form_dict = site_export.from_dict(site_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


