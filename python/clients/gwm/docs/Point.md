# Point

2D GIS Point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from gwm.models.point import Point

# TODO update the JSON string below
json = "{}"
# create an instance of Point from a JSON string
point_instance = Point.from_json(json)
# print the JSON string representation of the object
print Point.to_json()

# convert the object into a dict
point_dict = point_instance.to_dict()
# create an instance of Point from a dict
point_form_dict = point.from_dict(point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


