# InternalWorkPayloadFragmentRequestToPos

Desired X,Y position agent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from openapi_client.models.internal_work_payload_fragment_request_to_pos import InternalWorkPayloadFragmentRequestToPos

# TODO update the JSON string below
json = "{}"
# create an instance of InternalWorkPayloadFragmentRequestToPos from a JSON string
internal_work_payload_fragment_request_to_pos_instance = InternalWorkPayloadFragmentRequestToPos.from_json(json)
# print the JSON string representation of the object
print InternalWorkPayloadFragmentRequestToPos.to_json()

# convert the object into a dict
internal_work_payload_fragment_request_to_pos_dict = internal_work_payload_fragment_request_to_pos_instance.to_dict()
# create an instance of InternalWorkPayloadFragmentRequestToPos from a dict
internal_work_payload_fragment_request_to_pos_form_dict = internal_work_payload_fragment_request_to_pos.from_dict(internal_work_payload_fragment_request_to_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


