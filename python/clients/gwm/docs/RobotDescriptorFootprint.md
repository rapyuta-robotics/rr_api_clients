# RobotDescriptorFootprint

GIS polygon representing this 2D area on the map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Polygon']
**coordinates** | **List[List[List[float]]]** |  | 

## Example

```python
from gwm_client.models.robot_descriptor_footprint import RobotDescriptorFootprint

# TODO update the JSON string below
json = "{}"
# create an instance of RobotDescriptorFootprint from a JSON string
robot_descriptor_footprint_instance = RobotDescriptorFootprint.from_json(json)
# print the JSON string representation of the object
print RobotDescriptorFootprint.to_json()

# convert the object into a dict
robot_descriptor_footprint_dict = robot_descriptor_footprint_instance.to_dict()
# create an instance of RobotDescriptorFootprint from a dict
robot_descriptor_footprint_form_dict = robot_descriptor_footprint.from_dict(robot_descriptor_footprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


