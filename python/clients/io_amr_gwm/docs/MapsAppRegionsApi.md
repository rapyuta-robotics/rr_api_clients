# openapi_client.MapsAppRegionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_region_create**](MapsAppRegionsApi.md#v1_region_create) | **POST** /v1/region | 
[**v1_region_delete_destroy**](MapsAppRegionsApi.md#v1_region_delete_destroy) | **DELETE** /v1/region/delete | 
[**v1_region_destroy**](MapsAppRegionsApi.md#v1_region_destroy) | **DELETE** /v1/region/{id_or_name} | 
[**v1_region_list**](MapsAppRegionsApi.md#v1_region_list) | **GET** /v1/region | 
[**v1_region_partial_update**](MapsAppRegionsApi.md#v1_region_partial_update) | **PATCH** /v1/region/{id_or_name} | 
[**v1_region_retrieve**](MapsAppRegionsApi.md#v1_region_retrieve) | **GET** /v1/region/{id_or_name} | 
[**v1_region_update**](MapsAppRegionsApi.md#v1_region_update) | **PUT** /v1/region/{id_or_name} | 


# **v1_region_create**
> Region v1_region_create(region_request)



Manage Regions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.region import Region
from openapi_client.models.region_request import RegionRequest
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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    region_request = openapi_client.RegionRequest() # RegionRequest | 

    try:
        api_response = api_instance.v1_region_create(region_request)
        print("The response of MapsAppRegionsApi->v1_region_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_request** | [**RegionRequest**](RegionRequest.md)|  | 

### Return type

[**Region**](Region.md)

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

# **v1_region_delete_destroy**
> v1_region_delete_destroy(map_id, force=force, type=type)



Manage Regions

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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    map_id = 'map_id_example' # str | 
    force = True # bool | force clear all resources, including preserved ones (optional)
    type = 'type_example' # str | delete resources by type (optional)

    try:
        api_instance.v1_region_delete_destroy(map_id, force=force, type=type)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **force** | **bool**| force clear all resources, including preserved ones | [optional] 
 **type** | **str**| delete resources by type | [optional] 

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

# **v1_region_destroy**
> v1_region_destroy(id_or_name)



Manage Regions

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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    id_or_name = '1' # str | Region ID or Name.

    try:
        api_instance.v1_region_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Region ID or Name. | 

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

# **v1_region_list**
> List[RegionDbJson] v1_region_list(contains_point=contains_point, external_device=external_device, id=id, intersects_region=intersects_region, map=map, name=name, preserve=preserve, type=type, within_region=within_region)



List Regions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.region_db_json import RegionDbJson
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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    contains_point = 'contains_point_example' # str | find all regions that contain the point in format : `X,Y` (optional)
    external_device = ['external_device_example'] # List[str] | filter regions by associated external devices (optional)
    id = [56] # List[int] | filter regions by id (optional)
    intersects_region = 'intersects_region_example' # str | filter regions that intersect with region with given name or id (optional)
    map = ['map_example'] # List[str] | filter regions by maps (optional)
    name = ['name_example'] # List[str] | filter regions by name(s) (optional)
    preserve = True # bool |  (optional)
    type = ['type_example'] # List[str] | filter regions by type(s) (optional)
    within_region = 'within_region_example' # str | filter regions that is included by region with given name or id (optional)

    try:
        api_response = api_instance.v1_region_list(contains_point=contains_point, external_device=external_device, id=id, intersects_region=intersects_region, map=map, name=name, preserve=preserve, type=type, within_region=within_region)
        print("The response of MapsAppRegionsApi->v1_region_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contains_point** | **str**| find all regions that contain the point in format : &#x60;X,Y&#x60; | [optional] 
 **external_device** | [**List[str]**](str.md)| filter regions by associated external devices | [optional] 
 **id** | [**List[int]**](int.md)| filter regions by id | [optional] 
 **intersects_region** | **str**| filter regions that intersect with region with given name or id | [optional] 
 **map** | [**List[str]**](str.md)| filter regions by maps | [optional] 
 **name** | [**List[str]**](str.md)| filter regions by name(s) | [optional] 
 **preserve** | **bool**|  | [optional] 
 **type** | [**List[str]**](str.md)| filter regions by type(s) | [optional] 
 **within_region** | **str**| filter regions that is included by region with given name or id | [optional] 

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

# **v1_region_partial_update**
> Region v1_region_partial_update(id_or_name, patched_region_request=patched_region_request)



Manage Regions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.patched_region_request import PatchedRegionRequest
from openapi_client.models.region import Region
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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    id_or_name = '1' # str | Region ID or Name.
    patched_region_request = openapi_client.PatchedRegionRequest() # PatchedRegionRequest |  (optional)

    try:
        api_response = api_instance.v1_region_partial_update(id_or_name, patched_region_request=patched_region_request)
        print("The response of MapsAppRegionsApi->v1_region_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Region ID or Name. | 
 **patched_region_request** | [**PatchedRegionRequest**](PatchedRegionRequest.md)|  | [optional] 

### Return type

[**Region**](Region.md)

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

# **v1_region_retrieve**
> Region v1_region_retrieve(id_or_name)



Manage Regions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.region import Region
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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    id_or_name = '1' # str | Region ID or Name.

    try:
        api_response = api_instance.v1_region_retrieve(id_or_name)
        print("The response of MapsAppRegionsApi->v1_region_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Region ID or Name. | 

### Return type

[**Region**](Region.md)

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

# **v1_region_update**
> Region v1_region_update(id_or_name, region_request)



Manage Regions

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.region import Region
from openapi_client.models.region_request import RegionRequest
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
    api_instance = openapi_client.MapsAppRegionsApi(api_client)
    id_or_name = '1' # str | Region ID or Name.
    region_request = openapi_client.RegionRequest() # RegionRequest | 

    try:
        api_response = api_instance.v1_region_update(id_or_name, region_request)
        print("The response of MapsAppRegionsApi->v1_region_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppRegionsApi->v1_region_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Region ID or Name. | 
 **region_request** | [**RegionRequest**](RegionRequest.md)|  | 

### Return type

[**Region**](Region.md)

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

