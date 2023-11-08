# gwm.WorksAppAgentTaskFragmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_agent_task_fragments_bulk_patch_update_partial_update**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_bulk_patch_update_partial_update) | **PATCH** /v2/agent_task_fragments/bulk_patch_update | 
[**v2_agent_task_fragments_create**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_create) | **POST** /v2/agent_task_fragments | Create Agent Task Fragment
[**v2_agent_task_fragments_destroy**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_destroy) | **DELETE** /v2/agent_task_fragments/{id} | Delete Agent Task Fragment
[**v2_agent_task_fragments_list**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_list) | **GET** /v2/agent_task_fragments | List Agent Task Fragments
[**v2_agent_task_fragments_partial_update**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_partial_update) | **PATCH** /v2/agent_task_fragments/{id} | Update Agent Task Fragment
[**v2_agent_task_fragments_patch_partial_update**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_patch_partial_update) | **PATCH** /v2/agent_task_fragments/patch | 
[**v2_agent_task_fragments_retrieve**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_retrieve) | **GET** /v2/agent_task_fragments/{id} | Get Agent Task Fragment Detail
[**v2_agent_task_fragments_summary_retrieve**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_summary_retrieve) | **GET** /v2/agent_task_fragments/summary | Get AGENT TASK Fragment Summary
[**v2_agent_task_fragments_update**](WorksAppAgentTaskFragmentsApi.md#v2_agent_task_fragments_update) | **PUT** /v2/agent_task_fragments/{id} | Update Agent Task Fragment


# **v2_agent_task_fragments_bulk_patch_update_partial_update**
> AgentTaskFragment v2_agent_task_fragments_bulk_patch_update_partial_update(patched_agent_task_fragment_request=patched_agent_task_fragment_request)



Get Agent Task Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.patched_agent_task_fragment_request import PatchedAgentTaskFragmentRequest
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    patched_agent_task_fragment_request = gwm.PatchedAgentTaskFragmentRequest() # PatchedAgentTaskFragmentRequest |  (optional)

    try:
        api_response = api_instance.v2_agent_task_fragments_bulk_patch_update_partial_update(patched_agent_task_fragment_request=patched_agent_task_fragment_request)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_bulk_patch_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_agent_task_fragment_request** | [**PatchedAgentTaskFragmentRequest**](PatchedAgentTaskFragmentRequest.md)|  | [optional] 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_create**
> AgentTaskFragment v2_agent_task_fragments_create(agent_task_fragment_request)

Create Agent Task Fragment

Create Agent Task Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.agent_task_fragment_request import AgentTaskFragmentRequest
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    agent_task_fragment_request = {"id":1213213,"agent_task":1,"work_fragment":1,"status":"NOT_STARTED","type":"ITEM_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"},"from_location":{"key":"value"},"to_location":{"key":"value"}} # AgentTaskFragmentRequest | 

    try:
        # Create Agent Task Fragment
        api_response = api_instance.v2_agent_task_fragments_create(agent_task_fragment_request)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_task_fragment_request** | [**AgentTaskFragmentRequest**](AgentTaskFragmentRequest.md)|  | 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_destroy**
> v2_agent_task_fragments_destroy(id)

Delete Agent Task Fragment

Delete Agent Task Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    id = 56 # int | A unique value identifying this agent task fragment.

    try:
        # Delete Agent Task Fragment
        api_instance.v2_agent_task_fragments_destroy(id)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task fragment. | 

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

# **v2_agent_task_fragments_list**
> PaginatedAgentTaskFragmentList v2_agent_task_fragments_list(agent=agent, agent_task=agent_task, detection_data=detection_data, drop_data=drop_data, end_date=end_date, from_location=from_location, id=id, name=name, ordering=ordering, page=page, page_size=page_size, payload_data=payload_data, pick_data=pick_data, start_date=start_date, status=status, to_location=to_location, type=type, work=work, work_fragment=work_fragment, work_status=work_status, workflow=workflow)

List Agent Task Fragments

