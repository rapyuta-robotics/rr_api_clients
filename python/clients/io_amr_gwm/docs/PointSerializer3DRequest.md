# PointSerializer3DRequest

3D GIS point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from io_amr_gwm.models.point_serializer3_d_request import PointSerializer3DRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PointSerializer3DRequest from a JSON string
point_serializer3_d_request_instance = PointSerializer3DRequest.from_json(json)
# print the JSON string representation of the object
print PointSerializer3DRequest.to_json()

# convert the object into a dict
point_serializer3_d_request_dict = point_serializer3_d_request_instance.to_dict()
# create an instance of PointSerializer3DRequest from a dict
point_serializer3_d_request_form_dict = point_serializer3_d_request.from_dict(point_serializer3_d_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


