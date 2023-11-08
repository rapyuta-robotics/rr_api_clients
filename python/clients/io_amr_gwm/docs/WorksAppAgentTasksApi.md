# io_amr_gwm.WorksAppAgentTasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_agent_tasks_bulk_patch_update_partial_update**](WorksAppAgentTasksApi.md#v2_agent_tasks_bulk_patch_update_partial_update) | **PATCH** /v2/agent_tasks/bulk_patch_update | 
[**v2_agent_tasks_clear_all_destroy**](WorksAppAgentTasksApi.md#v2_agent_tasks_clear_all_destroy) | **DELETE** /v2/agent_tasks/clear_all | Clear All Agent Tasks
[**v2_agent_tasks_create**](WorksAppAgentTasksApi.md#v2_agent_tasks_create) | **POST** /v2/agent_tasks | Create Agent Task
[**v2_agent_tasks_destroy**](WorksAppAgentTasksApi.md#v2_agent_tasks_destroy) | **DELETE** /v2/agent_tasks/{id} | Delete Agent Task
[**v2_agent_tasks_list**](WorksAppAgentTasksApi.md#v2_agent_tasks_list) | **GET** /v2/agent_tasks | List Agent Tasks
[**v2_agent_tasks_partial_update**](WorksAppAgentTasksApi.md#v2_agent_tasks_partial_update) | **PATCH** /v2/agent_tasks/{id} | Update Agent Task
[**v2_agent_tasks_patch_partial_update**](WorksAppAgentTasksApi.md#v2_agent_tasks_patch_partial_update) | **PATCH** /v2/agent_tasks/patch | 
[**v2_agent_tasks_retrieve**](WorksAppAgentTasksApi.md#v2_agent_tasks_retrieve) | **GET** /v2/agent_tasks/{id} | Get Agent Task Detail
[**v2_agent_tasks_update**](WorksAppAgentTasksApi.md#v2_agent_tasks_update) | **PUT** /v2/agent_tasks/{id} | Update Agent Task


# **v2_agent_tasks_bulk_patch_update_partial_update**
> AgentTask v2_agent_tasks_bulk_patch_update_partial_update(patched_agent_task_request=patched_agent_task_request)



Get Agent Tasks

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.patched_agent_task_request import PatchedAgentTaskRequest
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    patched_agent_task_request = io_amr_gwm.PatchedAgentTaskRequest() # PatchedAgentTaskRequest |  (optional)

    try:
        api_response = api_instance.v2_agent_tasks_bulk_patch_update_partial_update(patched_agent_task_request=patched_agent_task_request)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_bulk_patch_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_agent_task_request** | [**PatchedAgentTaskRequest**](PatchedAgentTaskRequest.md)|  | [optional] 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_clear_all_destroy**
> v2_agent_tasks_clear_all_destroy()

Clear All Agent Tasks

Clear All Agent Tasks

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)

    try:
        # Clear All Agent Tasks
        api_instance.v2_agent_tasks_clear_all_destroy()
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_clear_all_destroy: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_create**
> AgentTask v2_agent_tasks_create(agent_task_request=agent_task_request)

Create Agent Task

Create Agent Task

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.agent_task_request import AgentTaskRequest
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    agent_task_request = {"id":11,"agent":1,"work":1,"status":"COMPLETED","type":"PAYLOAD_MOVE","assignment_data":{},"action_data":{},"split_data":{},"task_fragments":[{"id":33,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}},{"id":44,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}}]} # AgentTaskRequest |  (optional)

    try:
        # Create Agent Task
        api_response = api_instance.v2_agent_tasks_create(agent_task_request=agent_task_request)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_task_request** | [**AgentTaskRequest**](AgentTaskRequest.md)|  | [optional] 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_destroy**
> v2_agent_tasks_destroy(id)

Delete Agent Task

Delete Agent Task

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    id = 56 # int | A unique value identifying this agent task.

    try:
        # Delete Agent Task
        api_instance.v2_agent_tasks_destroy(id)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_list**
> PaginatedAgentTaskList v2_agent_tasks_list(agent=agent, id=id, ordering=ordering, page=page, page_size=page_size, status=status, type=type, work=work, work_status=work_status)

List Agent Tasks

List Agent Tasks

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_agent_task_list import PaginatedAgentTaskList
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    agent = 3.4 # float | filter by agent id (optional)
    id = [56] # List[int] |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    status = 'status_example' # str | filter by status (optional)
    type = 'type_example' # str | filter by type (optional)
    work = ['work_example'] # List[str] | filter by work id (optional)
    work_status = ['work_status_example'] # List[str] | Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed (optional)

    try:
        # List Agent Tasks
        api_response = api_instance.v2_agent_tasks_list(agent=agent, id=id, ordering=ordering, page=page, page_size=page_size, status=status, type=type, work=work, work_status=work_status)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **float**| filter by agent id | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **status** | **str**| filter by status | [optional] 
 **type** | **str**| filter by type | [optional] 
 **work** | [**List[str]**](str.md)| filter by work id | [optional] 
 **work_status** | [**List[str]**](str.md)| Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 

### Return type

[**PaginatedAgentTaskList**](PaginatedAgentTaskList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_partial_update**
> AgentTask v2_agent_tasks_partial_update(id, patched_agent_task_request=patched_agent_task_request)

Update Agent Task

Update Agent Task

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.patched_agent_task_request import PatchedAgentTaskRequest
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    id = 56 # int | A unique value identifying this agent task.
    patched_agent_task_request = {"agent":1,"work":1,"status":"COMPLETED","type":"PAYLOAD_MOVE","assignment_data":{},"action_data":{},"split_data":{},"task_fragments":[{"id":33,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}},{"id":44,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}}]} # PatchedAgentTaskRequest |  (optional)

    try:
        # Update Agent Task
        api_response = api_instance.v2_agent_tasks_partial_update(id, patched_agent_task_request=patched_agent_task_request)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task. | 
 **patched_agent_task_request** | [**PatchedAgentTaskRequest**](PatchedAgentTaskRequest.md)|  | [optional] 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_patch_partial_update**
> AgentTask v2_agent_tasks_patch_partial_update(patched_agent_task_request=patched_agent_task_request)



Get Agent Tasks

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.patched_agent_task_request import PatchedAgentTaskRequest
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    patched_agent_task_request = io_amr_gwm.PatchedAgentTaskRequest() # PatchedAgentTaskRequest |  (optional)

    try:
        api_response = api_instance.v2_agent_tasks_patch_partial_update(patched_agent_task_request=patched_agent_task_request)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_patch_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_patch_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_agent_task_request** | [**PatchedAgentTaskRequest**](PatchedAgentTaskRequest.md)|  | [optional] 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_retrieve**
> AgentTask v2_agent_tasks_retrieve(id)

Get Agent Task Detail

Get Agent Task Detail

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    id = 56 # int | A unique value identifying this agent task.

    try:
        # Get Agent Task Detail
        api_response = api_instance.v2_agent_tasks_retrieve(id)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task. | 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_agent_tasks_update**
> AgentTask v2_agent_tasks_update(id, agent_task_request=agent_task_request)

Update Agent Task

Update Agent Task

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.agent_task_request import AgentTaskRequest
from io_amr_gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = io_amr_gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = io_amr_gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with io_amr_gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = io_amr_gwm.WorksAppAgentTasksApi(api_client)
    id = 56 # int | A unique value identifying this agent task.
    agent_task_request = {"agent":1,"work":1,"status":"COMPLETED","type":"PAYLOAD_MOVE","assignment_data":{},"action_data":{},"split_data":{},"task_fragments":[{"id":33,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}},{"id":44,"work_fragment":1,"status":"PREPARING_TO_PICK","type":"CONTAINER_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"}}]} # AgentTaskRequest |  (optional)

    try:
        # Update Agent Task
        api_response = api_instance.v2_agent_tasks_update(id, agent_task_request=agent_task_request)
        print("The response of WorksAppAgentTasksApi->v2_agent_tasks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTasksApi->v2_agent_tasks_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task. | 
 **agent_task_request** | [**AgentTaskRequest**](AgentTaskRequest.md)|  | [optional] 

### Return type

[**AgentTask**](AgentTask.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

