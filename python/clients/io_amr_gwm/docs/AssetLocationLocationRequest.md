# AssetLocationLocationRequest

TODO: support thing other than spot, merge with libs.location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;spot&#x60; - Spot * &#x60;spot_query&#x60; - Spot Query | 
**id** | **int** |  | 

## Example

```python
from openapi_client.models.asset_location_location_request import AssetLocationLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLocationLocationRequest from a JSON string
asset_location_location_request_instance = AssetLocationLocationRequest.from_json(json)
# print the JSON string representation of the object
print AssetLocationLocationRequest.to_json()

# convert the object into a dict
asset_location_location_request_dict = asset_location_location_request_instance.to_dict()
# create an instance of AssetLocationLocationRequest from a dict
asset_location_location_request_form_dict = asset_location_location_request.from_dict(asset_location_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


