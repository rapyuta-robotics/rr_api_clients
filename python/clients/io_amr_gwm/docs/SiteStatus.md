# SiteStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type_version** | **int** |  | [readonly] 
**spot_version** | **int** |  | [readonly] 
**region_version** | **int** |  | [readonly] 
**robot_descriptor_version** | **int** |  | [readonly] 
**agent_version** | **int** |  | [readonly] 
**site_version** | **int** |  | [readonly] 
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [readonly] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [readonly] 
**created_at** | **datetime** | Timestamp at which this site was created | [readonly] 
**container_version** | **int** |  | [readonly] 
**container_descriptor_version** | **int** |  | [readonly] 
**product_version** | **int** |  | [readonly] 

## Example

```python
from openapi_client.models.site_status import SiteStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SiteStatus from a JSON string
site_status_instance = SiteStatus.from_json(json)
# print the JSON string representation of the object
print SiteStatus.to_json()

# convert the object into a dict
site_status_dict = site_status_instance.to_dict()
# create an instance of SiteStatus from a dict
site_status_form_dict = site_status.from_dict(site_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


