# PatchedSpotAnnotationUpdateRequestNavPos

Position for the robot to navigate to interact with the spot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from gwm_client.models.patched_spot_annotation_update_request_nav_pos import PatchedSpotAnnotationUpdateRequestNavPos

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSpotAnnotationUpdateRequestNavPos from a JSON string
patched_spot_annotation_update_request_nav_pos_instance = PatchedSpotAnnotationUpdateRequestNavPos.from_json(json)
# print the JSON string representation of the object
print PatchedSpotAnnotationUpdateRequestNavPos.to_json()

# convert the object into a dict
patched_spot_annotation_update_request_nav_pos_dict = patched_spot_annotation_update_request_nav_pos_instance.to_dict()
# create an instance of PatchedSpotAnnotationUpdateRequestNavPos from a dict
patched_spot_annotation_update_request_nav_pos_form_dict = patched_spot_annotation_update_request_nav_pos.from_dict(patched_spot_annotation_update_request_nav_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


