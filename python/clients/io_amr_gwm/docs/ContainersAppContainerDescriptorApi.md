# openapi_client.ContainersAppContainerDescriptorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_container_descriptors_apply_create**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_apply_create) | **POST** /v1/container_descriptors/apply | 
[**v1_container_descriptors_apply_dry_run_create**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_apply_dry_run_create) | **POST** /v1/container_descriptors/apply:dry_run | 
[**v1_container_descriptors_bulk_patch_update_partial_update**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_bulk_patch_update_partial_update) | **PATCH** /v1/container_descriptors/bulk_patch_update | Patch Container Descriptors
[**v1_container_descriptors_create**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_create) | **POST** /v1/container_descriptors | Create Container Descriptors
[**v1_container_descriptors_delete_destroy**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_delete_destroy) | **DELETE** /v1/container_descriptors/delete | Bulk Delete Container Descriptors
[**v1_container_descriptors_destroy**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_destroy) | **DELETE** /v1/container_descriptors/{id_or_name} | 
[**v1_container_descriptors_list**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_list) | **GET** /v1/container_descriptors | List Container Descriptors
[**v1_container_descriptors_partial_update**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_partial_update) | **PATCH** /v1/container_descriptors/{id_or_name} | 
[**v1_container_descriptors_retrieve**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_retrieve) | **GET** /v1/container_descriptors/{id_or_name} | 
[**v1_container_descriptors_update**](ContainersAppContainerDescriptorApi.md#v1_container_descriptors_update) | **PUT** /v1/container_descriptors/{id_or_name} | 


# **v1_container_descriptors_apply_create**
> ContainerDescriptor v1_container_descriptors_apply_create(container_descriptor_request)



Manage Container Descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor import ContainerDescriptor
from openapi_client.models.container_descriptor_request import ContainerDescriptorRequest
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    container_descriptor_request = openapi_client.ContainerDescriptorRequest() # ContainerDescriptorRequest | 

    try:
        api_response = api_instance.v1_container_descriptors_apply_create(container_descriptor_request)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_apply_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_apply_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_descriptor_request** | [**ContainerDescriptorRequest**](ContainerDescriptorRequest.md)|  | 

### Return type

[**ContainerDescriptor**](ContainerDescriptor.md)

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

# **v1_container_descriptors_apply_dry_run_create**
> ContainerDescriptor v1_container_descriptors_apply_dry_run_create(container_descriptor_request)



Manage Container Descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor import ContainerDescriptor
from openapi_client.models.container_descriptor_request import ContainerDescriptorRequest
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    container_descriptor_request = openapi_client.ContainerDescriptorRequest() # ContainerDescriptorRequest | 

    try:
        api_response = api_instance.v1_container_descriptors_apply_dry_run_create(container_descriptor_request)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_apply_dry_run_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_apply_dry_run_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_descriptor_request** | [**ContainerDescriptorRequest**](ContainerDescriptorRequest.md)|  | 

### Return type

[**ContainerDescriptor**](ContainerDescriptor.md)

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

# **v1_container_descriptors_bulk_patch_update_partial_update**
> v1_container_descriptors_bulk_patch_update_partial_update(patched_container_descriptor_request)

Patch Container Descriptors

Patch Container Descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.patched_container_descriptor_request import PatchedContainerDescriptorRequest
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    patched_container_descriptor_request = [openapi_client.PatchedContainerDescriptorRequest()] # List[PatchedContainerDescriptorRequest] | 

    try:
        # Patch Container Descriptors
        api_instance.v1_container_descriptors_bulk_patch_update_partial_update(patched_container_descriptor_request)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_container_descriptor_request** | [**List[PatchedContainerDescriptorRequest]**](PatchedContainerDescriptorRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_container_descriptors_create**
> PaginatedContainerDescriptorList v1_container_descriptors_create(container_descriptor_request, group=group, id=id, name=name, page=page, page_size=page_size, type=type)

Create Container Descriptors

Create Container Descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor_request import ContainerDescriptorRequest
from openapi_client.models.paginated_container_descriptor_list import PaginatedContainerDescriptorList
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    container_descriptor_request = [openapi_client.ContainerDescriptorRequest()] # List[ContainerDescriptorRequest] | 
    group = ['group_example'] # List[str] |  (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = ['type_example'] # List[str] |  (optional)

    try:
        # Create Container Descriptors
        api_response = api_instance.v1_container_descriptors_create(container_descriptor_request, group=group, id=id, name=name, page=page, page_size=page_size, type=type)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_descriptor_request** | [**List[ContainerDescriptorRequest]**](ContainerDescriptorRequest.md)|  | 
 **group** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedContainerDescriptorList**](PaginatedContainerDescriptorList.md)

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

# **v1_container_descriptors_delete_destroy**
> v1_container_descriptors_delete_destroy(application=application, id=id, name=name, type=type)

Bulk Delete Container Descriptors

Bulk Delete  Container Descriptors

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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    application = ['application_example'] # List[str] | List of Container Descriptor applications (optional)
    id = [3.4] # List[float] | List of Container Descriptor IDs (optional)
    name = ['name_example'] # List[str] | List of Container Descriptor names (optional)
    type = ['type_example'] # List[str] | List of Container Descriptor types (optional)

    try:
        # Bulk Delete Container Descriptors
        api_instance.v1_container_descriptors_delete_destroy(application=application, id=id, name=name, type=type)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**List[str]**](str.md)| List of Container Descriptor applications | [optional] 
 **id** | [**List[float]**](float.md)| List of Container Descriptor IDs | [optional] 
 **name** | [**List[str]**](str.md)| List of Container Descriptor names | [optional] 
 **type** | [**List[str]**](str.md)| List of Container Descriptor types | [optional] 

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

