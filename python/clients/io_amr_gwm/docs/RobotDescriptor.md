# RobotDescriptor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | Name of the robot | 
**type** | **str** | Type of robot  * &#x60;AMR&#x60; - Amr * &#x60;FORKLIFT&#x60; - Forklift | [optional] 
**vendor** | **str** | Name of system vendor | 
**model** | **str** |  | 
**io_project_id** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**footprint** | [**RobotDescriptorFootprint**](RobotDescriptorFootprint.md) |  | [optional] 
**workflows** | **Dict[str, object]** |  | [optional] 
**critical_battery_level** | **float** | Battery level under which a robot have to go to charge in % | [optional] 
**chargeable_battery_level** | **float** | Battery level under which a robot can be sent to charge in % | [optional] 
**minimum_charge_differential** | **float** | Minimum battery amount in % that robot needs to charge before stopping charging | [optional] 
**minimum_fleet_availability** | **float** | Robot fleet part that needs to be available at a given time in % | [optional] 

## Example

```python
from io_amr_gwm.models.robot_descriptor import RobotDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of RobotDescriptor from a JSON string
robot_descriptor_instance = RobotDescriptor.from_json(json)
# print the JSON string representation of the object
print RobotDescriptor.to_json()

# convert the object into a dict
robot_descriptor_dict = robot_descriptor_instance.to_dict()
# create an instance of RobotDescriptor from a dict
robot_descriptor_form_dict = robot_descriptor.from_dict(robot_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


