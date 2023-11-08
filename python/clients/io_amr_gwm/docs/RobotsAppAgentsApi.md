# io_amr_gwm.RobotsAppAgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_agent_create**](RobotsAppAgentsApi.md#v1_agent_create) | **POST** /v1/agent | 
[**v1_agent_destroy**](RobotsAppAgentsApi.md#v1_agent_destroy) | **DELETE** /v1/agent/{id_or_name} | 
[**v1_agent_global_mode_update**](RobotsAppAgentsApi.md#v1_agent_global_mode_update) | **PUT** /v1/agent/global_mode | Set all agents mode
[**v1_agent_list**](RobotsAppAgentsApi.md#v1_agent_list) | **GET** /v1/agent | 
[**v1_agent_partial_update**](RobotsAppAgentsApi.md#v1_agent_partial_update) | **PATCH** /v1/agent/{id_or_name} | 
[**v1_agent_retrieve**](RobotsAppAgentsApi.md#v1_agent_retrieve) | **GET** /v1/agent/{id_or_name} | 
[**v1_agent_update**](RobotsAppAgentsApi.md#v1_agent_update) | **PUT** /v1/agent/{id_or_name} | 


# **v1_agent_create**
> Agent v1_agent_create(agent_request)



Manage Agents in the Site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent import Agent
from io_amr_gwm.models.agent_request import AgentRequest
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    agent_request = io_amr_gwm.AgentRequest() # AgentRequest | 

    try:
        api_response = api_instance.v1_agent_create(agent_request)
        print("The response of RobotsAppAgentsApi->v1_agent_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_request** | [**AgentRequest**](AgentRequest.md)|  | 

### Return type

[**Agent**](Agent.md)

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

# **v1_agent_destroy**
> v1_agent_destroy(id_or_name)



List agents

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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    id_or_name = '1' # str | Agent ID or Name.

    try:
        api_instance.v1_agent_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Agent ID or Name. | 

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

# **v1_agent_global_mode_update**
> v1_agent_global_mode_update(agent_mode_request)

Set all agents mode

Set all agents mode

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent_mode_request import AgentModeRequest
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    agent_mode_request = io_amr_gwm.AgentModeRequest() # AgentModeRequest | 

    try:
        # Set all agents mode
        api_instance.v1_agent_global_mode_update(agent_mode_request)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_global_mode_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_mode_request** | [**AgentModeRequest**](AgentModeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list**
> List[Agent] v1_agent_list(map=map, robot_descriptor_id=robot_descriptor_id, robot_id=robot_id)



List agents

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent import Agent
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    map = [3.4] # List[float] | filter agents by maps ids or names (optional)
    robot_descriptor_id = 56 # int | filter agents by robot description ids (optional)
    robot_id = 56 # int | filter agents by robot id (optional)

    try:
        api_response = api_instance.v1_agent_list(map=map, robot_descriptor_id=robot_descriptor_id, robot_id=robot_id)
        print("The response of RobotsAppAgentsApi->v1_agent_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map** | [**List[float]**](float.md)| filter agents by maps ids or names | [optional] 
 **robot_descriptor_id** | **int**| filter agents by robot description ids | [optional] 
 **robot_id** | **int**| filter agents by robot id | [optional] 

### Return type

[**List[Agent]**](Agent.md)

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

# **v1_agent_partial_update**
> Agent v1_agent_partial_update(id_or_name, patched_agent_request=patched_agent_request)



List agents

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent import Agent
from io_amr_gwm.models.patched_agent_request import PatchedAgentRequest
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    id_or_name = '1' # str | Agent ID or Name.
    patched_agent_request = io_amr_gwm.PatchedAgentRequest() # PatchedAgentRequest |  (optional)

    try:
        api_response = api_instance.v1_agent_partial_update(id_or_name, patched_agent_request=patched_agent_request)
        print("The response of RobotsAppAgentsApi->v1_agent_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Agent ID or Name. | 
 **patched_agent_request** | [**PatchedAgentRequest**](PatchedAgentRequest.md)|  | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **v1_agent_retrieve**
> Agent v1_agent_retrieve(id_or_name)



List agents

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent import Agent
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    id_or_name = '1' # str | Agent ID or Name.

    try:
        api_response = api_instance.v1_agent_retrieve(id_or_name)
        print("The response of RobotsAppAgentsApi->v1_agent_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Agent ID or Name. | 

### Return type

[**Agent**](Agent.md)

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

# **v1_agent_update**
> Agent v1_agent_update(id_or_name, agent_request)



List agents

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.agent import Agent
from io_amr_gwm.models.agent_request import AgentRequest
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
    api_instance = io_amr_gwm.RobotsAppAgentsApi(api_client)
    id_or_name = '1' # str | Agent ID or Name.
    agent_request = io_amr_gwm.AgentRequest() # AgentRequest | 

    try:
        api_response = api_instance.v1_agent_update(id_or_name, agent_request)
        print("The response of RobotsAppAgentsApi->v1_agent_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppAgentsApi->v1_agent_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Agent ID or Name. | 
 **agent_request** | [**AgentRequest**](AgentRequest.md)|  | 

### Return type

[**Agent**](Agent.md)

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

