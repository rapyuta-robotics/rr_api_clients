# PaginatedWorkflowExecutionSerializerV1List


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[WorkflowExecutionSerializerV1]**](WorkflowExecutionSerializerV1.md) |  | [optional] 

## Example

```python
from gwm_client.models.paginated_workflow_execution_serializer_v1_list import PaginatedWorkflowExecutionSerializerV1List

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkflowExecutionSerializerV1List from a JSON string
paginated_workflow_execution_serializer_v1_list_instance = PaginatedWorkflowExecutionSerializerV1List.from_json(json)
# print the JSON string representation of the object
print PaginatedWorkflowExecutionSerializerV1List.to_json()

# convert the object into a dict
paginated_workflow_execution_serializer_v1_list_dict = paginated_workflow_execution_serializer_v1_list_instance.to_dict()
# create an instance of PaginatedWorkflowExecutionSerializerV1List from a dict
paginated_workflow_execution_serializer_v1_list_form_dict = paginated_workflow_execution_serializer_v1_list.from_dict(paginated_workflow_execution_serializer_v1_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


