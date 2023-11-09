# gwm_client.GraphGeneratorRegionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_graph_generator_download_aisle_regions_list**](GraphGeneratorRegionsApi.md#v1_graph_generator_download_aisle_regions_list) | **GET** /v1/graph_generator/download_aisle_regions | 
[**v1_graph_generator_generate_aisle_regions_create**](GraphGeneratorRegionsApi.md#v1_graph_generator_generate_aisle_regions_create) | **POST** /v1/graph_generator/generate_aisle_regions | 
[**v1_graph_generator_upload_aisle_regions_create**](GraphGeneratorRegionsApi.md#v1_graph_generator_upload_aisle_regions_create) | **POST** /v1/graph_generator/upload_aisle_regions | 


# **v1_graph_generator_download_aisle_regions_list**
> List[RegionDbJson] v1_graph_generator_download_aisle_regions_list(map_name)



Download the Aisle Regions of a Map

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.region_db_json import RegionDbJson
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
    api_instance = gwm_client.GraphGeneratorRegionsApi(api_client)
    map_name = 'map_name_example' # str | Map to download the regions from

    try:
        api_response = api_instance.v1_graph_generator_download_aisle_regions_list(map_name)
        print("The response of GraphGeneratorRegionsApi->v1_graph_generator_download_aisle_regions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorRegionsApi->v1_graph_generator_download_aisle_regions_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to download the regions from | 

### Return type

[**List[RegionDbJson]**](RegionDbJson.md)

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

# **v1_graph_generator_generate_aisle_regions_create**
> Region v1_graph_generator_generate_aisle_regions_create(map_name, map_layer_name, origin_x, origin_y, resolution=resolution, min_aisle_width=min_aisle_width, min_shelf_area=min_shelf_area, min_shelf_ratio=min_shelf_ratio, shelf_approx=shelf_approx)



### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.region import Region
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
    api_instance = gwm_client.GraphGeneratorRegionsApi(api_client)
    map_name = 'map_name_example' # str | 
    map_layer_name = 'map_layer_name_example' # str | 
    origin_x = 3.4 # float | 
    origin_y = 3.4 # float | 
    resolution = 0.05 # float |  (optional) (default to 0.05)
    min_aisle_width = 0.5 # float |  (optional) (default to 0.5)
    min_shelf_area = 1.0 # float |  (optional) (default to 1.0)
    min_shelf_ratio = 1.5 # float |  (optional) (default to 1.5)
    shelf_approx = 1.0 # float |  (optional) (default to 1.0)

    try:
        api_response = api_instance.v1_graph_generator_generate_aisle_regions_create(map_name, map_layer_name, origin_x, origin_y, resolution=resolution, min_aisle_width=min_aisle_width, min_shelf_area=min_shelf_area, min_shelf_ratio=min_shelf_ratio, shelf_approx=shelf_approx)
        print("The response of GraphGeneratorRegionsApi->v1_graph_generator_generate_aisle_regions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphGeneratorRegionsApi->v1_graph_generator_generate_aisle_regions_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**|  | 
 **map_layer_name** | **str**|  | 
 **origin_x** | **float**|  | 
 **origin_y** | **float**|  | 
 **resolution** | **float**|  | [optional] [default to 0.05]
 **min_aisle_width** | **float**|  | [optional] [default to 0.5]
 **min_shelf_area** | **float**|  | [optional] [default to 1.0]
 **min_shelf_ratio** | **float**|  | [optional] [default to 1.5]
 **shelf_approx** | **float**|  | [optional] [default to 1.0]

### Return type

[**Region**](Region.md)

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

# **v1_graph_generator_upload_aisle_regions_create**
> v1_graph_generator_upload_aisle_regions_create(map_name, aisle_regions)



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
    api_instance = gwm_client.GraphGeneratorRegionsApi(api_client)
    map_name = 'map_name_example' # str | Map to upload the regions to
    aisle_regions = None # bytearray | 

    try:
        api_instance.v1_graph_generator_upload_aisle_regions_create(map_name, aisle_regions)
    except Exception as e:
        print("Exception when calling GraphGeneratorRegionsApi->v1_graph_generator_upload_aisle_regions_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_name** | **str**| Map to upload the regions to | 
 **aisle_regions** | **bytearray**|  | 

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
**200** | Posted regions to GWM |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

