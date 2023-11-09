# Site


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | type fo site (e.g. warehouse) | [optional] 
**endpoint** | **str** |  | [readonly] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**created_at** | **datetime** | Timestamp at which this site was created | [readonly] 

## Example

```python
from gwm_client.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print Site.to_json()

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_form_dict = site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


