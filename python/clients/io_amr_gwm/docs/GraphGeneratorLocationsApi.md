# openapi_client.GraphGeneratorLocationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_graph_generator_download_spots_list**](GraphGeneratorLocationsApi.md#v1_graph_generator_download_spots_list) | **GET** /v1/graph_generator/download_spots | 
[**v1_graph_generator_generate_locations_create**](GraphGeneratorLocationsApi.md#v1_graph_generator_generate_locations_create) | **POST** /v1/graph_generator/generate_locations | 
[**v1_graph_generator_upload_spots_create**](GraphGeneratorLocationsApi.md#v1_graph_generator_upload_spots_create) | **POST** /v1/graph_generator/upload_spots | 


# **v1_graph_generator_download_spots_list**
> List[SpotAnnotationDbJson] v1_graph_generator_download_spots_list(map_name)



Download the Spots of a Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.spot_annotation_db_json import SpotAnnotationDbJson
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
    api_instance = openapi_client.GraphGeneratorLocationsApi(api_client)
    map_name = 'map_name_example' # str | Map to download the spots from

    try:
        api_response = api_instance.v1_graph_generator_download_spots_list(map_name)
        print("The response of GraphGeneratorLocationsApi->v1_graph_generator_download_spots_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorLocationsApi->v1_graph_generator_download_spots_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to download the spots from | 

### Return type

[**List[SpotAnnotationDbJson]**](SpotAnnotationDbJson.md)

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

# **v1_graph_generator_generate_locations_create**
> SpotAnnotation v1_graph_generator_generate_locations_create(map_name, rack_mapping)



### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.spot_annotation import SpotAnnotation
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
    api_instance = openapi_client.GraphGeneratorLocationsApi(api_client)
    map_name = 'map_name_example' # str | 
    rack_mapping = None # bytearray | 

    try:
        api_response = api_instance.v1_graph_generator_generate_locations_create(map_name, rack_mapping)
        print("The response of GraphGeneratorLocationsApi->v1_graph_generator_generate_locations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorLocationsApi->v1_graph_generator_generate_locations_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**|  | 
 **rack_mapping** | **bytearray**|  | 

### Return type

[**SpotAnnotation**](SpotAnnotation.md)

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

# **v1_graph_generator_upload_spots_create**
> v1_graph_generator_upload_spots_create(map_name, spots)



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
    api_instance = openapi_client.GraphGeneratorLocationsApi(api_client)
    map_name = 'map_name_example' # str | Map to upload the spots to
    spots = None # bytearray | 

    try:
        api_instance.v1_graph_generator_upload_spots_create(map_name, spots)
    except Exception as e:
        print("Exception when calling GraphGeneratorLocationsApi->v1_graph_generator_upload_spots_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to upload the spots to | 
 **spots** | **bytearray**|  | 

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
**200** | Posted spots to GWM |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

