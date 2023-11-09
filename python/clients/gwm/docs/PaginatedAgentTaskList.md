# PaginatedAgentTaskList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AgentTask]**](AgentTask.md) |  | [optional] 

## Example

```python
from gwm_client.models.paginated_agent_task_list import PaginatedAgentTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentTaskList from a JSON string
paginated_agent_task_list_instance = PaginatedAgentTaskList.from_json(json)
# print the JSON string representation of the object
print PaginatedAgentTaskList.to_json()

# convert the object into a dict
paginated_agent_task_list_dict = paginated_agent_task_list_instance.to_dict()
# create an instance of PaginatedAgentTaskList from a dict
paginated_agent_task_list_form_dict = paginated_agent_task_list.from_dict(paginated_agent_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


