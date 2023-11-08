# openapi_client.MapsAppMapsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_map_clear_graph_destroy**](MapsAppMapsApi.md#v1_map_clear_graph_destroy) | **DELETE** /v1/map/{id_or_name}/clear_graph | 
[**v1_map_clear_spots_destroy**](MapsAppMapsApi.md#v1_map_clear_spots_destroy) | **DELETE** /v1/map/{id_or_name}/clear_spots | 
[**v1_map_create**](MapsAppMapsApi.md#v1_map_create) | **POST** /v1/map | 
[**v1_map_destroy**](MapsAppMapsApi.md#v1_map_destroy) | **DELETE** /v1/map/{id_or_name} | 
[**v1_map_list**](MapsAppMapsApi.md#v1_map_list) | **GET** /v1/map | 
[**v1_map_partial_update**](MapsAppMapsApi.md#v1_map_partial_update) | **PATCH** /v1/map/{id_or_name} | 
[**v1_map_retrieve**](MapsAppMapsApi.md#v1_map_retrieve) | **GET** /v1/map/{id_or_name} | 
[**v1_map_status_retrieve**](MapsAppMapsApi.md#v1_map_status_retrieve) | **GET** /v1/map/{id_or_name}/status | 
[**v1_map_update**](MapsAppMapsApi.md#v1_map_update) | **PUT** /v1/map/{id_or_name} | 
[**v1_map_upload_update**](MapsAppMapsApi.md#v1_map_upload_update) | **PUT** /v1/map/upload | 


# **v1_map_clear_graph_destroy**
> v1_map_clear_graph_destroy(id_or_name)



Generate Routing Graph for Map

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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.

    try:
        api_instance.v1_map_clear_graph_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_clear_graph_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 

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

# **v1_map_clear_spots_destroy**
> v1_map_clear_spots_destroy(id_or_name)



Generate Routing Graph for Map

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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.

    try:
        api_instance.v1_map_clear_spots_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_clear_spots_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 

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

# **v1_map_create**
> Map v1_map_create(map_request=map_request)



Manage Maps

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
from openapi_client.models.map_request import MapRequest
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    map_request = openapi_client.MapRequest() # MapRequest |  (optional)

    try:
        api_response = api_instance.v1_map_create(map_request=map_request)
        print("The response of MapsAppMapsApi->v1_map_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_request** | [**MapRequest**](MapRequest.md)|  | [optional] 

### Return type

[**Map**](Map.md)

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

# **v1_map_destroy**
> v1_map_destroy(id_or_name)



Generate Routing Graph for Map

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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.

    try:
        api_instance.v1_map_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 

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

# **v1_map_list**
> List[Map] v1_map_list()



Manage Maps

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)

    try:
        api_response = api_instance.v1_map_list()
        print("The response of MapsAppMapsApi->v1_map_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Map]**](Map.md)

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

# **v1_map_partial_update**
> MapGraphUpdate v1_map_partial_update(id_or_name, patched_map_graph_update_request=patched_map_graph_update_request)



Generate Routing Graph for Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map_graph_update import MapGraphUpdate
from openapi_client.models.patched_map_graph_update_request import PatchedMapGraphUpdateRequest
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.
    patched_map_graph_update_request = openapi_client.PatchedMapGraphUpdateRequest() # PatchedMapGraphUpdateRequest |  (optional)

    try:
        api_response = api_instance.v1_map_partial_update(id_or_name, patched_map_graph_update_request=patched_map_graph_update_request)
        print("The response of MapsAppMapsApi->v1_map_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 
 **patched_map_graph_update_request** | [**PatchedMapGraphUpdateRequest**](PatchedMapGraphUpdateRequest.md)|  | [optional] 

### Return type

[**MapGraphUpdate**](MapGraphUpdate.md)

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

# **v1_map_retrieve**
> Map v1_map_retrieve(id_or_name)



Generate Routing Graph for Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.

    try:
        api_response = api_instance.v1_map_retrieve(id_or_name)
        print("The response of MapsAppMapsApi->v1_map_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 

### Return type

[**Map**](Map.md)

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

# **v1_map_status_retrieve**
> Map v1_map_status_retrieve(id_or_name)



Generate Routing Graph for Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.

    try:
        api_response = api_instance.v1_map_status_retrieve(id_or_name)
        print("The response of MapsAppMapsApi->v1_map_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_status_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 

### Return type

[**Map**](Map.md)

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

# **v1_map_update**
> Map v1_map_update(id_or_name, map_request=map_request)



Generate Routing Graph for Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
from openapi_client.models.map_request import MapRequest
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    id_or_name = '1' # str | Map ID or Name.
    map_request = openapi_client.MapRequest() # MapRequest |  (optional)

    try:
        api_response = api_instance.v1_map_update(id_or_name, map_request=map_request)
        print("The response of MapsAppMapsApi->v1_map_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Map ID or Name. | 
 **map_request** | [**MapRequest**](MapRequest.md)|  | [optional] 

### Return type

[**Map**](Map.md)

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

# **v1_map_upload_update**
> v1_map_upload_update(map_export_request=map_export_request)



Upload Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.map_export_request import MapExportRequest
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
    api_instance = openapi_client.MapsAppMapsApi(api_client)
    map_export_request = openapi_client.MapExportRequest() # MapExportRequest |  (optional)

    try:
        api_instance.v1_map_upload_update(map_export_request=map_export_request)
    except Exception as e:
        print("Exception when calling MapsAppMapsApi->v1_map_upload_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_export_request** | [**MapExportRequest**](MapExportRequest.md)|  | [optional] 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