List Agent Task Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.paginated_agent_task_fragment_list import PaginatedAgentTaskFragmentList
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    agent = 3.4 # float | filter by agent id (optional)
    agent_task = 3.4 # float | filter by agent_task id (optional)
    detection_data = 'detection_data_example' # str | filter by detection_data query (optional)
    drop_data = 'drop_data_example' # str | filter by drop_data query (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    from_location = 'from_location_example' # str | filter by from_location query (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    ordering = 'ordering_example' # str | order the result, default is ID (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    payload_data = 'payload_data_example' # str | filter by payload_data query (optional)
    pick_data = 'pick_data_example' # str | filter by pick_data query (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = 'status_example' # str | filter by status (optional)
    to_location = 'to_location_example' # str | filter by to_location query (optional)
    type = 'type_example' # str | filter by type (optional)
    work = ['work_example'] # List[str] | filter by work id (optional)
    work_fragment = 'work_fragment_example' # str | filter by work_fragment id (optional)
    work_status = ['work_status_example'] # List[str] | Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # List Agent Task Fragments
        api_response = api_instance.v2_agent_task_fragments_list(agent=agent, agent_task=agent_task, detection_data=detection_data, drop_data=drop_data, end_date=end_date, from_location=from_location, id=id, name=name, ordering=ordering, page=page, page_size=page_size, payload_data=payload_data, pick_data=pick_data, start_date=start_date, status=status, to_location=to_location, type=type, work=work, work_fragment=work_fragment, work_status=work_status, workflow=workflow)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **float**| filter by agent id | [optional] 
 **agent_task** | **float**| filter by agent_task id | [optional] 
 **detection_data** | **str**| filter by detection_data query | [optional] 
 **drop_data** | **str**| filter by drop_data query | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **from_location** | **str**| filter by from_location query | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **ordering** | **str**| order the result, default is ID | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **payload_data** | **str**| filter by payload_data query | [optional] 
 **pick_data** | **str**| filter by pick_data query | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **status** | **str**| filter by status | [optional] 
 **to_location** | **str**| filter by to_location query | [optional] 
 **type** | **str**| filter by type | [optional] 
 **work** | [**List[str]**](str.md)| filter by work id | [optional] 
 **work_fragment** | **str**| filter by work_fragment id | [optional] 
 **work_status** | [**List[str]**](str.md)| Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
 **workflow** | **str**|  | [optional] 

### Return type

[**PaginatedAgentTaskFragmentList**](PaginatedAgentTaskFragmentList.md)

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

# **v2_agent_task_fragments_partial_update**
> AgentTaskFragment v2_agent_task_fragments_partial_update(id, patched_agent_task_fragment_request=patched_agent_task_fragment_request)

Update Agent Task Fragment

Update Agent Task Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.patched_agent_task_fragment_request import PatchedAgentTaskFragmentRequest
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    id = 56 # int | A unique value identifying this agent task fragment.
    patched_agent_task_fragment_request = {"agent_task":1,"work_fragment":1,"status":"NOT_STARTED","type":"ITEM_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"},"from_location":{"key":"value"},"to_location":{"key":"value"}} # PatchedAgentTaskFragmentRequest |  (optional)

    try:
        # Update Agent Task Fragment
        api_response = api_instance.v2_agent_task_fragments_partial_update(id, patched_agent_task_fragment_request=patched_agent_task_fragment_request)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task fragment. | 
 **patched_agent_task_fragment_request** | [**PatchedAgentTaskFragmentRequest**](PatchedAgentTaskFragmentRequest.md)|  | [optional] 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_patch_partial_update**
> AgentTaskFragment v2_agent_task_fragments_patch_partial_update(patched_agent_task_fragment_request=patched_agent_task_fragment_request)



