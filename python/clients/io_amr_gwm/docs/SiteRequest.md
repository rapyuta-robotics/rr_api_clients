# SiteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | type fo site (e.g. warehouse) | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from io_amr_gwm.models.site_request import SiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRequest from a JSON string
site_request_instance = SiteRequest.from_json(json)
# print the JSON string representation of the object
print SiteRequest.to_json()

# convert the object into a dict
site_request_dict = site_request_instance.to_dict()
# create an instance of SiteRequest from a dict
site_request_form_dict = site_request.from_dict(site_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


