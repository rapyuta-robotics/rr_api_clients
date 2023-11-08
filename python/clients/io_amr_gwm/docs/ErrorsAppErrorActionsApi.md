# openapi_client.ErrorsAppErrorActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_error_action_create**](ErrorsAppErrorActionsApi.md#v1_error_action_create) | **POST** /v1/error_action | 
[**v1_error_action_destroy**](ErrorsAppErrorActionsApi.md#v1_error_action_destroy) | **DELETE** /v1/error_action/{id_or_name} | 
[**v1_error_action_list**](ErrorsAppErrorActionsApi.md#v1_error_action_list) | **GET** /v1/error_action | 
[**v1_error_action_partial_update**](ErrorsAppErrorActionsApi.md#v1_error_action_partial_update) | **PATCH** /v1/error_action/{id_or_name} | 
[**v1_error_action_retrieve**](ErrorsAppErrorActionsApi.md#v1_error_action_retrieve) | **GET** /v1/error_action/{id_or_name} | 
[**v1_error_action_update**](ErrorsAppErrorActionsApi.md#v1_error_action_update) | **PUT** /v1/error_action/{id_or_name} | 


# **v1_error_action_create**
> ErrorAction v1_error_action_create(error_action_request)



Create a new Error Action

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.error_action import ErrorAction
from openapi_client.models.error_action_request import ErrorActionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)
    error_action_request = {"name":"blow_up_robot","description":"Makes the robot explode to clear the way for other robots","schema":{"type":"object","required":["explosion_radius"],"properties":{"explosion_radius":{"type":"number","title":"explosion_radius","default":10}},"additionalProperties":false}} # ErrorActionRequest | 

    try:
        api_response = api_instance.v1_error_action_create(error_action_request)
        print("The response of ErrorsAppErrorActionsApi->v1_error_action_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_action_request** | [**ErrorActionRequest**](ErrorActionRequest.md)|  | 

### Return type

[**ErrorAction**](ErrorAction.md)

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

# **v1_error_action_destroy**
> v1_error_action_destroy(id_or_name)



Manage Error Actions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error action.

    try:
        api_instance.v1_error_action_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error action. | 

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

# **v1_error_action_list**
> List[ErrorAction] v1_error_action_list()



List Error Actions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.error_action import ErrorAction
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)

    try:
        api_response = api_instance.v1_error_action_list()
        print("The response of ErrorsAppErrorActionsApi->v1_error_action_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ErrorAction]**](ErrorAction.md)

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

# **v1_error_action_partial_update**
> ErrorAction v1_error_action_partial_update(id_or_name, patched_error_action_request=patched_error_action_request)



Manage Error Actions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.error_action import ErrorAction
from openapi_client.models.patched_error_action_request import PatchedErrorActionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error action.
    patched_error_action_request = openapi_client.PatchedErrorActionRequest() # PatchedErrorActionRequest |  (optional)

    try:
        api_response = api_instance.v1_error_action_partial_update(id_or_name, patched_error_action_request=patched_error_action_request)
        print("The response of ErrorsAppErrorActionsApi->v1_error_action_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error action. | 
 **patched_error_action_request** | [**PatchedErrorActionRequest**](PatchedErrorActionRequest.md)|  | [optional] 

### Return type

[**ErrorAction**](ErrorAction.md)

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

# **v1_error_action_retrieve**
> ErrorAction v1_error_action_retrieve(id_or_name)



Manage Error Actions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.error_action import ErrorAction
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error action.

    try:
        api_response = api_instance.v1_error_action_retrieve(id_or_name)
        print("The response of ErrorsAppErrorActionsApi->v1_error_action_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error action. | 

### Return type

[**ErrorAction**](ErrorAction.md)

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

# **v1_error_action_update**
> ErrorAction v1_error_action_update(id_or_name, error_action_request)



Manage Error Actions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.error_action import ErrorAction
from openapi_client.models.error_action_request import ErrorActionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: tokenAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ErrorsAppErrorActionsApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error action.
    error_action_request = openapi_client.ErrorActionRequest() # ErrorActionRequest | 

    try:
        api_response = api_instance.v1_error_action_update(id_or_name, error_action_request)
        print("The response of ErrorsAppErrorActionsApi->v1_error_action_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorActionsApi->v1_error_action_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error action. | 
 **error_action_request** | [**ErrorActionRequest**](ErrorActionRequest.md)|  | 

### Return type

[**ErrorAction**](ErrorAction.md)

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

