# PointRequest

2D GIS Point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from io_amr_gwm.models.point_request import PointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PointRequest from a JSON string
point_request_instance = PointRequest.from_json(json)
# print the JSON string representation of the object
print PointRequest.to_json()

# convert the object into a dict
point_request_dict = point_request_instance.to_dict()
# create an instance of PointRequest from a dict
point_request_form_dict = point_request.from_dict(point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