# **v1_container_descriptors_destroy**
> v1_container_descriptors_destroy(id_or_name)



List container descriptors

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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    id_or_name = '1' # str | ContainerDescriptor ID or Name.

    try:
        api_instance.v1_container_descriptors_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| ContainerDescriptor ID or Name. | 

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

# **v1_container_descriptors_list**
> PaginatedContainerDescriptorList v1_container_descriptors_list(application=application, group=group, id=id, name=name, page=page, page_size=page_size, type=type)

List Container Descriptors

List Container Descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.paginated_container_descriptor_list import PaginatedContainerDescriptorList
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    application = ['application_example'] # List[str] | List of Container Descriptor applications (optional)
    group = ['group_example'] # List[str] |  (optional)
    id = [3.4] # List[float] | List of Container Descriptor IDs (optional)
    name = ['name_example'] # List[str] | List of Container Descriptor names (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = ['type_example'] # List[str] | List of Container Descriptor types (optional)

    try:
        # List Container Descriptors
        api_response = api_instance.v1_container_descriptors_list(application=application, group=group, id=id, name=name, page=page, page_size=page_size, type=type)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**List[str]**](str.md)| List of Container Descriptor applications | [optional] 
 **group** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[float]**](float.md)| List of Container Descriptor IDs | [optional] 
 **name** | [**List[str]**](str.md)| List of Container Descriptor names | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | [**List[str]**](str.md)| List of Container Descriptor types | [optional] 

### Return type

[**PaginatedContainerDescriptorList**](PaginatedContainerDescriptorList.md)

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

# **v1_container_descriptors_partial_update**
> ContainerDescriptor v1_container_descriptors_partial_update(id_or_name, patched_container_descriptor_request=patched_container_descriptor_request)



List container descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor import ContainerDescriptor
from openapi_client.models.patched_container_descriptor_request import PatchedContainerDescriptorRequest
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    id_or_name = '1' # str | ContainerDescriptor ID or Name.
    patched_container_descriptor_request = openapi_client.PatchedContainerDescriptorRequest() # PatchedContainerDescriptorRequest |  (optional)

    try:
        api_response = api_instance.v1_container_descriptors_partial_update(id_or_name, patched_container_descriptor_request=patched_container_descriptor_request)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| ContainerDescriptor ID or Name. | 
 **patched_container_descriptor_request** | [**PatchedContainerDescriptorRequest**](PatchedContainerDescriptorRequest.md)|  | [optional] 

### Return type

[**ContainerDescriptor**](ContainerDescriptor.md)

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

# **v1_container_descriptors_retrieve**
> ContainerDescriptor v1_container_descriptors_retrieve(id_or_name)



List container descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor import ContainerDescriptor
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    id_or_name = '1' # str | ContainerDescriptor ID or Name.

    try:
        api_response = api_instance.v1_container_descriptors_retrieve(id_or_name)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| ContainerDescriptor ID or Name. | 

### Return type

[**ContainerDescriptor**](ContainerDescriptor.md)

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

# **v1_container_descriptors_update**
> ContainerDescriptor v1_container_descriptors_update(id_or_name, container_descriptor_request)



List container descriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.container_descriptor import ContainerDescriptor
from openapi_client.models.container_descriptor_request import ContainerDescriptorRequest
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
    api_instance = openapi_client.ContainersAppContainerDescriptorApi(api_client)
    id_or_name = '1' # str | ContainerDescriptor ID or Name.
    container_descriptor_request = openapi_client.ContainerDescriptorRequest() # ContainerDescriptorRequest | 

    try:
        api_response = api_instance.v1_container_descriptors_update(id_or_name, container_descriptor_request)
        print("The response of ContainersAppContainerDescriptorApi->v1_container_descriptors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerDescriptorApi->v1_container_descriptors_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| ContainerDescriptor ID or Name. | 
 **container_descriptor_request** | [**ContainerDescriptorRequest**](ContainerDescriptorRequest.md)|  | 

### Return type

[**ContainerDescriptor**](ContainerDescriptor.md)

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

