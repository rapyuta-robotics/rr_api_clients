# ErrorActionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**description** | **str** | A description of what this error action does | 
**var_schema** | **Dict[str, object]** | Schema description for the meta_data using (http://json-schema.org/learn/getting-started-step-by-step) | 
**auto_recovery_action_schema** | **Dict[str, object]** | Schema description for the auto recovery action content using (http://json-schema.org/learn/getting-started-step-by-step) | [optional] 

## Example

```python
from io_amr_gwm.models.error_action_request import ErrorActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorActionRequest from a JSON string
error_action_request_instance = ErrorActionRequest.from_json(json)
# print the JSON string representation of the object
print ErrorActionRequest.to_json()

# convert the object into a dict
error_action_request_dict = error_action_request_instance.to_dict()
# create an instance of ErrorActionRequest from a dict
error_action_request_form_dict = error_action_request.from_dict(error_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


