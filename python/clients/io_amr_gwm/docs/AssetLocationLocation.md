# AssetLocationLocation

TODO: support thing other than spot, merge with libs.location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;spot&#x60; - Spot * &#x60;spot_query&#x60; - Spot Query | 
**id** | **int** |  | 

## Example

```python
from openapi_client.models.asset_location_location import AssetLocationLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLocationLocation from a JSON string
asset_location_location_instance = AssetLocationLocation.from_json(json)
# print the JSON string representation of the object
print AssetLocationLocation.to_json()

# convert the object into a dict
asset_location_location_dict = asset_location_location_instance.to_dict()
# create an instance of AssetLocationLocation from a dict
asset_location_location_form_dict = asset_location_location.from_dict(asset_location_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


