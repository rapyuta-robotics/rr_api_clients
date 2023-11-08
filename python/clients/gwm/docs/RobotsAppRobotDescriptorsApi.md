# gwm.RobotsAppRobotDescriptorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_robot_descriptor_create**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_create) | **POST** /v1/robot_descriptor | 
[**v1_robot_descriptor_destroy**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_destroy) | **DELETE** /v1/robot_descriptor/{id} | 
[**v1_robot_descriptor_list**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_list) | **GET** /v1/robot_descriptor | 
[**v1_robot_descriptor_partial_update**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_partial_update) | **PATCH** /v1/robot_descriptor/{id} | 
[**v1_robot_descriptor_retrieve**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_retrieve) | **GET** /v1/robot_descriptor/{id} | 
[**v1_robot_descriptor_update**](RobotsAppRobotDescriptorsApi.md#v1_robot_descriptor_update) | **PUT** /v1/robot_descriptor/{id} | 


# **v1_robot_descriptor_create**
> RobotDescriptor v1_robot_descriptor_create(robot_descriptor_request)



Manage RobotDescriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.robot_descriptor import RobotDescriptor
from gwm.models.robot_descriptor_request import RobotDescriptorRequest
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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    robot_descriptor_request = gwm.RobotDescriptorRequest() # RobotDescriptorRequest | 

    try:
        api_response = api_instance.v1_robot_descriptor_create(robot_descriptor_request)
        print("The response of RobotsAppRobotDescriptorsApi->v1_robot_descriptor_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_descriptor_request** | [**RobotDescriptorRequest**](RobotDescriptorRequest.md)|  | 

### Return type

[**RobotDescriptor**](RobotDescriptor.md)

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

# **v1_robot_descriptor_destroy**
> v1_robot_descriptor_destroy(id)



Manage RobotDescriptors

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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    id = 56 # int | 

    try:
        api_instance.v1_robot_descriptor_destroy(id)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **v1_robot_descriptor_list**
> List[RobotDescriptor] v1_robot_descriptor_list(agent_id=agent_id, model=model, name=name, type=type, vendor=vendor)



Manage RobotDescriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.robot_descriptor import RobotDescriptor
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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    agent_id = 'agent_id_example' # str |  (optional)
    model = 'model_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    type = 'type_example' # str | Type of robot  * `AMR` - Amr * `FORKLIFT` - Forklift (optional)
    vendor = 'vendor_example' # str |  (optional)

    try:
        api_response = api_instance.v1_robot_descriptor_list(agent_id=agent_id, model=model, name=name, type=type, vendor=vendor)
        print("The response of RobotsAppRobotDescriptorsApi->v1_robot_descriptor_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **type** | **str**| Type of robot  * &#x60;AMR&#x60; - Amr * &#x60;FORKLIFT&#x60; - Forklift | [optional] 
 **vendor** | **str**|  | [optional] 

### Return type

[**List[RobotDescriptor]**](RobotDescriptor.md)

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

# **v1_robot_descriptor_partial_update**
> RobotDescriptor v1_robot_descriptor_partial_update(id, patched_robot_descriptor_request=patched_robot_descriptor_request)



Manage RobotDescriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.patched_robot_descriptor_request import PatchedRobotDescriptorRequest
from gwm.models.robot_descriptor import RobotDescriptor
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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    id = 56 # int | 
    patched_robot_descriptor_request = gwm.PatchedRobotDescriptorRequest() # PatchedRobotDescriptorRequest |  (optional)

    try:
        api_response = api_instance.v1_robot_descriptor_partial_update(id, patched_robot_descriptor_request=patched_robot_descriptor_request)
        print("The response of RobotsAppRobotDescriptorsApi->v1_robot_descriptor_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **patched_robot_descriptor_request** | [**PatchedRobotDescriptorRequest**](PatchedRobotDescriptorRequest.md)|  | [optional] 

### Return type

[**RobotDescriptor**](RobotDescriptor.md)

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

# **v1_robot_descriptor_retrieve**
> RobotDescriptor v1_robot_descriptor_retrieve(id)



Manage RobotDescriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.robot_descriptor import RobotDescriptor
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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.v1_robot_descriptor_retrieve(id)
        print("The response of RobotsAppRobotDescriptorsApi->v1_robot_descriptor_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RobotDescriptor**](RobotDescriptor.md)

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

# **v1_robot_descriptor_update**
> RobotDescriptor v1_robot_descriptor_update(id, robot_descriptor_request)



Manage RobotDescriptors

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.robot_descriptor import RobotDescriptor
from gwm.models.robot_descriptor_request import RobotDescriptorRequest
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
    api_instance = gwm.RobotsAppRobotDescriptorsApi(api_client)
    id = 56 # int | 
    robot_descriptor_request = gwm.RobotDescriptorRequest() # RobotDescriptorRequest | 

    try:
        api_response = api_instance.v1_robot_descriptor_update(id, robot_descriptor_request)
        print("The response of RobotsAppRobotDescriptorsApi->v1_robot_descriptor_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotDescriptorsApi->v1_robot_descriptor_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **robot_descriptor_request** | [**RobotDescriptorRequest**](RobotDescriptorRequest.md)|  | 

### Return type

[**RobotDescriptor**](RobotDescriptor.md)

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

