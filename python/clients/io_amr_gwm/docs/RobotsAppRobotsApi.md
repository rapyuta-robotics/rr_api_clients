# io_amr_gwm.RobotsAppRobotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_robot_create**](RobotsAppRobotsApi.md#v1_robot_create) | **POST** /v1/robot | 
[**v1_robot_destroy**](RobotsAppRobotsApi.md#v1_robot_destroy) | **DELETE** /v1/robot/{id} | 
[**v1_robot_list**](RobotsAppRobotsApi.md#v1_robot_list) | **GET** /v1/robot | 
[**v1_robot_partial_update**](RobotsAppRobotsApi.md#v1_robot_partial_update) | **PATCH** /v1/robot/{id} | 
[**v1_robot_retrieve**](RobotsAppRobotsApi.md#v1_robot_retrieve) | **GET** /v1/robot/{id} | 
[**v1_robot_update**](RobotsAppRobotsApi.md#v1_robot_update) | **PUT** /v1/robot/{id} | 


# **v1_robot_create**
> Robot v1_robot_create(robot_request)



Manage Robots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.robot import Robot
from io_amr_gwm.models.robot_request import RobotRequest
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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    robot_request = io_amr_gwm.RobotRequest() # RobotRequest | 

    try:
        api_response = api_instance.v1_robot_create(robot_request)
        print("The response of RobotsAppRobotsApi->v1_robot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_request** | [**RobotRequest**](RobotRequest.md)|  | 

### Return type

[**Robot**](Robot.md)

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

# **v1_robot_destroy**
> v1_robot_destroy(id)



Manage Robots

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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    id = 56 # int | A unique integer value identifying this robot.

    try:
        api_instance.v1_robot_destroy(id)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this robot. | 

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

# **v1_robot_list**
> List[Robot] v1_robot_list(robot_descriptor=robot_descriptor)



Manage Robots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.robot import Robot
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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    robot_descriptor = 56 # int |  (optional)

    try:
        api_response = api_instance.v1_robot_list(robot_descriptor=robot_descriptor)
        print("The response of RobotsAppRobotsApi->v1_robot_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_descriptor** | **int**|  | [optional] 

### Return type

[**List[Robot]**](Robot.md)

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

# **v1_robot_partial_update**
> Robot v1_robot_partial_update(id, patched_robot_request=patched_robot_request)



Manage Robots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_robot_request import PatchedRobotRequest
from io_amr_gwm.models.robot import Robot
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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    id = 56 # int | A unique integer value identifying this robot.
    patched_robot_request = io_amr_gwm.PatchedRobotRequest() # PatchedRobotRequest |  (optional)

    try:
        api_response = api_instance.v1_robot_partial_update(id, patched_robot_request=patched_robot_request)
        print("The response of RobotsAppRobotsApi->v1_robot_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this robot. | 
 **patched_robot_request** | [**PatchedRobotRequest**](PatchedRobotRequest.md)|  | [optional] 

### Return type

[**Robot**](Robot.md)

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

# **v1_robot_retrieve**
> Robot v1_robot_retrieve(id)



Manage Robots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.robot import Robot
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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    id = 56 # int | A unique integer value identifying this robot.

    try:
        api_response = api_instance.v1_robot_retrieve(id)
        print("The response of RobotsAppRobotsApi->v1_robot_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this robot. | 

### Return type

[**Robot**](Robot.md)

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

# **v1_robot_update**
> Robot v1_robot_update(id, robot_request)



Manage Robots

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.robot import Robot
from io_amr_gwm.models.robot_request import RobotRequest
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
    api_instance = io_amr_gwm.RobotsAppRobotsApi(api_client)
    id = 56 # int | A unique integer value identifying this robot.
    robot_request = io_amr_gwm.RobotRequest() # RobotRequest | 

    try:
        api_response = api_instance.v1_robot_update(id, robot_request)
        print("The response of RobotsAppRobotsApi->v1_robot_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RobotsAppRobotsApi->v1_robot_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this robot. | 
 **robot_request** | [**RobotRequest**](RobotRequest.md)|  | 

### Return type

[**Robot**](Robot.md)

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

