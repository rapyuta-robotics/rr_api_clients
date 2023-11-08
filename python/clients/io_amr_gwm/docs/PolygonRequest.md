# PolygonRequest

GIS Polygon - (representation of polygon with 1 or more LinearRings)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Polygon']
**coordinates** | **List[List[List[float]]]** |  | 

## Example

```python
from io_amr_gwm.models.polygon_request import PolygonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonRequest from a JSON string
polygon_request_instance = PolygonRequest.from_json(json)
# print the JSON string representation of the object
print PolygonRequest.to_json()

# convert the object into a dict
polygon_request_dict = polygon_request_instance.to_dict()
# create an instance of PolygonRequest from a dict
polygon_request_form_dict = polygon_request.from_dict(polygon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


