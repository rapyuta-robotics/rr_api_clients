# WorkflowExecutionSerializerV1Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The workflow type. | 
**data** | **Dict[str, object]** | The workflow execution input data. | 
**context** | **Dict[str, object]** | The workflow execution context. | [optional] 

## Example

```python
from gwm_client.models.workflow_execution_serializer_v1_request import WorkflowExecutionSerializerV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionSerializerV1Request from a JSON string
workflow_execution_serializer_v1_request_instance = WorkflowExecutionSerializerV1Request.from_json(json)
# print the JSON string representation of the object
print WorkflowExecutionSerializerV1Request.to_json()

# convert the object into a dict
workflow_execution_serializer_v1_request_dict = workflow_execution_serializer_v1_request_instance.to_dict()
# create an instance of WorkflowExecutionSerializerV1Request from a dict
workflow_execution_serializer_v1_request_form_dict = workflow_execution_serializer_v1_request.from_dict(workflow_execution_serializer_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


