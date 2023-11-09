# PatchedErrorTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**local_error_code** | **int** | This is the internal error code that io amr uses ; each corresponds to a specific failure condition | [optional] 
**reporting_component** | **str** | This is the reporting_component of the error | [optional] 
**global_error_code** | **int** | This is the global error code that the customer assigns  | [optional] 
**criticality** | **int** | Severity of the error  * &#x60;1&#x60; - Warning * &#x60;2&#x60; - Error * &#x60;3&#x60; - Ignore | [optional] 
**clearing_options** | **List[object]** |  | [optional] 
**auto_recovery_actions** | [**List[AutoRecoveryActionRequest]**](AutoRecoveryActionRequest.md) |  | [optional] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 

## Example

```python
from gwm.models.patched_error_type_request import PatchedErrorTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedErrorTypeRequest from a JSON string
patched_error_type_request_instance = PatchedErrorTypeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedErrorTypeRequest.to_json()

# convert the object into a dict
patched_error_type_request_dict = patched_error_type_request_instance.to_dict()
# create an instance of PatchedErrorTypeRequest from a dict
patched_error_type_request_form_dict = patched_error_type_request.from_dict(patched_error_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

