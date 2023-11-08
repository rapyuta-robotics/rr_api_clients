# gwm.GraphGeneratorGraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_graph_generator_download_graph_retrieve**](GraphGeneratorGraphApi.md#v1_graph_generator_download_graph_retrieve) | **GET** /v1/graph_generator/download_graph | 
[**v1_graph_generator_generate_graph_create**](GraphGeneratorGraphApi.md#v1_graph_generator_generate_graph_create) | **POST** /v1/graph_generator/generate_graph | 
[**v1_graph_generator_upload_graph_create**](GraphGeneratorGraphApi.md#v1_graph_generator_upload_graph_create) | **POST** /v1/graph_generator/upload_graph | 


# **v1_graph_generator_download_graph_retrieve**
> DownloadGraphResponse v1_graph_generator_download_graph_retrieve(map_name)



Download the Nodes and Edges of a Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.download_graph_response import DownloadGraphResponse
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
    api_instance = gwm.GraphGeneratorGraphApi(api_client)
    map_name = 'map_name_example' # str | Map to download the graph from

    try:
        api_response = api_instance.v1_graph_generator_download_graph_retrieve(map_name)
        print("The response of GraphGeneratorGraphApi->v1_graph_generator_download_graph_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorGraphApi->v1_graph_generator_download_graph_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to download the graph from | 

### Return type

[**DownloadGraphResponse**](DownloadGraphResponse.md)

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

# **v1_graph_generator_generate_graph_create**
> bytearray v1_graph_generator_generate_graph_create(map_name, layer_name, graph_generator)



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
    api_instance = gwm.GraphGeneratorGraphApi(api_client)
    map_name = 'map_name_example' # str | 
    layer_name = 'layer_name_example' # str | 
    graph_generator = None # bytearray | 

    try:
        api_response = api_instance.v1_graph_generator_generate_graph_create(map_name, layer_name, graph_generator)
        print("The response of GraphGeneratorGraphApi->v1_graph_generator_generate_graph_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorGraphApi->v1_graph_generator_generate_graph_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**|  | 
 **layer_name** | **str**|  | 
 **graph_generator** | **bytearray**|  | 

### Return type

**bytearray**

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_graph_generator_upload_graph_create**
> v1_graph_generator_upload_graph_create(map_name, graph)



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
    api_instance = gwm.GraphGeneratorGraphApi(api_client)
    map_name = 'map_name_example' # str | Map to upload the graph to
    graph = None # bytearray | 

    try:
        api_instance.v1_graph_generator_upload_graph_create(map_name, graph)
    except Exception as e:
        print("Exception when calling GraphGeneratorGraphApi->v1_graph_generator_upload_graph_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to upload the graph to | 
 **graph** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted nodes and edges to GWM |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

