# PatchedExternalDeviceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**spots** | **List[int]** | List of spots the external device is connected to | [optional] 
**regions** | **List[int]** | List of regions the external device is connected to | [optional] 
**version** | **int** | System generated monotonic integer that is updated for each mutation to spots or regions associated with external device | [optional] 

## Example

```python
from gwm_client.models.patched_external_device_request import PatchedExternalDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedExternalDeviceRequest from a JSON string
patched_external_device_request_instance = PatchedExternalDeviceRequest.from_json(json)
# print the JSON string representation of the object
print PatchedExternalDeviceRequest.to_json()

# convert the object into a dict
patched_external_device_request_dict = patched_external_device_request_instance.to_dict()
# create an instance of PatchedExternalDeviceRequest from a dict
patched_external_device_request_form_dict = patched_external_device_request.from_dict(patched_external_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


