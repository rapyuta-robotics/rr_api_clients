# gwm_client.ComputeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_v1_workflows_executions_bulk_create**](ComputeApi.md#compute_v1_workflows_executions_bulk_create) | **POST** /compute/v1/workflows/executions/bulk/ | 
[**compute_v1_workflows_executions_bulk_partial_update**](ComputeApi.md#compute_v1_workflows_executions_bulk_partial_update) | **PATCH** /compute/v1/workflows/executions/bulk/ | 
[**compute_v1_workflows_executions_create**](ComputeApi.md#compute_v1_workflows_executions_create) | **POST** /compute/v1/workflows/executions/ | 
[**compute_v1_workflows_executions_destroy**](ComputeApi.md#compute_v1_workflows_executions_destroy) | **DELETE** /compute/v1/workflows/executions/{id}/ | 
[**compute_v1_workflows_executions_list**](ComputeApi.md#compute_v1_workflows_executions_list) | **GET** /compute/v1/workflows/executions/ | 
[**compute_v1_workflows_executions_partial_update**](ComputeApi.md#compute_v1_workflows_executions_partial_update) | **PATCH** /compute/v1/workflows/executions/{id}/ | 
[**compute_v1_workflows_executions_retrieve**](ComputeApi.md#compute_v1_workflows_executions_retrieve) | **GET** /compute/v1/workflows/executions/{id}/ | 
[**compute_v1_workflows_executions_update**](ComputeApi.md#compute_v1_workflows_executions_update) | **PUT** /compute/v1/workflows/executions/{id}/ | 


# **compute_v1_workflows_executions_bulk_create**
> List[WorkflowExecutionSerializerV1] compute_v1_workflows_executions_bulk_create(workflow_execution_serializer_v1_request)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_serializer_v1 import WorkflowExecutionSerializerV1
from gwm_client.models.workflow_execution_serializer_v1_request import WorkflowExecutionSerializerV1Request
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    workflow_execution_serializer_v1_request = [gwm_client.WorkflowExecutionSerializerV1Request()] # List[WorkflowExecutionSerializerV1Request] | 

    try:
        api_response = api_instance.compute_v1_workflows_executions_bulk_create(workflow_execution_serializer_v1_request)
        print("The response of ComputeApi->compute_v1_workflows_executions_bulk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_bulk_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_execution_serializer_v1_request** | [**List[WorkflowExecutionSerializerV1Request]**](WorkflowExecutionSerializerV1Request.md)|  | 

### Return type

[**List[WorkflowExecutionSerializerV1]**](WorkflowExecutionSerializerV1.md)

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

# **compute_v1_workflows_executions_bulk_partial_update**
> List[WorkflowExecutionBulkUpdateSerializerV1] compute_v1_workflows_executions_bulk_partial_update(workflow_execution_bulk_update_serializer_v1_request)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_bulk_update_serializer_v1 import WorkflowExecutionBulkUpdateSerializerV1
from gwm_client.models.workflow_execution_bulk_update_serializer_v1_request import WorkflowExecutionBulkUpdateSerializerV1Request
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    workflow_execution_bulk_update_serializer_v1_request = [gwm_client.WorkflowExecutionBulkUpdateSerializerV1Request()] # List[WorkflowExecutionBulkUpdateSerializerV1Request] | 

    try:
        api_response = api_instance.compute_v1_workflows_executions_bulk_partial_update(workflow_execution_bulk_update_serializer_v1_request)
        print("The response of ComputeApi->compute_v1_workflows_executions_bulk_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_bulk_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_execution_bulk_update_serializer_v1_request** | [**List[WorkflowExecutionBulkUpdateSerializerV1Request]**](WorkflowExecutionBulkUpdateSerializerV1Request.md)|  | 

### Return type

[**List[WorkflowExecutionBulkUpdateSerializerV1]**](WorkflowExecutionBulkUpdateSerializerV1.md)

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

# **compute_v1_workflows_executions_create**
> WorkflowExecutionSerializerV1 compute_v1_workflows_executions_create(workflow_execution_serializer_v1_request)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_serializer_v1 import WorkflowExecutionSerializerV1
from gwm_client.models.workflow_execution_serializer_v1_request import WorkflowExecutionSerializerV1Request
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    workflow_execution_serializer_v1_request = gwm_client.WorkflowExecutionSerializerV1Request() # WorkflowExecutionSerializerV1Request | 

    try:
        api_response = api_instance.compute_v1_workflows_executions_create(workflow_execution_serializer_v1_request)
        print("The response of ComputeApi->compute_v1_workflows_executions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_execution_serializer_v1_request** | [**WorkflowExecutionSerializerV1Request**](WorkflowExecutionSerializerV1Request.md)|  | 

### Return type

[**WorkflowExecutionSerializerV1**](WorkflowExecutionSerializerV1.md)

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

# **compute_v1_workflows_executions_destroy**
> compute_v1_workflows_executions_destroy(id)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    id = 'id_example' # str | A UUID string identifying this workflow execution.

    try:
        api_instance.compute_v1_workflows_executions_destroy(id)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this workflow execution. | 

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

# **compute_v1_workflows_executions_list**
> List[WorkflowExecutionSerializerV1] compute_v1_workflows_executions_list(context=context, end_time_after=end_time_after, end_time_before=end_time_before, id=id, insert_time_after=insert_time_after, insert_time_before=insert_time_before, start_time_after=start_time_after, start_time_before=start_time_before, status=status, type=type, update_time_after=update_time_after, update_time_before=update_time_before)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_serializer_v1 import WorkflowExecutionSerializerV1
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    context = 'context_example' # str | filter by context query (optional)
    end_time_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = 'id_example' # str |  (optional)
    insert_time_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    insert_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_time_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = 'status_example' # str | Status of the workflow execution.  * `PENDING` - Pending * `RUNNING` - Running * `COMPLETED` - Completed * `FAILED` - Failed * `CANCELED` - Canceled * `TERMINATED` - Terminated * `CONTINUED_AS_NEW` - Continued as new * `TIMED_OUT` - Timed out (optional)
    type = 'type_example' # str | The workflow type. (optional)
    update_time_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    update_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.compute_v1_workflows_executions_list(context=context, end_time_after=end_time_after, end_time_before=end_time_before, id=id, insert_time_after=insert_time_after, insert_time_before=insert_time_before, start_time_after=start_time_after, start_time_before=start_time_before, status=status, type=type, update_time_after=update_time_after, update_time_before=update_time_before)
        print("The response of ComputeApi->compute_v1_workflows_executions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| filter by context query | [optional] 
 **end_time_after** | **datetime**|  | [optional] 
 **end_time_before** | **datetime**|  | [optional] 
 **id** | **str**|  | [optional] 
 **insert_time_after** | **datetime**|  | [optional] 
 **insert_time_before** | **datetime**|  | [optional] 
 **start_time_after** | **datetime**|  | [optional] 
 **start_time_before** | **datetime**|  | [optional] 
 **status** | **str**| Status of the workflow execution.  * &#x60;PENDING&#x60; - Pending * &#x60;RUNNING&#x60; - Running * &#x60;COMPLETED&#x60; - Completed * &#x60;FAILED&#x60; - Failed * &#x60;CANCELED&#x60; - Canceled * &#x60;TERMINATED&#x60; - Terminated * &#x60;CONTINUED_AS_NEW&#x60; - Continued as new * &#x60;TIMED_OUT&#x60; - Timed out | [optional] 
 **type** | **str**| The workflow type. | [optional] 
 **update_time_after** | **datetime**|  | [optional] 
 **update_time_before** | **datetime**|  | [optional] 

### Return type

[**List[WorkflowExecutionSerializerV1]**](WorkflowExecutionSerializerV1.md)

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

# **compute_v1_workflows_executions_partial_update**
> WorkflowExecutionUpdateSerializerV1 compute_v1_workflows_executions_partial_update(id, patched_workflow_execution_update_serializer_v1_request=patched_workflow_execution_update_serializer_v1_request)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.patched_workflow_execution_update_serializer_v1_request import PatchedWorkflowExecutionUpdateSerializerV1Request
from gwm_client.models.workflow_execution_update_serializer_v1 import WorkflowExecutionUpdateSerializerV1
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    id = 'id_example' # str | A UUID string identifying this workflow execution.
    patched_workflow_execution_update_serializer_v1_request = gwm_client.PatchedWorkflowExecutionUpdateSerializerV1Request() # PatchedWorkflowExecutionUpdateSerializerV1Request |  (optional)

    try:
        api_response = api_instance.compute_v1_workflows_executions_partial_update(id, patched_workflow_execution_update_serializer_v1_request=patched_workflow_execution_update_serializer_v1_request)
        print("The response of ComputeApi->compute_v1_workflows_executions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this workflow execution. | 
 **patched_workflow_execution_update_serializer_v1_request** | [**PatchedWorkflowExecutionUpdateSerializerV1Request**](PatchedWorkflowExecutionUpdateSerializerV1Request.md)|  | [optional] 

### Return type

[**WorkflowExecutionUpdateSerializerV1**](WorkflowExecutionUpdateSerializerV1.md)

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

# **compute_v1_workflows_executions_retrieve**
> WorkflowExecutionSerializerV1 compute_v1_workflows_executions_retrieve(id)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_serializer_v1 import WorkflowExecutionSerializerV1
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    id = 'id_example' # str | A UUID string identifying this workflow execution.

    try:
        api_response = api_instance.compute_v1_workflows_executions_retrieve(id)
        print("The response of ComputeApi->compute_v1_workflows_executions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this workflow execution. | 

### Return type

[**WorkflowExecutionSerializerV1**](WorkflowExecutionSerializerV1.md)

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

# **compute_v1_workflows_executions_update**
> WorkflowExecutionUpdateSerializerV1 compute_v1_workflows_executions_update(id, workflow_execution_update_serializer_v1_request=workflow_execution_update_serializer_v1_request)



A view set for listing, retrieving and performing workflow executions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.workflow_execution_update_serializer_v1 import WorkflowExecutionUpdateSerializerV1
from gwm_client.models.workflow_execution_update_serializer_v1_request import WorkflowExecutionUpdateSerializerV1Request
from gwm_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gwm_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = gwm_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gwm_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gwm_client.ComputeApi(api_client)
    id = 'id_example' # str | A UUID string identifying this workflow execution.
    workflow_execution_update_serializer_v1_request = gwm_client.WorkflowExecutionUpdateSerializerV1Request() # WorkflowExecutionUpdateSerializerV1Request |  (optional)

    try:
        api_response = api_instance.compute_v1_workflows_executions_update(id, workflow_execution_update_serializer_v1_request=workflow_execution_update_serializer_v1_request)
        print("The response of ComputeApi->compute_v1_workflows_executions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputeApi->compute_v1_workflows_executions_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this workflow execution. | 
 **workflow_execution_update_serializer_v1_request** | [**WorkflowExecutionUpdateSerializerV1Request**](WorkflowExecutionUpdateSerializerV1Request.md)|  | [optional] 

### Return type

[**WorkflowExecutionUpdateSerializerV1**](WorkflowExecutionUpdateSerializerV1.md)

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

