# io_amr_gwm.ContainersAppAssetLocationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_asset_locations_bulk_patch_update_partial_update**](ContainersAppAssetLocationApi.md#v1_asset_locations_bulk_patch_update_partial_update) | **PATCH** /v1/asset_locations/bulk_patch_update | Patch asset locations
[**v1_asset_locations_create**](ContainersAppAssetLocationApi.md#v1_asset_locations_create) | **POST** /v1/asset_locations | Create asset locations
[**v1_asset_locations_delete_destroy**](ContainersAppAssetLocationApi.md#v1_asset_locations_delete_destroy) | **DELETE** /v1/asset_locations/delete | Bulk Delete asset locations
[**v1_asset_locations_destroy**](ContainersAppAssetLocationApi.md#v1_asset_locations_destroy) | **DELETE** /v1/asset_locations/{id} | 
[**v1_asset_locations_list**](ContainersAppAssetLocationApi.md#v1_asset_locations_list) | **GET** /v1/asset_locations | List asset locations
[**v1_asset_locations_partial_update**](ContainersAppAssetLocationApi.md#v1_asset_locations_partial_update) | **PATCH** /v1/asset_locations/{id} | 
[**v1_asset_locations_retrieve**](ContainersAppAssetLocationApi.md#v1_asset_locations_retrieve) | **GET** /v1/asset_locations/{id} | 
[**v1_asset_locations_update**](ContainersAppAssetLocationApi.md#v1_asset_locations_update) | **PUT** /v1/asset_locations/{id} | 


# **v1_asset_locations_bulk_patch_update_partial_update**
> v1_asset_locations_bulk_patch_update_partial_update(patched_asset_location_patch_request)

Patch asset locations

Patch asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_asset_location_patch_request import PatchedAssetLocationPatchRequest
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    patched_asset_location_patch_request = [io_amr_gwm.PatchedAssetLocationPatchRequest()] # List[PatchedAssetLocationPatchRequest] | 

    try:
        # Patch asset locations
        api_instance.v1_asset_locations_bulk_patch_update_partial_update(patched_asset_location_patch_request)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_asset_location_patch_request** | [**List[PatchedAssetLocationPatchRequest]**](PatchedAssetLocationPatchRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_asset_locations_create**
> PaginatedAssetLocationList v1_asset_locations_create(asset_location_request, container=container, id=id, intersects_region=intersects_region, map=map, page=page, page_size=page_size, position=position, spot=spot, type=type)

Create asset locations

Create asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.asset_location_request import AssetLocationRequest
from io_amr_gwm.models.paginated_asset_location_list import PaginatedAssetLocationList
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    asset_location_request = [io_amr_gwm.AssetLocationRequest()] # List[AssetLocationRequest] | 
    container = [56] # List[int] |  (optional)
    id = [56] # List[int] |  (optional)
    intersects_region = 'intersects_region_example' # str |  (optional)
    map = 56 # int |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    position = ['position_example'] # List[str] | format: x,y,floor (optional)
    spot = [56] # List[int] |  (optional)
    type = ['type_example'] # List[str] |  (optional)

    try:
        # Create asset locations
        api_response = api_instance.v1_asset_locations_create(asset_location_request, container=container, id=id, intersects_region=intersects_region, map=map, page=page, page_size=page_size, position=position, spot=spot, type=type)
        print("The response of ContainersAppAssetLocationApi->v1_asset_locations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_location_request** | [**List[AssetLocationRequest]**](AssetLocationRequest.md)|  | 
 **container** | [**List[int]**](int.md)|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **intersects_region** | **str**|  | [optional] 
 **map** | **int**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **position** | [**List[str]**](str.md)| format: x,y,floor | [optional] 
 **spot** | [**List[int]**](int.md)|  | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedAssetLocationList**](PaginatedAssetLocationList.md)

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

# **v1_asset_locations_delete_destroy**
> v1_asset_locations_delete_destroy(container=container, id=id, intersects_region=intersects_region, map=map, position=position, spot=spot, type=type)

Bulk Delete asset locations

Bulk Delete asset locations

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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    container = [56] # List[int] | List of 'Container IDs' (optional)
    id = [56] # List[int] | List of AssetLocation IDs (optional)
    intersects_region = 56 # int | 'Region ID' or 'Region name (optional)
    map = 56 # int | map of associated spot (optional)
    position = 'position_example' # str | x,y coordinate of associated spot (optional)
    spot = [56] # List[int] | List of 'SpotAnnotation IDs' (optional)
    type = ['type_example'] # List[str] | type of asset location (optional)

    try:
        # Bulk Delete asset locations
        api_instance.v1_asset_locations_delete_destroy(container=container, id=id, intersects_region=intersects_region, map=map, position=position, spot=spot, type=type)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | [**List[int]**](int.md)| List of &#39;Container IDs&#39; | [optional] 
 **id** | [**List[int]**](int.md)| List of AssetLocation IDs | [optional] 
 **intersects_region** | **int**| &#39;Region ID&#39; or &#39;Region name | [optional] 
 **map** | **int**| map of associated spot | [optional] 
 **position** | **str**| x,y coordinate of associated spot | [optional] 
 **spot** | [**List[int]**](int.md)| List of &#39;SpotAnnotation IDs&#39; | [optional] 
 **type** | [**List[str]**](str.md)| type of asset location | [optional] 

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

# **v1_asset_locations_destroy**
> v1_asset_locations_destroy(id)



Manage asset locations

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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    id = 56 # int | A unique integer value identifying this asset location.

    try:
        api_instance.v1_asset_locations_destroy(id)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this asset location. | 

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

# **v1_asset_locations_list**
> PaginatedAssetLocationList v1_asset_locations_list(container=container, id=id, intersects_region=intersects_region, map=map, page=page, page_size=page_size, position=position, spot=spot, type=type)

List asset locations

List asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_asset_location_list import PaginatedAssetLocationList
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    container = [56] # List[int] | List of 'Container IDs' (optional)
    id = [56] # List[int] | List of AssetLocation IDs (optional)
    intersects_region = 56 # int | 'Region ID' or 'Region name (optional)
    map = 56 # int | map of associated spot (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    position = 'position_example' # str | x,y coordinate of associated spot (optional)
    spot = [56] # List[int] | List of 'SpotAnnotation IDs' (optional)
    type = ['type_example'] # List[str] | type of asset location (optional)

    try:
        # List asset locations
        api_response = api_instance.v1_asset_locations_list(container=container, id=id, intersects_region=intersects_region, map=map, page=page, page_size=page_size, position=position, spot=spot, type=type)
        print("The response of ContainersAppAssetLocationApi->v1_asset_locations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | [**List[int]**](int.md)| List of &#39;Container IDs&#39; | [optional] 
 **id** | [**List[int]**](int.md)| List of AssetLocation IDs | [optional] 
 **intersects_region** | **int**| &#39;Region ID&#39; or &#39;Region name | [optional] 
 **map** | **int**| map of associated spot | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **position** | **str**| x,y coordinate of associated spot | [optional] 
 **spot** | [**List[int]**](int.md)| List of &#39;SpotAnnotation IDs&#39; | [optional] 
 **type** | [**List[str]**](str.md)| type of asset location | [optional] 

### Return type

[**PaginatedAssetLocationList**](PaginatedAssetLocationList.md)

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

# **v1_asset_locations_partial_update**
> AssetLocation v1_asset_locations_partial_update(id, patched_asset_location_request=patched_asset_location_request)



Manage asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.asset_location import AssetLocation
from io_amr_gwm.models.patched_asset_location_request import PatchedAssetLocationRequest
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    id = 56 # int | A unique integer value identifying this asset location.
    patched_asset_location_request = io_amr_gwm.PatchedAssetLocationRequest() # PatchedAssetLocationRequest |  (optional)

    try:
        api_response = api_instance.v1_asset_locations_partial_update(id, patched_asset_location_request=patched_asset_location_request)
        print("The response of ContainersAppAssetLocationApi->v1_asset_locations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this asset location. | 
 **patched_asset_location_request** | [**PatchedAssetLocationRequest**](PatchedAssetLocationRequest.md)|  | [optional] 

### Return type

[**AssetLocation**](AssetLocation.md)

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

# **v1_asset_locations_retrieve**
> AssetLocation v1_asset_locations_retrieve(id)



Manage asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.asset_location import AssetLocation
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    id = 56 # int | A unique integer value identifying this asset location.

    try:
        api_response = api_instance.v1_asset_locations_retrieve(id)
        print("The response of ContainersAppAssetLocationApi->v1_asset_locations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this asset location. | 

### Return type

[**AssetLocation**](AssetLocation.md)

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

# **v1_asset_locations_update**
> AssetLocation v1_asset_locations_update(id, asset_location_request)



Manage asset locations

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.asset_location import AssetLocation
from io_amr_gwm.models.asset_location_request import AssetLocationRequest
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
    api_instance = io_amr_gwm.ContainersAppAssetLocationApi(api_client)
    id = 56 # int | A unique integer value identifying this asset location.
    asset_location_request = io_amr_gwm.AssetLocationRequest() # AssetLocationRequest | 

    try:
        api_response = api_instance.v1_asset_locations_update(id, asset_location_request)
        print("The response of ContainersAppAssetLocationApi->v1_asset_locations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppAssetLocationApi->v1_asset_locations_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this asset location. | 
 **asset_location_request** | [**AssetLocationRequest**](AssetLocationRequest.md)|  | 

### Return type

[**AssetLocation**](AssetLocation.md)

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

