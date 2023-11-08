# PatchedRobotDescriptorRequestFootprint

GIS polygon representing this 2D area on the map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Polygon']
**coordinates** | **List[List[List[float]]]** |  | 

## Example

```python
from io_amr_gwm.models.patched_robot_descriptor_request_footprint import PatchedRobotDescriptorRequestFootprint

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRobotDescriptorRequestFootprint from a JSON string
patched_robot_descriptor_request_footprint_instance = PatchedRobotDescriptorRequestFootprint.from_json(json)
# print the JSON string representation of the object
print PatchedRobotDescriptorRequestFootprint.to_json()

# convert the object into a dict
patched_robot_descriptor_request_footprint_dict = patched_robot_descriptor_request_footprint_instance.to_dict()
# create an instance of PatchedRobotDescriptorRequestFootprint from a dict
patched_robot_descriptor_request_footprint_form_dict = patched_robot_descriptor_request_footprint.from_dict(patched_robot_descriptor_request_footprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


