# WorkflowExecutionUpdateSerializerV1Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the workflow execution.  * &#x60;PENDING&#x60; - Pending * &#x60;RUNNING&#x60; - Running * &#x60;COMPLETED&#x60; - Completed * &#x60;FAILED&#x60; - Failed * &#x60;CANCELED&#x60; - Canceled * &#x60;TERMINATED&#x60; - Terminated * &#x60;CONTINUED_AS_NEW&#x60; - Continued as new * &#x60;TIMED_OUT&#x60; - Timed out | [optional] 
**result** | **Dict[str, object]** | The workflow execution result. | [optional] 
**context** | **Dict[str, object]** | The workflow execution context. | [optional] 

## Example

```python
from gwm_client.models.workflow_execution_update_serializer_v1_request import WorkflowExecutionUpdateSerializerV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionUpdateSerializerV1Request from a JSON string
workflow_execution_update_serializer_v1_request_instance = WorkflowExecutionUpdateSerializerV1Request.from_json(json)
# print the JSON string representation of the object
print WorkflowExecutionUpdateSerializerV1Request.to_json()

# convert the object into a dict
workflow_execution_update_serializer_v1_request_dict = workflow_execution_update_serializer_v1_request_instance.to_dict()
# create an instance of WorkflowExecutionUpdateSerializerV1Request from a dict
workflow_execution_update_serializer_v1_request_form_dict = workflow_execution_update_serializer_v1_request.from_dict(workflow_execution_update_serializer_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


