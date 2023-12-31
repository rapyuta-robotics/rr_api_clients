# ExternalDeviceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** |  | 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**spots** | **List[int]** | List of spots the external device is connected to | [optional] 
**regions** | **List[int]** | List of regions the external device is connected to | [optional] 
**version** | **int** | System generated monotonic integer that is updated for each mutation to spots or regions associated with external device | [optional] 

## Example

```python
from gwm_client.models.external_device_request import ExternalDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDeviceRequest from a JSON string
external_device_request_instance = ExternalDeviceRequest.from_json(json)
# print the JSON string representation of the object
print ExternalDeviceRequest.to_json()

# convert the object into a dict
external_device_request_dict = external_device_request_instance.to_dict()
# create an instance of ExternalDeviceRequest from a dict
external_device_request_form_dict = external_device_request.from_dict(external_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


