# Robot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | Name of the robot | 
**io_device_id** | **str** |  | [optional] 
**io_project_id** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | 
**robot_descriptor** | **int** | &#x60;id&#x60; of relevant related element eg: agent,map,site,spot,node,edge,external_device | 
**ip_address** | **str** | IP address of the robot  | [optional] 
**current_mode** | **str** | The current state of the robot   * &#x60;MAPPING&#x60; - Mapping * &#x60;NORMAL&#x60; - Normal | [optional] 
**requested_mode** | **str** | The requested state of the robot  * &#x60;MAPPING&#x60; - Mapping * &#x60;NORMAL&#x60; - Normal | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm_client.models.robot import Robot

# TODO update the JSON string below
json = "{}"
# create an instance of Robot from a JSON string
robot_instance = Robot.from_json(json)
# print the JSON string representation of the object
print Robot.to_json()

# convert the object into a dict
robot_dict = robot_instance.to_dict()
# create an instance of Robot from a dict
robot_form_dict = robot.from_dict(robot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


