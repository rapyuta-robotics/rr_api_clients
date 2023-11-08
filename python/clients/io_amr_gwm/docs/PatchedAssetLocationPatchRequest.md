# PatchedAssetLocationPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from io_amr_gwm.models.patched_asset_location_patch_request import PatchedAssetLocationPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAssetLocationPatchRequest from a JSON string
patched_asset_location_patch_request_instance = PatchedAssetLocationPatchRequest.from_json(json)
# print the JSON string representation of the object
print PatchedAssetLocationPatchRequest.to_json()

# convert the object into a dict
patched_asset_location_patch_request_dict = patched_asset_location_patch_request_instance.to_dict()
# create an instance of PatchedAssetLocationPatchRequest from a dict
patched_asset_location_patch_request_form_dict = patched_asset_location_patch_request.from_dict(patched_asset_location_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


