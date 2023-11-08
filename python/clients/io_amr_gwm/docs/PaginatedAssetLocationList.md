# PaginatedAssetLocationList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AssetLocation]**](AssetLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.paginated_asset_location_list import PaginatedAssetLocationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetLocationList from a JSON string
paginated_asset_location_list_instance = PaginatedAssetLocationList.from_json(json)
# print the JSON string representation of the object
print PaginatedAssetLocationList.to_json()

# convert the object into a dict
paginated_asset_location_list_dict = paginated_asset_location_list_instance.to_dict()
# create an instance of PaginatedAssetLocationList from a dict
paginated_asset_location_list_form_dict = paginated_asset_location_list.from_dict(paginated_asset_location_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


