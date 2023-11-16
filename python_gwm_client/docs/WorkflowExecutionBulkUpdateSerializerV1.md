# WorkflowExecutionBulkUpdateSerializerV1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** | The workflow type. | [readonly] 
**status** | **str** | Status of the workflow execution.  * &#x60;PENDING&#x60; - Pending * &#x60;RUNNING&#x60; - Running * &#x60;COMPLETED&#x60; - Completed * &#x60;FAILED&#x60; - Failed * &#x60;CANCELED&#x60; - Canceled * &#x60;TERMINATED&#x60; - Terminated * &#x60;CONTINUED_AS_NEW&#x60; - Continued as new * &#x60;TIMED_OUT&#x60; - Timed out | [optional] 
**data** | **Dict[str, object]** | The workflow execution input data. | [readonly] 
**result** | **Dict[str, object]** | The workflow execution result. | [optional] 
**context** | **Dict[str, object]** | The workflow execution context. | [optional] 
**start_time** | **datetime** | Timestamp of when the workflow execution was started. | [readonly] 
**end_time** | **datetime** | Timestamp of when the workflow execution was ended. | [readonly] 
**insert_time** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**update_time** | **datetime** | Timestamp of when the resource was last modified. | [readonly] 

## Example

```python
from gwm_client.models.workflow_execution_bulk_update_serializer_v1 import WorkflowExecutionBulkUpdateSerializerV1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionBulkUpdateSerializerV1 from a JSON string
workflow_execution_bulk_update_serializer_v1_instance = WorkflowExecutionBulkUpdateSerializerV1.from_json(json)
# print the JSON string representation of the object
print WorkflowExecutionBulkUpdateSerializerV1.to_json()

# convert the object into a dict
workflow_execution_bulk_update_serializer_v1_dict = workflow_execution_bulk_update_serializer_v1_instance.to_dict()
# create an instance of WorkflowExecutionBulkUpdateSerializerV1 from a dict
workflow_execution_bulk_update_serializer_v1_form_dict = workflow_execution_bulk_update_serializer_v1.from_dict(workflow_execution_bulk_update_serializer_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


