# gwm_client.ErrorsAppErrorTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_error_type_create**](ErrorsAppErrorTypesApi.md#v1_error_type_create) | **POST** /v1/error_type | Create a new Error Type
[**v1_error_type_destroy**](ErrorsAppErrorTypesApi.md#v1_error_type_destroy) | **DELETE** /v1/error_type/{id_or_name} | Delete Error Type
[**v1_error_type_list**](ErrorsAppErrorTypesApi.md#v1_error_type_list) | **GET** /v1/error_type | List Error Types
[**v1_error_type_partial_update**](ErrorsAppErrorTypesApi.md#v1_error_type_partial_update) | **PATCH** /v1/error_type/{id_or_name} | Patch Error Types
[**v1_error_type_patch_partial_update**](ErrorsAppErrorTypesApi.md#v1_error_type_patch_partial_update) | **PATCH** /v1/error_type/patch | 
[**v1_error_type_put_update**](ErrorsAppErrorTypesApi.md#v1_error_type_put_update) | **PUT** /v1/error_type/put | 
[**v1_error_type_retrieve**](ErrorsAppErrorTypesApi.md#v1_error_type_retrieve) | **GET** /v1/error_type/{id_or_name} | Get Error Type
[**v1_error_type_update**](ErrorsAppErrorTypesApi.md#v1_error_type_update) | **PUT** /v1/error_type/{id_or_name} | Patch Error Types


# **v1_error_type_create**
> ErrorType v1_error_type_create(error_type_request)

Create a new Error Type

Create a new Error Type

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
from gwm_client.models.error_type_request import ErrorTypeRequest
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    error_type_request = {"name":"Robot entered self destruct region","local_error_code":999,"reporting_component":"explosion manager","global_error_code":9999,"criticality":1,"clearing_options":["blow_up_robot"],"auto_recovery_actions":[{"action":"blow_up_robot","content":{"explosion_radius":50},"first_attempt_after":10,"retry_interval":5,"max_attempts":10}],"meta_data":{"key":"value"}} # ErrorTypeRequest | 

    try:
        # Create a new Error Type
        api_response = api_instance.v1_error_type_create(error_type_request)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_type_request** | [**ErrorTypeRequest**](ErrorTypeRequest.md)|  | 

### Return type

[**ErrorType**](ErrorType.md)

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

# **v1_error_type_destroy**
> v1_error_type_destroy(id_or_name)

Delete Error Type

Delete Error Type

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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error type.

    try:
        # Delete Error Type
        api_instance.v1_error_type_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error type. | 

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

# **v1_error_type_list**
> List[ErrorType] v1_error_type_list(criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)

List Error Types

List Error Types

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    criticality = [56] # List[int] | filter by criticality (optional)
    local_error_code = [56] # List[int] | filter errors by local error code (optional)
    reporting_component = ['reporting_component_example'] # List[str] | filter errors by reporting component (optional)

    try:
        # List Error Types
        api_response = api_instance.v1_error_type_list(criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criticality** | [**List[int]**](int.md)| filter by criticality | [optional] 
 **local_error_code** | [**List[int]**](int.md)| filter errors by local error code | [optional] 
 **reporting_component** | [**List[str]**](str.md)| filter errors by reporting component | [optional] 

### Return type

[**List[ErrorType]**](ErrorType.md)

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

# **v1_error_type_partial_update**
> ErrorType v1_error_type_partial_update(id_or_name, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component, patched_error_type_request=patched_error_type_request)

Patch Error Types

Patch Error Types

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
from gwm_client.models.patched_error_type_request import PatchedErrorTypeRequest
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error type.
    criticality = [56] # List[int] | filter by criticality (optional)
    local_error_code = [56] # List[int] | filter errors by local error code (optional)
    reporting_component = ['reporting_component_example'] # List[str] | filter errors by reporting component (optional)
    patched_error_type_request = {"name":"Robot entered self destruct region","local_error_code":999,"reporting_component":"explosion manager","global_error_code":9999,"criticality":1,"clearing_options":["blow_up_robot"],"auto_recovery_actions":[{"action":"blow_up_robot","content":{"explosion_radius":50},"first_attempt_after":10,"retry_interval":5,"max_attempts":10}],"meta_data":{"key":"value"}} # PatchedErrorTypeRequest |  (optional)

    try:
        # Patch Error Types
        api_response = api_instance.v1_error_type_partial_update(id_or_name, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component, patched_error_type_request=patched_error_type_request)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error type. | 
 **criticality** | [**List[int]**](int.md)| filter by criticality | [optional] 
 **local_error_code** | [**List[int]**](int.md)| filter errors by local error code | [optional] 
 **reporting_component** | [**List[str]**](str.md)| filter errors by reporting component | [optional] 
 **patched_error_type_request** | [**PatchedErrorTypeRequest**](PatchedErrorTypeRequest.md)|  | [optional] 

### Return type

[**ErrorType**](ErrorType.md)

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

# **v1_error_type_patch_partial_update**
> ErrorType v1_error_type_patch_partial_update(patched_error_type_request=patched_error_type_request)



Manage Error Types

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
from gwm_client.models.patched_error_type_request import PatchedErrorTypeRequest
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    patched_error_type_request = gwm_client.PatchedErrorTypeRequest() # PatchedErrorTypeRequest |  (optional)

    try:
        api_response = api_instance.v1_error_type_patch_partial_update(patched_error_type_request=patched_error_type_request)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_patch_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_patch_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_error_type_request** | [**PatchedErrorTypeRequest**](PatchedErrorTypeRequest.md)|  | [optional] 

### Return type

[**ErrorType**](ErrorType.md)

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

# **v1_error_type_put_update**
> ErrorType v1_error_type_put_update(error_type_request)



Manage Error Types

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
from gwm_client.models.error_type_request import ErrorTypeRequest
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    error_type_request = gwm_client.ErrorTypeRequest() # ErrorTypeRequest | 

    try:
        api_response = api_instance.v1_error_type_put_update(error_type_request)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_put_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_put_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_type_request** | [**ErrorTypeRequest**](ErrorTypeRequest.md)|  | 

### Return type

[**ErrorType**](ErrorType.md)

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

# **v1_error_type_retrieve**
> ErrorType v1_error_type_retrieve(id_or_name, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)

Get Error Type

Get Error Type

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error type.
    criticality = [56] # List[int] | filter by criticality (optional)
    local_error_code = [56] # List[int] | filter errors by local error code (optional)
    reporting_component = ['reporting_component_example'] # List[str] | filter errors by reporting component (optional)

    try:
        # Get Error Type
        api_response = api_instance.v1_error_type_retrieve(id_or_name, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error type. | 
 **criticality** | [**List[int]**](int.md)| filter by criticality | [optional] 
 **local_error_code** | [**List[int]**](int.md)| filter errors by local error code | [optional] 
 **reporting_component** | [**List[str]**](str.md)| filter errors by reporting component | [optional] 

### Return type

[**ErrorType**](ErrorType.md)

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

# **v1_error_type_update**
> ErrorType v1_error_type_update(id_or_name, error_type_request, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)

Patch Error Types

Patch Error Types

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.error_type import ErrorType
from gwm_client.models.error_type_request import ErrorTypeRequest
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
    api_instance = gwm_client.ErrorsAppErrorTypesApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this error type.
    error_type_request = {"name":"Robot entered self destruct region","local_error_code":999,"reporting_component":"explosion manager","global_error_code":9999,"criticality":1,"clearing_options":["blow_up_robot"],"auto_recovery_actions":[{"action":"blow_up_robot","content":{"explosion_radius":50},"first_attempt_after":10,"retry_interval":5,"max_attempts":10}],"meta_data":{"key":"value"}} # ErrorTypeRequest | 
    criticality = [56] # List[int] | filter by criticality (optional)
    local_error_code = [56] # List[int] | filter errors by local error code (optional)
    reporting_component = ['reporting_component_example'] # List[str] | filter errors by reporting component (optional)

    try:
        # Patch Error Types
        api_response = api_instance.v1_error_type_update(id_or_name, error_type_request, criticality=criticality, local_error_code=local_error_code, reporting_component=reporting_component)
        print("The response of ErrorsAppErrorTypesApi->v1_error_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorsAppErrorTypesApi->v1_error_type_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this error type. | 
 **error_type_request** | [**ErrorTypeRequest**](ErrorTypeRequest.md)|  | 
 **criticality** | [**List[int]**](int.md)| filter by criticality | [optional] 
 **local_error_code** | [**List[int]**](int.md)| filter errors by local error code | [optional] 
 **reporting_component** | [**List[str]**](str.md)| filter errors by reporting component | [optional] 

### Return type

[**ErrorType**](ErrorType.md)

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

