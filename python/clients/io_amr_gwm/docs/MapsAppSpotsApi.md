# openapi_client.MapsAppSpotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_spot_bulk_patch_update_partial_update**](MapsAppSpotsApi.md#v1_spot_bulk_patch_update_partial_update) | **PATCH** /v1/spot/bulk_patch_update | Patch Spots
[**v1_spot_create**](MapsAppSpotsApi.md#v1_spot_create) | **POST** /v1/spot | 
[**v1_spot_delete_destroy**](MapsAppSpotsApi.md#v1_spot_delete_destroy) | **DELETE** /v1/spot/delete | 
[**v1_spot_destroy**](MapsAppSpotsApi.md#v1_spot_destroy) | **DELETE** /v1/spot/{id_or_name} | 
[**v1_spot_list**](MapsAppSpotsApi.md#v1_spot_list) | **GET** /v1/spot | 
[**v1_spot_partial_update**](MapsAppSpotsApi.md#v1_spot_partial_update) | **PATCH** /v1/spot/{id_or_name} | 
[**v1_spot_retrieve**](MapsAppSpotsApi.md#v1_spot_retrieve) | **GET** /v1/spot/{id_or_name} | 


# **v1_spot_bulk_patch_update_partial_update**
> v1_spot_bulk_patch_update_partial_update(patched_spot_annotation_update_request)

Patch Spots

Patch Spots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.patched_spot_annotation_update_request import PatchedSpotAnnotationUpdateRequest
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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    patched_spot_annotation_update_request = [openapi_client.PatchedSpotAnnotationUpdateRequest()] # List[PatchedSpotAnnotationUpdateRequest] | 

    try:
        # Patch Spots
        api_instance.v1_spot_bulk_patch_update_partial_update(patched_spot_annotation_update_request)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_spot_annotation_update_request** | [**List[PatchedSpotAnnotationUpdateRequest]**](PatchedSpotAnnotationUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_spot_create**
> List[SpotAnnotation] v1_spot_create(spot_annotation_request, allocatable=allocatable, external_device=external_device, id=id, intersects_region=intersects_region, map=map, name=name, node=node, position=position, type=type)



Manage Spots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.spot_annotation import SpotAnnotation
from openapi_client.models.spot_annotation_request import SpotAnnotationRequest
from openapi_client.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    spot_annotation_request = [openapi_client.SpotAnnotationRequest()] # List[SpotAnnotationRequest] | 
    allocatable = True # bool |  (optional)
    external_device = [openapi_client.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    id = [56] # List[int] | user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer (optional)
    intersects_region = 'intersects_region_example' # str |  (optional)
    map = [openapi_client.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    name = ['name_example'] # List[str] | user defined `name` of this object. Must be unique in the site or map (for nodes and edges) (optional)
    node = [openapi_client.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    position = ['position_example'] # List[str] | format: x,y,floor (optional)
    type = ['type_example'] # List[str] | User defined spot type (optional)

    try:
        api_response = api_instance.v1_spot_create(spot_annotation_request, allocatable=allocatable, external_device=external_device, id=id, intersects_region=intersects_region, map=map, name=name, node=node, position=position, type=type)
        print("The response of MapsAppSpotsApi->v1_spot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_annotation_request** | [**List[SpotAnnotationRequest]**](SpotAnnotationRequest.md)|  | 
 **allocatable** | **bool**|  | [optional] 
 **external_device** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **id** | [**List[int]**](int.md)| user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
 **intersects_region** | **str**|  | [optional] 
 **map** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **name** | [**List[str]**](str.md)| user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
 **node** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **position** | [**List[str]**](str.md)| format: x,y,floor | [optional] 
 **type** | [**List[str]**](str.md)| User defined spot type | [optional] 

### Return type

[**List[SpotAnnotation]**](SpotAnnotation.md)

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

# **v1_spot_delete_destroy**
> v1_spot_delete_destroy(map_id, force=force, type=type)



Manage Spots

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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    map_id = 'map_id_example' # str | 
    force = True # bool | force clear all resources, including preserved ones (optional)
    type = 'type_example' # str | delete resources by type (optional)

    try:
        api_instance.v1_spot_delete_destroy(map_id, force=force, type=type)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_delete_destroy: %s\n" % e)
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

# **v1_spot_destroy**
> v1_spot_destroy(id_or_name)



List Spots

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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    id_or_name = '1' # str | Spot ID or Name.

    try:
        api_instance.v1_spot_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Spot ID or Name. | 

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

# **v1_spot_list**
> List[SpotAnnotation] v1_spot_list(allocatable=allocatable, external_device=external_device, id=id, intersects_region=intersects_region, map=map, meta_data=meta_data, name=name, node=node, position=position, type=type, with_region_ids=with_region_ids)



List Spots

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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    allocatable = True # bool | Filter only allocatable spots (optional)
    external_device = ['external_device_example'] # List[str] | filter spots relative to external devices identified by their name (optional)
    id = [56] # List[int] | filter spot with id (optional)
    intersects_region = 'intersects_region_example' # str | filter spots which are contained within region with id (optional)
    map = ['map_example'] # List[str] | filter spots by maps (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = ['name_example'] # List[str] | filter spots by name(s) (optional)
    node = 56 # int | filter spots by node id (optional)
    position = 'position_example' # str | x,y coordinate of spot (optional)
    type = ['type_example'] # List[str] | filter spots by type(s) (optional)
    with_region_ids = True # bool | add related region ids (optional)

    try:
        api_response = api_instance.v1_spot_list(allocatable=allocatable, external_device=external_device, id=id, intersects_region=intersects_region, map=map, meta_data=meta_data, name=name, node=node, position=position, type=type, with_region_ids=with_region_ids)
        print("The response of MapsAppSpotsApi->v1_spot_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocatable** | **bool**| Filter only allocatable spots | [optional] 
 **external_device** | [**List[str]**](str.md)| filter spots relative to external devices identified by their name | [optional] 
 **id** | [**List[int]**](int.md)| filter spot with id | [optional] 
 **intersects_region** | **str**| filter spots which are contained within region with id | [optional] 
 **map** | [**List[str]**](str.md)| filter spots by maps | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **name** | [**List[str]**](str.md)| filter spots by name(s) | [optional] 
 **node** | **int**| filter spots by node id | [optional] 
 **position** | **str**| x,y coordinate of spot | [optional] 
 **type** | [**List[str]**](str.md)| filter spots by type(s) | [optional] 
 **with_region_ids** | **bool**| add related region ids | [optional] 

### Return type

[**List[SpotAnnotation]**](SpotAnnotation.md)

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

# **v1_spot_partial_update**
> SpotAnnotationUpdate v1_spot_partial_update(id_or_name, patched_spot_annotation_update_request=patched_spot_annotation_update_request)



List Spots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.patched_spot_annotation_update_request import PatchedSpotAnnotationUpdateRequest
from openapi_client.models.spot_annotation_update import SpotAnnotationUpdate
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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    id_or_name = '1' # str | Spot ID or Name.
    patched_spot_annotation_update_request = openapi_client.PatchedSpotAnnotationUpdateRequest() # PatchedSpotAnnotationUpdateRequest |  (optional)

    try:
        api_response = api_instance.v1_spot_partial_update(id_or_name, patched_spot_annotation_update_request=patched_spot_annotation_update_request)
        print("The response of MapsAppSpotsApi->v1_spot_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Spot ID or Name. | 
 **patched_spot_annotation_update_request** | [**PatchedSpotAnnotationUpdateRequest**](PatchedSpotAnnotationUpdateRequest.md)|  | [optional] 

### Return type

[**SpotAnnotationUpdate**](SpotAnnotationUpdate.md)

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

# **v1_spot_retrieve**
> SpotAnnotation v1_spot_retrieve(id_or_name)



List Spots

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
    api_instance = openapi_client.MapsAppSpotsApi(api_client)
    id_or_name = '1' # str | Spot ID or Name.

    try:
        api_response = api_instance.v1_spot_retrieve(id_or_name)
        print("The response of MapsAppSpotsApi->v1_spot_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppSpotsApi->v1_spot_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Spot ID or Name. | 

### Return type

[**SpotAnnotation**](SpotAnnotation.md)

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

