# LocationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | * &#x60;spot&#x60; - Spot * &#x60;spot_query&#x60; - Spot Query | [optional] [default to 'spot_query']
**spot_query** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.location_request import LocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationRequest from a JSON string
location_request_instance = LocationRequest.from_json(json)
# print the JSON string representation of the object
print LocationRequest.to_json()

# convert the object into a dict
location_request_dict = location_request_instance.to_dict()
# create an instance of LocationRequest from a dict
location_request_form_dict = location_request.from_dict(location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


