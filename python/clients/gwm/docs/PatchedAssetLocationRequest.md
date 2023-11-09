# PatchedAssetLocationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**asset** | [**AssetRequest**](AssetRequest.md) |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**location** | [**AssetLocationLocationRequest**](AssetLocationLocationRequest.md) |  | [optional] 
**type** | **str** | User defined asset location type | [optional] 
**index** | **int** | Unique per spot if present | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from gwm.models.patched_asset_location_request import PatchedAssetLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAssetLocationRequest from a JSON string
patched_asset_location_request_instance = PatchedAssetLocationRequest.from_json(json)
# print the JSON string representation of the object
print PatchedAssetLocationRequest.to_json()

# convert the object into a dict
patched_asset_location_request_dict = patched_asset_location_request_instance.to_dict()
# create an instance of PatchedAssetLocationRequest from a dict
patched_asset_location_request_form_dict = patched_asset_location_request.from_dict(patched_asset_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


