# gwm.SitesAppExternalDevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_external_device_create**](SitesAppExternalDevicesApi.md#v1_external_device_create) | **POST** /v1/external_device | 
[**v1_external_device_destroy**](SitesAppExternalDevicesApi.md#v1_external_device_destroy) | **DELETE** /v1/external_device/{id_or_name} | 
[**v1_external_device_list**](SitesAppExternalDevicesApi.md#v1_external_device_list) | **GET** /v1/external_device | 
[**v1_external_device_partial_update**](SitesAppExternalDevicesApi.md#v1_external_device_partial_update) | **PATCH** /v1/external_device/{id_or_name} | 
[**v1_external_device_retrieve**](SitesAppExternalDevicesApi.md#v1_external_device_retrieve) | **GET** /v1/external_device/{id_or_name} | 
[**v1_external_device_update**](SitesAppExternalDevicesApi.md#v1_external_device_update) | **PUT** /v1/external_device/{id_or_name} | 


# **v1_external_device_create**
> ExternalDevice v1_external_device_create(external_device_request)



Manage External Devices

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.external_device import ExternalDevice
from gwm.models.external_device_request import ExternalDeviceRequest
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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    external_device_request = gwm.ExternalDeviceRequest() # ExternalDeviceRequest | 

    try:
        api_response = api_instance.v1_external_device_create(external_device_request)
        print("The response of SitesAppExternalDevicesApi->v1_external_device_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_device_request** | [**ExternalDeviceRequest**](ExternalDeviceRequest.md)|  | 

### Return type

[**ExternalDevice**](ExternalDevice.md)

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

# **v1_external_device_destroy**
> v1_external_device_destroy(id_or_name)



Manage External Devices

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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    id_or_name = '1' # str | External Device ID or Name.

    try:
        api_instance.v1_external_device_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| External Device ID or Name. | 

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

# **v1_external_device_list**
> List[ExternalDevice] v1_external_device_list(id=id, type=type)



List agents

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.external_device import ExternalDevice
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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    id = 56 # int | filter external devices with external device id (optional)
    type = 'type_example' # str | filter external devices with external device type (optional)

    try:
        api_response = api_instance.v1_external_device_list(id=id, type=type)
        print("The response of SitesAppExternalDevicesApi->v1_external_device_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| filter external devices with external device id | [optional] 
 **type** | **str**| filter external devices with external device type | [optional] 

### Return type

[**List[ExternalDevice]**](ExternalDevice.md)

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

# **v1_external_device_partial_update**
> ExternalDevice v1_external_device_partial_update(id_or_name, patched_external_device_request=patched_external_device_request)



Manage External Devices

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.external_device import ExternalDevice
from gwm.models.patched_external_device_request import PatchedExternalDeviceRequest
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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    id_or_name = '1' # str | External Device ID or Name.
    patched_external_device_request = gwm.PatchedExternalDeviceRequest() # PatchedExternalDeviceRequest |  (optional)

    try:
        api_response = api_instance.v1_external_device_partial_update(id_or_name, patched_external_device_request=patched_external_device_request)
        print("The response of SitesAppExternalDevicesApi->v1_external_device_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| External Device ID or Name. | 
 **patched_external_device_request** | [**PatchedExternalDeviceRequest**](PatchedExternalDeviceRequest.md)|  | [optional] 

### Return type

[**ExternalDevice**](ExternalDevice.md)

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

# **v1_external_device_retrieve**
> ExternalDevice v1_external_device_retrieve(id_or_name)



Manage External Devices

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.external_device import ExternalDevice
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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    id_or_name = '1' # str | External Device ID or Name.

    try:
        api_response = api_instance.v1_external_device_retrieve(id_or_name)
        print("The response of SitesAppExternalDevicesApi->v1_external_device_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| External Device ID or Name. | 

### Return type

[**ExternalDevice**](ExternalDevice.md)

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

# **v1_external_device_update**
> ExternalDevice v1_external_device_update(id_or_name, external_device_request)



Manage External Devices

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.external_device import ExternalDevice
from gwm.models.external_device_request import ExternalDeviceRequest
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
    api_instance = gwm.SitesAppExternalDevicesApi(api_client)
    id_or_name = '1' # str | External Device ID or Name.
    external_device_request = gwm.ExternalDeviceRequest() # ExternalDeviceRequest | 

    try:
        api_response = api_instance.v1_external_device_update(id_or_name, external_device_request)
        print("The response of SitesAppExternalDevicesApi->v1_external_device_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppExternalDevicesApi->v1_external_device_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| External Device ID or Name. | 
 **external_device_request** | [**ExternalDeviceRequest**](ExternalDeviceRequest.md)|  | 

### Return type

[**ExternalDevice**](ExternalDevice.md)

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

