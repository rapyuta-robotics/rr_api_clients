# PointSerializer3D

3D GIS point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from io_amr_gwm.models.point_serializer3_d import PointSerializer3D

# TODO update the JSON string below
json = "{}"
# create an instance of PointSerializer3D from a JSON string
point_serializer3_d_instance = PointSerializer3D.from_json(json)
# print the JSON string representation of the object
print PointSerializer3D.to_json()

# convert the object into a dict
point_serializer3_d_dict = point_serializer3_d_instance.to_dict()
# create an instance of PointSerializer3D from a dict
point_serializer3_d_form_dict = point_serializer3_d.from_dict(point_serializer3_d_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


