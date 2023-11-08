# AssetLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**modified** | **datetime** |  | [readonly] 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**asset** | [**Asset**](Asset.md) |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**location** | [**AssetLocationLocation**](AssetLocationLocation.md) |  | 
**type** | **str** | User defined asset location type | [optional] 
**index** | **int** | Unique per spot if present | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from io_amr_gwm.models.asset_location import AssetLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLocation from a JSON string
asset_location_instance = AssetLocation.from_json(json)
# print the JSON string representation of the object
print AssetLocation.to_json()

# convert the object into a dict
asset_location_dict = asset_location_instance.to_dict()
# create an instance of AssetLocation from a dict
asset_location_form_dict = asset_location.from_dict(asset_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


