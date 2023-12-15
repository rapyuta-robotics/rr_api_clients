# PosPointRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'Point']
**coordinates** | **List[float]** |  | 

## Example

```python
from gwm_client.models.pos_point_request import PosPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PosPointRequest from a JSON string
pos_point_request_instance = PosPointRequest.from_json(json)
# print the JSON string representation of the object
print PosPointRequest.to_json()

# convert the object into a dict
pos_point_request_dict = pos_point_request_instance.to_dict()
# create an instance of PosPointRequest from a dict
pos_point_request_form_dict = pos_point_request.from_dict(pos_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


