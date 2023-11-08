# io_amr_gwm.MapsAppNodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_map_node_bulk_patch_update_partial_update**](MapsAppNodesApi.md#v1_map_node_bulk_patch_update_partial_update) | **PATCH** /v1/map/{map_id_or_name}/node/bulk_patch_update | Patch Map Nodes
[**v1_map_node_count_retrieve**](MapsAppNodesApi.md#v1_map_node_count_retrieve) | **GET** /v1/map/{map_id_or_name}/node/count | 
[**v1_map_node_create**](MapsAppNodesApi.md#v1_map_node_create) | **POST** /v1/map/{map_id_or_name}/node | 
[**v1_map_node_delete_destroy**](MapsAppNodesApi.md#v1_map_node_delete_destroy) | **DELETE** /v1/map/{map_id_or_name}/node/delete | 
[**v1_map_node_destroy**](MapsAppNodesApi.md#v1_map_node_destroy) | **DELETE** /v1/map/{map_id_or_name}/node/{id} | 
[**v1_map_node_list**](MapsAppNodesApi.md#v1_map_node_list) | **GET** /v1/map/{map_id_or_name}/node | 
[**v1_map_node_partial_update**](MapsAppNodesApi.md#v1_map_node_partial_update) | **PATCH** /v1/map/{map_id_or_name}/node/{id} | 
[**v1_map_node_retrieve**](MapsAppNodesApi.md#v1_map_node_retrieve) | **GET** /v1/map/{map_id_or_name}/node/{id} | 


# **v1_map_node_bulk_patch_update_partial_update**
> v1_map_node_bulk_patch_update_partial_update(map_id_or_name, patched_node_request)

Patch Map Nodes

Patch Map Nodes

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_node_request import PatchedNodeRequest
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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    patched_node_request = [io_amr_gwm.PatchedNodeRequest()] # List[PatchedNodeRequest] | 

    try:
        # Patch Map Nodes
        api_instance.v1_map_node_bulk_patch_update_partial_update(map_id_or_name, patched_node_request)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **patched_node_request** | [**List[PatchedNodeRequest]**](PatchedNodeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_map_node_count_retrieve**
> int v1_map_node_count_retrieve(map_id_or_name, edge=edge, intersects_region=intersects_region, position=position, type=type)



Manage Routing Graph Nodes

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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    edge = 'edge_example' # str |  (optional)
    intersects_region = 'intersects_region_example' # str |  (optional)
    position = ['position_example'] # List[str] | format: x,y,floor (optional)
    type = ['type_example'] # List[str] | User defined node type (optional)

    try:
        api_response = api_instance.v1_map_node_count_retrieve(map_id_or_name, edge=edge, intersects_region=intersects_region, position=position, type=type)
        print("The response of MapsAppNodesApi->v1_map_node_count_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_count_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **edge** | **str**|  | [optional] 
 **intersects_region** | **str**|  | [optional] 
 **position** | [**List[str]**](str.md)| format: x,y,floor | [optional] 
 **type** | [**List[str]**](str.md)| User defined node type | [optional] 

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

# **v1_map_node_create**
> List[Node] v1_map_node_create(map_id_or_name, node_request, edge=edge, intersects_region=intersects_region, position=position, type=type)



Manage Routing Graph Nodes

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.node import Node
from io_amr_gwm.models.node_request import NodeRequest
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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    node_request = [io_amr_gwm.NodeRequest()] # List[NodeRequest] | 
    edge = 'edge_example' # str |  (optional)
    intersects_region = 'intersects_region_example' # str |  (optional)
    position = ['position_example'] # List[str] | format: x,y,floor (optional)
    type = ['type_example'] # List[str] | User defined node type (optional)

    try:
        api_response = api_instance.v1_map_node_create(map_id_or_name, node_request, edge=edge, intersects_region=intersects_region, position=position, type=type)
        print("The response of MapsAppNodesApi->v1_map_node_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **node_request** | [**List[NodeRequest]**](NodeRequest.md)|  | 
 **edge** | **str**|  | [optional] 
 **intersects_region** | **str**|  | [optional] 
 **position** | [**List[str]**](str.md)| format: x,y,floor | [optional] 
 **type** | [**List[str]**](str.md)| User defined node type | [optional] 

### Return type

[**List[Node]**](Node.md)

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

# **v1_map_node_delete_destroy**
> v1_map_node_delete_destroy(map_id_or_name, force=force)



Manage Routing Graph Nodes

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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    force = True # bool | force clear all resources, including preserved ones (optional)

    try:
        api_instance.v1_map_node_delete_destroy(map_id_or_name, force=force)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_delete_destroy: %s\n" % e)
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

# **v1_map_node_destroy**
> v1_map_node_destroy(id, map_id_or_name)



Manage Routing Graph Nodes

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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    id = 56 # int | A unique integer value identifying this node.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_instance.v1_map_node_destroy(id, map_id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this node. | 
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

# **v1_map_node_list**
> List[NodeDbJson] v1_map_node_list(map_id_or_name, edge=edge, intersects_region=intersects_region, meta_data=meta_data, position=position, type=type)



List Nodes

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.node_db_json import NodeDbJson
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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    edge = 56 # int | filter nodes which touch edge with id (optional)
    intersects_region = 'intersects_region_example' # str | filter nodes which are contained within region with name or id (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    position = 'position_example' # str | x,y coordinate of node (optional)
    type = ['type_example'] # List[str] | filter regions by type(s) (optional)

    try:
        api_response = api_instance.v1_map_node_list(map_id_or_name, edge=edge, intersects_region=intersects_region, meta_data=meta_data, position=position, type=type)
        print("The response of MapsAppNodesApi->v1_map_node_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **edge** | **int**| filter nodes which touch edge with id | [optional] 
 **intersects_region** | **str**| filter nodes which are contained within region with name or id | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **position** | **str**| x,y coordinate of node | [optional] 
 **type** | [**List[str]**](str.md)| filter regions by type(s) | [optional] 

### Return type

[**List[NodeDbJson]**](NodeDbJson.md)

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

# **v1_map_node_partial_update**
> Node v1_map_node_partial_update(id, map_id_or_name, patched_node_request=patched_node_request)



Manage Routing Graph Nodes

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.node import Node
from io_amr_gwm.models.patched_node_request import PatchedNodeRequest
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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    id = 56 # int | A unique integer value identifying this node.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    patched_node_request = io_amr_gwm.PatchedNodeRequest() # PatchedNodeRequest |  (optional)

    try:
        api_response = api_instance.v1_map_node_partial_update(id, map_id_or_name, patched_node_request=patched_node_request)
        print("The response of MapsAppNodesApi->v1_map_node_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this node. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **patched_node_request** | [**PatchedNodeRequest**](PatchedNodeRequest.md)|  | [optional] 

### Return type

[**Node**](Node.md)

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

# **v1_map_node_retrieve**
> Node v1_map_node_retrieve(id, map_id_or_name)



Manage Routing Graph Nodes

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.node import Node
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
    api_instance = io_amr_gwm.MapsAppNodesApi(api_client)
    id = 56 # int | A unique integer value identifying this node.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_node_retrieve(id, map_id_or_name)
        print("The response of MapsAppNodesApi->v1_map_node_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppNodesApi->v1_map_node_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this node. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**Node**](Node.md)

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

