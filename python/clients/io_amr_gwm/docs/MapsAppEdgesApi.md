# io_amr_gwm.MapsAppEdgesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_map_edge_create**](MapsAppEdgesApi.md#v1_map_edge_create) | **POST** /v1/map/{map_id_or_name}/edge | 
[**v1_map_edge_delete_destroy**](MapsAppEdgesApi.md#v1_map_edge_delete_destroy) | **DELETE** /v1/map/{map_id_or_name}/edge/delete | 
[**v1_map_edge_destroy**](MapsAppEdgesApi.md#v1_map_edge_destroy) | **DELETE** /v1/map/{map_id_or_name}/edge/{id} | 
[**v1_map_edge_list**](MapsAppEdgesApi.md#v1_map_edge_list) | **GET** /v1/map/{map_id_or_name}/edge | 
[**v1_map_edge_partial_update**](MapsAppEdgesApi.md#v1_map_edge_partial_update) | **PATCH** /v1/map/{map_id_or_name}/edge/{id} | 
[**v1_map_edge_retrieve**](MapsAppEdgesApi.md#v1_map_edge_retrieve) | **GET** /v1/map/{map_id_or_name}/edge/{id} | 


# **v1_map_edge_create**
> List[Edge] v1_map_edge_create(map_id_or_name, edge_request, intersects_region=intersects_region, node=node, within_region=within_region)



Manage Routing Graph Edges

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.edge import Edge
from io_amr_gwm.models.edge_request import EdgeRequest
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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    edge_request = [io_amr_gwm.EdgeRequest()] # List[EdgeRequest] | 
    intersects_region = 'intersects_region_example' # str |  (optional)
    node = 'node_example' # str |  (optional)
    within_region = 'within_region_example' # str |  (optional)

    try:
        api_response = api_instance.v1_map_edge_create(map_id_or_name, edge_request, intersects_region=intersects_region, node=node, within_region=within_region)
        print("The response of MapsAppEdgesApi->v1_map_edge_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **edge_request** | [**List[EdgeRequest]**](EdgeRequest.md)|  | 
 **intersects_region** | **str**|  | [optional] 
 **node** | **str**|  | [optional] 
 **within_region** | **str**|  | [optional] 

### Return type

[**List[Edge]**](Edge.md)

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

# **v1_map_edge_delete_destroy**
> v1_map_edge_delete_destroy(map_id_or_name, force=force)



Manage Routing Graph Edges

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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    force = True # bool | force clear all resources, including preserved ones (optional)

    try:
        api_instance.v1_map_edge_delete_destroy(map_id_or_name, force=force)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **force** | **bool**| force clear all resources, including preserved ones | [optional] 

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

# **v1_map_edge_destroy**
> v1_map_edge_destroy(id, map_id_or_name)



Manage Routing Graph Edges

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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    id = 56 # int | A unique integer value identifying this edge.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_instance.v1_map_edge_destroy(id, map_id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edge. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

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

# **v1_map_edge_list**
> List[Edge] v1_map_edge_list(map_id_or_name, intersects_region=intersects_region, node=node, within_region=within_region)



Manage Routing Graph Edges

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.edge import Edge
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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    intersects_region = 'intersects_region_example' # str | filter edges which are crossing a region with id or name (optional)
    node = 56 # int | filter edges connected to the node (optional)
    within_region = 'within_region_example' # str | filter edges which are within a region with id or name (optional)

    try:
        api_response = api_instance.v1_map_edge_list(map_id_or_name, intersects_region=intersects_region, node=node, within_region=within_region)
        print("The response of MapsAppEdgesApi->v1_map_edge_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **intersects_region** | **str**| filter edges which are crossing a region with id or name | [optional] 
 **node** | **int**| filter edges connected to the node | [optional] 
 **within_region** | **str**| filter edges which are within a region with id or name | [optional] 

### Return type

[**List[Edge]**](Edge.md)

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

# **v1_map_edge_partial_update**
> Edge v1_map_edge_partial_update(id, map_id_or_name, patched_edge_request=patched_edge_request)



Manage Routing Graph Edges

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.edge import Edge
from io_amr_gwm.models.patched_edge_request import PatchedEdgeRequest
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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    id = 56 # int | A unique integer value identifying this edge.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    patched_edge_request = io_amr_gwm.PatchedEdgeRequest() # PatchedEdgeRequest |  (optional)

    try:
        api_response = api_instance.v1_map_edge_partial_update(id, map_id_or_name, patched_edge_request=patched_edge_request)
        print("The response of MapsAppEdgesApi->v1_map_edge_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edge. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **patched_edge_request** | [**PatchedEdgeRequest**](PatchedEdgeRequest.md)|  | [optional] 

### Return type

[**Edge**](Edge.md)

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

# **v1_map_edge_retrieve**
> Edge v1_map_edge_retrieve(id, map_id_or_name)



Manage Routing Graph Edges

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.edge import Edge
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
    api_instance = io_amr_gwm.MapsAppEdgesApi(api_client)
    id = 56 # int | A unique integer value identifying this edge.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_edge_retrieve(id, map_id_or_name)
        print("The response of MapsAppEdgesApi->v1_map_edge_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppEdgesApi->v1_map_edge_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edge. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**Edge**](Edge.md)

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

