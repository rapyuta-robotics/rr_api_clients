# AssetLocationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 
**asset** | [**AssetRequest**](AssetRequest.md) |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**location** | [**AssetLocationLocationRequest**](AssetLocationLocationRequest.md) |  | 
**type** | **str** | User defined asset location type | [optional] 
**index** | **int** | Unique per spot if present | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_location_request import AssetLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssetLocationRequest from a JSON string
asset_location_request_instance = AssetLocationRequest.from_json(json)
# print the JSON string representation of the object
print AssetLocationRequest.to_json()

# convert the object into a dict
asset_location_request_dict = asset_location_request_instance.to_dict()
# create an instance of AssetLocationRequest from a dict
asset_location_request_form_dict = asset_location_request.from_dict(asset_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


