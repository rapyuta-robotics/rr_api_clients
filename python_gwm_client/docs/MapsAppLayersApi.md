# gwm_client.MapsAppLayersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_map_layer_create**](MapsAppLayersApi.md#v1_map_layer_create) | **POST** /v1/map/{map_id_or_name}/layer | 
[**v1_map_layer_destroy**](MapsAppLayersApi.md#v1_map_layer_destroy) | **DELETE** /v1/map/{map_id_or_name}/layer/{id_or_name} | 
[**v1_map_layer_get_yaml_retrieve**](MapsAppLayersApi.md#v1_map_layer_get_yaml_retrieve) | **GET** /v1/map/{map_id_or_name}/layer/{id_or_name}/get_yaml | 
[**v1_map_layer_list**](MapsAppLayersApi.md#v1_map_layer_list) | **GET** /v1/map/{map_id_or_name}/layer | 
[**v1_map_layer_partial_update**](MapsAppLayersApi.md#v1_map_layer_partial_update) | **PATCH** /v1/map/{map_id_or_name}/layer/{id_or_name} | 
[**v1_map_layer_retrieve**](MapsAppLayersApi.md#v1_map_layer_retrieve) | **GET** /v1/map/{map_id_or_name}/layer/{id_or_name} | 
[**v1_map_layer_retrieve_layer_data_retrieve**](MapsAppLayersApi.md#v1_map_layer_retrieve_layer_data_retrieve) | **GET** /v1/map/{map_id_or_name}/layer/{id_or_name}/retrieve_layer_data | 
[**v1_map_layer_retrieve_layer_image_retrieve**](MapsAppLayersApi.md#v1_map_layer_retrieve_layer_image_retrieve) | **GET** /v1/map/{map_id_or_name}/layer/{id_or_name}/retrieve_layer_image | 
[**v1_map_layer_update**](MapsAppLayersApi.md#v1_map_layer_update) | **PUT** /v1/map/{map_id_or_name}/layer/{id_or_name} | 
[**v1_map_layer_upload_layer_data_update**](MapsAppLayersApi.md#v1_map_layer_upload_layer_data_update) | **PUT** /v1/map/{map_id_or_name}/layer/{id_or_name}/upload_layer_data | 
[**v1_map_layer_upload_layer_image_update**](MapsAppLayersApi.md#v1_map_layer_upload_layer_image_update) | **PUT** /v1/map/{map_id_or_name}/layer/{id_or_name}/upload_layer_image | 


# **v1_map_layer_create**
> Layer v1_map_layer_create(map_id_or_name, layer_request)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer import Layer
from gwm_client.models.layer_request import LayerRequest
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    layer_request = gwm_client.LayerRequest() # LayerRequest | 

    try:
        api_response = api_instance.v1_map_layer_create(map_id_or_name, layer_request)
        print("The response of MapsAppLayersApi->v1_map_layer_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 
 **layer_request** | [**LayerRequest**](LayerRequest.md)|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_map_layer_destroy**
> v1_map_layer_destroy(id_or_name, map_id_or_name)



Manage Map Layers

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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_instance.v1_map_layer_destroy(id_or_name, map_id_or_name)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
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

# **v1_map_layer_get_yaml_retrieve**
> LayerYAML v1_map_layer_get_yaml_retrieve(id_or_name, map_id_or_name)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer_yaml import LayerYAML
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_layer_get_yaml_retrieve(id_or_name, map_id_or_name)
        print("The response of MapsAppLayersApi->v1_map_layer_get_yaml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_get_yaml_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**LayerYAML**](LayerYAML.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_map_layer_list**
> List[Layer] v1_map_layer_list(map_id_or_name)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer import Layer
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_layer_list(map_id_or_name)
        print("The response of MapsAppLayersApi->v1_map_layer_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**List[Layer]**](Layer.md)

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

# **v1_map_layer_partial_update**
> Layer v1_map_layer_partial_update(id_or_name, map_id_or_name, patched_layer_request=patched_layer_request)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer import Layer
from gwm_client.models.patched_layer_request import PatchedLayerRequest
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    patched_layer_request = gwm_client.PatchedLayerRequest() # PatchedLayerRequest |  (optional)

    try:
        api_response = api_instance.v1_map_layer_partial_update(id_or_name, map_id_or_name, patched_layer_request=patched_layer_request)
        print("The response of MapsAppLayersApi->v1_map_layer_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **patched_layer_request** | [**PatchedLayerRequest**](PatchedLayerRequest.md)|  | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_map_layer_retrieve**
> Layer v1_map_layer_retrieve(id_or_name, map_id_or_name)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer import Layer
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_layer_retrieve(id_or_name, map_id_or_name)
        print("The response of MapsAppLayersApi->v1_map_layer_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**Layer**](Layer.md)

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

# **v1_map_layer_retrieve_layer_data_retrieve**
> LayerData v1_map_layer_retrieve_layer_data_retrieve(id_or_name, map_id_or_name)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer_data import LayerData
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this layer.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_layer_retrieve_layer_data_retrieve(id_or_name, map_id_or_name)
        print("The response of MapsAppLayersApi->v1_map_layer_retrieve_layer_data_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_retrieve_layer_data_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this layer. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**LayerData**](LayerData.md)

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

# **v1_map_layer_retrieve_layer_image_retrieve**
> LayerImage v1_map_layer_retrieve_layer_image_retrieve(id_or_name, map_id_or_name)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer_image import LayerImage
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = 56 # int | A unique integer value identifying this layer.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name

    try:
        api_response = api_instance.v1_map_layer_retrieve_layer_image_retrieve(id_or_name, map_id_or_name)
        print("The response of MapsAppLayersApi->v1_map_layer_retrieve_layer_image_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_retrieve_layer_image_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **int**| A unique integer value identifying this layer. | 
 **map_id_or_name** | **str**| MAP ID or Name | 

### Return type

[**LayerImage**](LayerImage.md)

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

# **v1_map_layer_update**
> Layer v1_map_layer_update(id_or_name, map_id_or_name, layer_request)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer import Layer
from gwm_client.models.layer_request import LayerRequest
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    layer_request = gwm_client.LayerRequest() # LayerRequest | 

    try:
        api_response = api_instance.v1_map_layer_update(id_or_name, map_id_or_name, layer_request)
        print("The response of MapsAppLayersApi->v1_map_layer_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **layer_request** | [**LayerRequest**](LayerRequest.md)|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_map_layer_upload_layer_data_update**
> LayerData v1_map_layer_upload_layer_data_update(id_or_name, map_id_or_name, data=data)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer_data import LayerData
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    data = None # bytearray |  (optional)

    try:
        api_response = api_instance.v1_map_layer_upload_layer_data_update(id_or_name, map_id_or_name, data=data)
        print("The response of MapsAppLayersApi->v1_map_layer_upload_layer_data_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_upload_layer_data_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **data** | **bytearray**|  | [optional] 

### Return type

[**LayerData**](LayerData.md)

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

# **v1_map_layer_upload_layer_image_update**
> LayerImage v1_map_layer_upload_layer_image_update(id_or_name, map_id_or_name, image=image)



Manage Map Layers

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.layer_image import LayerImage
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
    api_instance = gwm_client.MapsAppLayersApi(api_client)
    id_or_name = '1' # str | Layer ID or Name.
    map_id_or_name = 'map_id_or_name_example' # str | MAP ID or Name
    image = None # bytearray | Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file (optional)

    try:
        api_response = api_instance.v1_map_layer_upload_layer_image_update(id_or_name, map_id_or_name, image=image)
        print("The response of MapsAppLayersApi->v1_map_layer_upload_layer_image_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsAppLayersApi->v1_map_layer_upload_layer_image_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Layer ID or Name. | 
 **map_id_or_name** | **str**| MAP ID or Name | 
 **image** | **bytearray**| Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file | [optional] 

### Return type

[**LayerImage**](LayerImage.md)

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

