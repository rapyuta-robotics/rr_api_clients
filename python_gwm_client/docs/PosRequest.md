# PosRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos** | [**PosPointRequest**](PosPointRequest.md) |  | [optional] 
**yaw** | **float** |  | [optional] 
**map** | **Dict[str, object]** |  | [optional] 

## Example

```python
from gwm_client.models.pos_request import PosRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PosRequest from a JSON string
pos_request_instance = PosRequest.from_json(json)
# print the JSON string representation of the object
print PosRequest.to_json()

# convert the object into a dict
pos_request_dict = pos_request_instance.to_dict()
# create an instance of PosRequest from a dict
pos_request_form_dict = pos_request.from_dict(pos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