Get Agent Task Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.patched_agent_task_fragment_request import PatchedAgentTaskFragmentRequest
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    patched_agent_task_fragment_request = gwm.PatchedAgentTaskFragmentRequest() # PatchedAgentTaskFragmentRequest |  (optional)

    try:
        api_response = api_instance.v2_agent_task_fragments_patch_partial_update(patched_agent_task_fragment_request=patched_agent_task_fragment_request)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_patch_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_patch_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_agent_task_fragment_request** | [**PatchedAgentTaskFragmentRequest**](PatchedAgentTaskFragmentRequest.md)|  | [optional] 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_retrieve**
> AgentTaskFragment v2_agent_task_fragments_retrieve(id)

Get Agent Task Fragment Detail

Get Agent Task Fragment Detail

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    id = 56 # int | A unique value identifying this agent task fragment.

    try:
        # Get Agent Task Fragment Detail
        api_response = api_instance.v2_agent_task_fragments_retrieve(id)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task fragment. | 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_summary_retrieve**
> AgentTaskFragment v2_agent_task_fragments_summary_retrieve(agent=agent, agent_task=agent_task, end_date=end_date, group_by=group_by, id=id, name=name, start_date=start_date, status=status, type=type, work=work, work_fragment=work_fragment, work_status=work_status, workflow=workflow)

Get AGENT TASK Fragment Summary

Get AGENT TASK Fragment Summary

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    agent = [gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    agent_task = 56 # int |  (optional)
    end_date = 'end_date_example' # str | filter by end date (optional)
    group_by = ['group_by_example'] # List[str] | group by (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    start_date = 'start_date_example' # str | filter by start date (optional)
    status = 'status_example' # str | Agent Task Fragment status (optional)
    type = 'type_example' # str | Agent Task Fragment type (optional)
    work = [gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    work_fragment = 56 # int |  (optional)
    work_status = ['work_status_example'] # List[str] | Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # Get AGENT TASK Fragment Summary
        api_response = api_instance.v2_agent_task_fragments_summary_retrieve(agent=agent, agent_task=agent_task, end_date=end_date, group_by=group_by, id=id, name=name, start_date=start_date, status=status, type=type, work=work, work_fragment=work_fragment, work_status=work_status, workflow=workflow)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_summary_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **agent_task** | **int**|  | [optional] 
 **end_date** | **str**| filter by end date | [optional] 
 **group_by** | [**List[str]**](str.md)| group by | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **start_date** | **str**| filter by start date | [optional] 
 **status** | **str**| Agent Task Fragment status | [optional] 
 **type** | **str**| Agent Task Fragment type | [optional] 
 **work** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **work_fragment** | **int**|  | [optional] 
 **work_status** | [**List[str]**](str.md)| Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
 **workflow** | **str**|  | [optional] 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

# **v2_agent_task_fragments_update**
> AgentTaskFragment v2_agent_task_fragments_update(id, agent_task_fragment_request)

Update Agent Task Fragment

Update Agent Task Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.agent_task_fragment import AgentTaskFragment
from gwm.models.agent_task_fragment_request import AgentTaskFragmentRequest
from gwm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm.WorksAppAgentTaskFragmentsApi(api_client)
    id = 56 # int | A unique value identifying this agent task fragment.
    agent_task_fragment_request = {"agent_task":1,"work_fragment":1,"status":"NOT_STARTED","type":"ITEM_MOVE","quantity_requested":100,"quantity_delivered":50,"payload_data":{"key":"value"},"detection_data":{"key":"value"},"pick_data":{"key":"value"},"drop_data":{"key":"value"},"from_location":{"key":"value"},"to_location":{"key":"value"}} # AgentTaskFragmentRequest | 

    try:
        # Update Agent Task Fragment
        api_response = api_instance.v2_agent_task_fragments_update(id, agent_task_fragment_request)
        print("The response of WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppAgentTaskFragmentsApi->v2_agent_task_fragments_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique value identifying this agent task fragment. | 
 **agent_task_fragment_request** | [**AgentTaskFragmentRequest**](AgentTaskFragmentRequest.md)|  | 

### Return type

[**AgentTaskFragment**](AgentTaskFragment.md)

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

