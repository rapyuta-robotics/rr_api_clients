# io_amr_gwm.ContainersAppContainerMasterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_containers_apply_create**](ContainersAppContainerMasterApi.md#v1_containers_apply_create) | **POST** /v1/containers/apply | 
[**v1_containers_apply_dry_run_create**](ContainersAppContainerMasterApi.md#v1_containers_apply_dry_run_create) | **POST** /v1/containers/apply:dry_run | 
[**v1_containers_bulk_patch_update_partial_update**](ContainersAppContainerMasterApi.md#v1_containers_bulk_patch_update_partial_update) | **PATCH** /v1/containers/bulk_patch_update | Patch containers
[**v1_containers_count_retrieve**](ContainersAppContainerMasterApi.md#v1_containers_count_retrieve) | **GET** /v1/containers/count | 
[**v1_containers_create**](ContainersAppContainerMasterApi.md#v1_containers_create) | **POST** /v1/containers | Create containers
[**v1_containers_delete_destroy**](ContainersAppContainerMasterApi.md#v1_containers_delete_destroy) | **DELETE** /v1/containers/delete | Bulk Delete Containers
[**v1_containers_destroy**](ContainersAppContainerMasterApi.md#v1_containers_destroy) | **DELETE** /v1/containers/{id_or_name} | 
[**v1_containers_list**](ContainersAppContainerMasterApi.md#v1_containers_list) | **GET** /v1/containers | 
[**v1_containers_partial_update**](ContainersAppContainerMasterApi.md#v1_containers_partial_update) | **PATCH** /v1/containers/{id_or_name} | 
[**v1_containers_retrieve**](ContainersAppContainerMasterApi.md#v1_containers_retrieve) | **GET** /v1/containers/{id_or_name} | 
[**v1_containers_update**](ContainersAppContainerMasterApi.md#v1_containers_update) | **PUT** /v1/containers/{id_or_name} | 


# **v1_containers_apply_create**
> Container v1_containers_apply_create(container_request)



Manage Containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container import Container
from io_amr_gwm.models.container_request import ContainerRequest
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    container_request = io_amr_gwm.ContainerRequest() # ContainerRequest | 

    try:
        api_response = api_instance.v1_containers_apply_create(container_request)
        print("The response of ContainersAppContainerMasterApi->v1_containers_apply_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_apply_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_request** | [**ContainerRequest**](ContainerRequest.md)|  | 

### Return type

[**Container**](Container.md)

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

# **v1_containers_apply_dry_run_create**
> Container v1_containers_apply_dry_run_create(container_request)



Manage Containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container import Container
from io_amr_gwm.models.container_request import ContainerRequest
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    container_request = io_amr_gwm.ContainerRequest() # ContainerRequest | 

    try:
        api_response = api_instance.v1_containers_apply_dry_run_create(container_request)
        print("The response of ContainersAppContainerMasterApi->v1_containers_apply_dry_run_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_apply_dry_run_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_request** | [**ContainerRequest**](ContainerRequest.md)|  | 

### Return type

[**Container**](Container.md)

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

# **v1_containers_bulk_patch_update_partial_update**
> v1_containers_bulk_patch_update_partial_update(patched_container_request)

Patch containers

Patch containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_container_request import PatchedContainerRequest
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    patched_container_request = [io_amr_gwm.PatchedContainerRequest()] # List[PatchedContainerRequest] | 

    try:
        # Patch containers
        api_instance.v1_containers_bulk_patch_update_partial_update(patched_container_request)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_container_request** | [**List[PatchedContainerRequest]**](PatchedContainerRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_containers_count_retrieve**
> int v1_containers_count_retrieve(descriptor=descriptor, descriptor_group=descriptor_group, id=id, name=name, type=type)



Manage Containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    descriptor = [io_amr_gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    descriptor_group = ['descriptor_group_example'] # List[str] |  (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.v1_containers_count_retrieve(descriptor=descriptor, descriptor_group=descriptor_group, id=id, name=name, type=type)
        print("The response of ContainersAppContainerMasterApi->v1_containers_count_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_count_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **descriptor_group** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

**int**

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

# **v1_containers_create**
> PaginatedContainerList v1_containers_create(container_request, descriptor=descriptor, descriptor_group=descriptor_group, id=id, name=name, page=page, page_size=page_size, type=type)

Create containers

Create containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container_request import ContainerRequest
from io_amr_gwm.models.paginated_container_list import PaginatedContainerList
from io_amr_gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    container_request = [io_amr_gwm.ContainerRequest()] # List[ContainerRequest] | 
    descriptor = [io_amr_gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    descriptor_group = ['descriptor_group_example'] # List[str] |  (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = 'type_example' # str |  (optional)

    try:
        # Create containers
        api_response = api_instance.v1_containers_create(container_request, descriptor=descriptor, descriptor_group=descriptor_group, id=id, name=name, page=page, page_size=page_size, type=type)
        print("The response of ContainersAppContainerMasterApi->v1_containers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_request** | [**List[ContainerRequest]**](ContainerRequest.md)|  | 
 **descriptor** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **descriptor_group** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**PaginatedContainerList**](PaginatedContainerList.md)

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

# **v1_containers_delete_destroy**
> v1_containers_delete_destroy(descriptor=descriptor, id=id, name=name)

Bulk Delete Containers

Bulk Delete  Containers

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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    descriptor = ['descriptor_example'] # List[str] | List of 'Container Descriptor IDs' or 'Container Descriptor names' (optional)
    id = [3.4] # List[float] | List of Container IDs (optional)
    name = ['name_example'] # List[str] | List of Container names (optional)

    try:
        # Bulk Delete Containers
        api_instance.v1_containers_delete_destroy(descriptor=descriptor, id=id, name=name)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor** | [**List[str]**](str.md)| List of &#39;Container Descriptor IDs&#39; or &#39;Container Descriptor names&#39; | [optional] 
 **id** | [**List[float]**](float.md)| List of Container IDs | [optional] 
 **name** | [**List[str]**](str.md)| List of Container names | [optional] 

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

# **v1_containers_destroy**
> v1_containers_destroy(id_or_name)



List containers

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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    id_or_name = '1' # str | Container ID or Name.

    try:
        api_instance.v1_containers_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Container ID or Name. | 

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

# **v1_containers_list**
> PaginatedContainerList v1_containers_list(descriptor=descriptor, descriptor_group=descriptor_group, id=id, meta_data=meta_data, name=name, page=page, page_size=page_size, type=type)



List containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_container_list import PaginatedContainerList
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    descriptor = ['descriptor_example'] # List[str] | List of 'Container Descriptor IDs' or 'Container Descriptor names' (optional)
    descriptor_group = ['descriptor_group_example'] # List[str] |  (optional)
    id = [3.4] # List[float] | List of Container IDs (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = ['name_example'] # List[str] | List of Container names (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.v1_containers_list(descriptor=descriptor, descriptor_group=descriptor_group, id=id, meta_data=meta_data, name=name, page=page, page_size=page_size, type=type)
        print("The response of ContainersAppContainerMasterApi->v1_containers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descriptor** | [**List[str]**](str.md)| List of &#39;Container Descriptor IDs&#39; or &#39;Container Descriptor names&#39; | [optional] 
 **descriptor_group** | [**List[str]**](str.md)|  | [optional] 
 **id** | [**List[float]**](float.md)| List of Container IDs | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **name** | [**List[str]**](str.md)| List of Container names | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**PaginatedContainerList**](PaginatedContainerList.md)

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

# **v1_containers_partial_update**
> Container v1_containers_partial_update(id_or_name, patched_container_request=patched_container_request)



List containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container import Container
from io_amr_gwm.models.patched_container_request import PatchedContainerRequest
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    id_or_name = '1' # str | Container ID or Name.
    patched_container_request = io_amr_gwm.PatchedContainerRequest() # PatchedContainerRequest |  (optional)

    try:
        api_response = api_instance.v1_containers_partial_update(id_or_name, patched_container_request=patched_container_request)
        print("The response of ContainersAppContainerMasterApi->v1_containers_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Container ID or Name. | 
 **patched_container_request** | [**PatchedContainerRequest**](PatchedContainerRequest.md)|  | [optional] 

### Return type

[**Container**](Container.md)

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

# **v1_containers_retrieve**
> Container v1_containers_retrieve(id_or_name)



List containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container import Container
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    id_or_name = '1' # str | Container ID or Name.

    try:
        api_response = api_instance.v1_containers_retrieve(id_or_name)
        print("The response of ContainersAppContainerMasterApi->v1_containers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Container ID or Name. | 

### Return type

[**Container**](Container.md)

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

# **v1_containers_update**
> Container v1_containers_update(id_or_name, container_request)



List containers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.container import Container
from io_amr_gwm.models.container_request import ContainerRequest
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
    api_instance = io_amr_gwm.ContainersAppContainerMasterApi(api_client)
    id_or_name = '1' # str | Container ID or Name.
    container_request = io_amr_gwm.ContainerRequest() # ContainerRequest | 

    try:
        api_response = api_instance.v1_containers_update(id_or_name, container_request)
        print("The response of ContainersAppContainerMasterApi->v1_containers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppContainerMasterApi->v1_containers_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Container ID or Name. | 
 **container_request** | [**ContainerRequest**](ContainerRequest.md)|  | 

### Return type

[**Container**](Container.md)

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

