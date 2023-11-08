# AssetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;container&#x60; - Container * &#x60;product&#x60; - Product | 
**id** | **int** |  | 

## Example

```python
from io_amr_gwm.models.asset_request import AssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRequest from a JSON string
asset_request_instance = AssetRequest.from_json(json)
# print the JSON string representation of the object
print AssetRequest.to_json()

# convert the object into a dict
asset_request_dict = asset_request_instance.to_dict()
# create an instance of AssetRequest from a dict
asset_request_form_dict = asset_request.from_dict(asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


