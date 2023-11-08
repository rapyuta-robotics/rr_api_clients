# PaginatedAgentTaskFragmentList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AgentTaskFragment]**](AgentTaskFragment.md) |  | [optional] 

## Example

```python
from io_amr_gwm.models.paginated_agent_task_fragment_list import PaginatedAgentTaskFragmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentTaskFragmentList from a JSON string
paginated_agent_task_fragment_list_instance = PaginatedAgentTaskFragmentList.from_json(json)
# print the JSON string representation of the object
print PaginatedAgentTaskFragmentList.to_json()

# convert the object into a dict
paginated_agent_task_fragment_list_dict = paginated_agent_task_fragment_list_instance.to_dict()
# create an instance of PaginatedAgentTaskFragmentList from a dict
paginated_agent_task_fragment_list_form_dict = paginated_agent_task_fragment_list.from_dict(paginated_agent_task_fragment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


