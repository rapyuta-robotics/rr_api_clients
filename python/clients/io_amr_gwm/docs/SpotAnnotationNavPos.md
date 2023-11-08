# SpotAnnotationNavPos

Position for the robot to navigate to interact with the spot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from openapi_client.models.spot_annotation_nav_pos import SpotAnnotationNavPos

# TODO update the JSON string below
json = "{}"
# create an instance of SpotAnnotationNavPos from a JSON string
spot_annotation_nav_pos_instance = SpotAnnotationNavPos.from_json(json)
# print the JSON string representation of the object
print SpotAnnotationNavPos.to_json()

# convert the object into a dict
spot_annotation_nav_pos_dict = spot_annotation_nav_pos_instance.to_dict()
# create an instance of SpotAnnotationNavPos from a dict
spot_annotation_nav_pos_form_dict = spot_annotation_nav_pos.from_dict(spot_annotation_nav_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


