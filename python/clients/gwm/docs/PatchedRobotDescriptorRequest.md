# PatchedRobotDescriptorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | Name of the robot | [optional] 
**type** | **str** | Type of robot  * &#x60;AMR&#x60; - Amr * &#x60;FORKLIFT&#x60; - Forklift | [optional] 
**vendor** | **str** | Name of system vendor | [optional] 
**model** | **str** |  | [optional] 
**io_project_id** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**footprint** | [**PatchedRobotDescriptorRequestFootprint**](PatchedRobotDescriptorRequestFootprint.md) |  | [optional] 
**workflows** | **Dict[str, object]** |  | [optional] 
**critical_battery_level** | **float** | Battery level under which a robot have to go to charge in % | [optional] 
**chargeable_battery_level** | **float** | Battery level under which a robot can be sent to charge in % | [optional] 
**minimum_charge_differential** | **float** | Minimum battery amount in % that robot needs to charge before stopping charging | [optional] 
**minimum_fleet_availability** | **float** | Robot fleet part that needs to be available at a given time in % | [optional] 

## Example

```python
from gwm_client.models.patched_robot_descriptor_request import PatchedRobotDescriptorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRobotDescriptorRequest from a JSON string
patched_robot_descriptor_request_instance = PatchedRobotDescriptorRequest.from_json(json)
# print the JSON string representation of the object
print PatchedRobotDescriptorRequest.to_json()

# convert the object into a dict
patched_robot_descriptor_request_dict = patched_robot_descriptor_request_instance.to_dict()
# create an instance of PatchedRobotDescriptorRequest from a dict
patched_robot_descriptor_request_form_dict = patched_robot_descriptor_request.from_dict(patched_robot_descriptor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


