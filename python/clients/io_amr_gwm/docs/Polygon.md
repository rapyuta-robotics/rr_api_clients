# Polygon

GIS Polygon - (representation of polygon with 1 or more LinearRings)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Polygon']
**coordinates** | **List[List[List[float]]]** |  | 

## Example

```python
from openapi_client.models.polygon import Polygon

# TODO update the JSON string below
json = "{}"
# create an instance of Polygon from a JSON string
polygon_instance = Polygon.from_json(json)
# print the JSON string representation of the object
print Polygon.to_json()

# convert the object into a dict
polygon_dict = polygon_instance.to_dict()
# create an instance of Polygon from a dict
polygon_form_dict = polygon.from_dict(polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


