# Location


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;spot&#x60; - Spot * &#x60;spot_query&#x60; - Spot Query | [optional] [default to 'spot_query']
**spot_query** | **Dict[str, object]** |  | [optional] 

## Example

```python
from gwm_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


