# InternalWorkPayloadFragmentToPos

Desired X,Y position agent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** |  | 
**type** | **str** |  | [optional] [default to 'Point']

## Example

```python
from gwm_client.models.internal_work_payload_fragment_to_pos import InternalWorkPayloadFragmentToPos

# TODO update the JSON string below
json = "{}"
# create an instance of InternalWorkPayloadFragmentToPos from a JSON string
internal_work_payload_fragment_to_pos_instance = InternalWorkPayloadFragmentToPos.from_json(json)
# print the JSON string representation of the object
print InternalWorkPayloadFragmentToPos.to_json()

# convert the object into a dict
internal_work_payload_fragment_to_pos_dict = internal_work_payload_fragment_to_pos_instance.to_dict()
# create an instance of InternalWorkPayloadFragmentToPos from a dict
internal_work_payload_fragment_to_pos_form_dict = internal_work_payload_fragment_to_pos.from_dict(internal_work_payload_fragment_to_pos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


