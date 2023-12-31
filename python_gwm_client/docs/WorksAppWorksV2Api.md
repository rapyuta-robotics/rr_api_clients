# gwm_client.WorksAppWorksV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_work_activate_create**](WorksAppWorksV2Api.md#v2_work_activate_create) | **POST** /v2/work/activate | Activate work
[**v2_work_clear_all_destroy**](WorksAppWorksV2Api.md#v2_work_clear_all_destroy) | **DELETE** /v2/work/clear_all | Clear all works
[**v2_work_create**](WorksAppWorksV2Api.md#v2_work_create) | **POST** /v2/work | Create A Work
[**v2_work_destroy**](WorksAppWorksV2Api.md#v2_work_destroy) | **DELETE** /v2/work/{id} | Cancel or force Delete Work
[**v2_work_internal_update_partial_update**](WorksAppWorksV2Api.md#v2_work_internal_update_partial_update) | **PATCH** /v2/work/{id}/internal_update | Internal Update Work
[**v2_work_list**](WorksAppWorksV2Api.md#v2_work_list) | **GET** /v2/work | List Works
[**v2_work_partial_update**](WorksAppWorksV2Api.md#v2_work_partial_update) | **PATCH** /v2/work/{id} | Partially Update Work
[**v2_work_retrieve**](WorksAppWorksV2Api.md#v2_work_retrieve) | **GET** /v2/work/{id} | Get A Work information
[**v2_work_summary_retrieve**](WorksAppWorksV2Api.md#v2_work_summary_retrieve) | **GET** /v2/work/summary | Get Work Summary


# **v2_work_activate_create**
> ActivateWork v2_work_activate_create(activate_work_request)

Activate work

Activate work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.activate_work import ActivateWork
from gwm_client.models.activate_work_request import ActivateWorkRequest
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    activate_work_request = gwm_client.ActivateWorkRequest() # ActivateWorkRequest | 

    try:
        # Activate work
        api_response = api_instance.v2_work_activate_create(activate_work_request)
        print("The response of WorksAppWorksV2Api->v2_work_activate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_activate_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_work_request** | [**ActivateWorkRequest**](ActivateWorkRequest.md)|  | 

### Return type

[**ActivateWork**](ActivateWork.md)

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

# **v2_work_clear_all_destroy**
> v2_work_clear_all_destroy()

Clear all works

Manage Works

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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)

    try:
        # Clear all works
        api_instance.v2_work_clear_all_destroy()
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_clear_all_destroy: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **v2_work_create**
> Work v2_work_create(work_request)

Create A Work

Create A Work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.work import Work
from gwm_client.models.work_request import WorkRequest
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    work_request = {"type":"ADHOC_MOVE_POSITION","map":1,"priority":0,"pos":{"coordinates":[2,4],"type":"Point"},"yaw":0,"assigned_agent":1,"meta_data":{"attribute_1":"value_1"},"application_data":{}} # WorkRequest | 

    try:
        # Create A Work
        api_response = api_instance.v2_work_create(work_request)
        print("The response of WorksAppWorksV2Api->v2_work_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_request** | [**WorkRequest**](WorkRequest.md)|  | 

### Return type

[**Work**](Work.md)

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

# **v2_work_destroy**
> v2_work_destroy(id, force=force)

Cancel or force Delete Work

Cancel or force Delete Work

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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.
    force = False # bool | Force the deletion of the work (optional) (default to False)

    try:
        # Cancel or force Delete Work
        api_instance.v2_work_destroy(id, force=force)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 
 **force** | **bool**| Force the deletion of the work | [optional] [default to False]

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

# **v2_work_internal_update_partial_update**
> WorkInternalUpdate v2_work_internal_update_partial_update(id, patched_work_internal_update_request=patched_work_internal_update_request)

Internal Update Work

Internal Update Work (do not use this, this is for internal updates only)

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.patched_work_internal_update_request import PatchedWorkInternalUpdateRequest
from gwm_client.models.work_internal_update import WorkInternalUpdate
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.
    patched_work_internal_update_request = gwm_client.PatchedWorkInternalUpdateRequest() # PatchedWorkInternalUpdateRequest |  (optional)

    try:
        # Internal Update Work
        api_response = api_instance.v2_work_internal_update_partial_update(id, patched_work_internal_update_request=patched_work_internal_update_request)
        print("The response of WorksAppWorksV2Api->v2_work_internal_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_internal_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 
 **patched_work_internal_update_request** | [**PatchedWorkInternalUpdateRequest**](PatchedWorkInternalUpdateRequest.md)|  | [optional] 

### Return type

[**WorkInternalUpdate**](WorkInternalUpdate.md)

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

# **v2_work_list**
> List[Work] v2_work_list(activated_at_after=activated_at_after, activated_at_before=activated_at_before, application_data=application_data, assigned_agent=assigned_agent, batch=batch, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, priority=priority, status=status, type=type, workflow=workflow)

List Works

List Works

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.work import Work
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    activated_at_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    activated_at_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    application_data = 'application_data_example' # str | filter by application_data query (optional)
    assigned_agent = [] # List[float] | filter by work assigned to any agents with ids (optional) (default to [])
    batch = ['batch_example'] # List[str] |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | filter works created after given timestamp (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | filter works created before given timestamp (optional)
    cut_off_time_after = '2013-10-20T19:20:30+01:00' # datetime | filter works cut off time after given timestamp (optional)
    cut_off_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [3.4] # List[float] | filter works by ids (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = ['name_example'] # List[str] | User provided names eg: `mywarehouse_move_2021-05-11T12:05:27Z` (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | Page number, this is only applicable if page_size param is passed (optional)
    page_size = 56 # int |  (optional)
    priority = [56] # List[int] |  (optional)
    status = ['status_example'] # List[str] | filter by work status (optional)
    type = ['type_example'] # List[str] | filter by work type (optional)
    workflow = ['workflow_example'] # List[str] |  (optional)

    try:
        # List Works
        api_response = api_instance.v2_work_list(activated_at_after=activated_at_after, activated_at_before=activated_at_before, application_data=application_data, assigned_agent=assigned_agent, batch=batch, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, priority=priority, status=status, type=type, workflow=workflow)
        print("The response of WorksAppWorksV2Api->v2_work_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activated_at_after** | **datetime**|  | [optional] 
 **activated_at_before** | **datetime**|  | [optional] 
 **application_data** | **str**| filter by application_data query | [optional] 
 **assigned_agent** | [**List[float]**](float.md)| filter by work assigned to any agents with ids | [optional] [default to []]
 **batch** | [**List[str]**](str.md)|  | [optional] 
 **created_at_after** | **datetime**| filter works created after given timestamp | [optional] 
 **created_at_before** | **datetime**| filter works created before given timestamp | [optional] 
 **cut_off_time_after** | **datetime**| filter works cut off time after given timestamp | [optional] 
 **cut_off_time_before** | **datetime**|  | [optional] 
 **id** | [**List[float]**](float.md)| filter works by ids | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **name** | [**List[str]**](str.md)| User provided names eg: &#x60;mywarehouse_move_2021-05-11T12:05:27Z&#x60; | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| Page number, this is only applicable if page_size param is passed | [optional] 
 **page_size** | **int**|  | [optional] 
 **priority** | [**List[int]**](int.md)|  | [optional] 
 **status** | [**List[str]**](str.md)| filter by work status | [optional] 
 **type** | [**List[str]**](str.md)| filter by work type | [optional] 
 **workflow** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Work]**](Work.md)

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

# **v2_work_partial_update**
> WorkExternalUpdate v2_work_partial_update(id, patched_work_external_update_request=patched_work_external_update_request)

Partially Update Work

Partially Update Work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.patched_work_external_update_request import PatchedWorkExternalUpdateRequest
from gwm_client.models.work_external_update import WorkExternalUpdate
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.
    patched_work_external_update_request = {"action":"SET_PRIORITY","priority":10} # PatchedWorkExternalUpdateRequest |  (optional)

    try:
        # Partially Update Work
        api_response = api_instance.v2_work_partial_update(id, patched_work_external_update_request=patched_work_external_update_request)
        print("The response of WorksAppWorksV2Api->v2_work_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 
 **patched_work_external_update_request** | [**PatchedWorkExternalUpdateRequest**](PatchedWorkExternalUpdateRequest.md)|  | [optional] 

### Return type

[**WorkExternalUpdate**](WorkExternalUpdate.md)

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

# **v2_work_retrieve**
> Work v2_work_retrieve(id)

Get A Work information

Get A Work information

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.work import Work
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.

    try:
        # Get A Work information
        api_response = api_instance.v2_work_retrieve(id)
        print("The response of WorksAppWorksV2Api->v2_work_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 

### Return type

[**Work**](Work.md)

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

# **v2_work_summary_retrieve**
> Work v2_work_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, type=type, workflow=workflow)

Get Work Summary

Get Work Summary

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.work import Work
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
    api_instance = gwm_client.WorksAppWorksV2Api(api_client)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    interval = 'interval_example' # str | * `daily` - daily * `weekly` - weekly * `monthly` - monthly * `annually` - annually (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    type = ['type_example'] # List[str] | Type of the work  * `CHARGE` - Charge * `EXPLORE` - Explore * `PAYLOAD_MOVE` - Payload Move * `ADHOC_MOVE_POSITION` - Adhoc Move Position * `ADHOC_MOVE_REGION` - Adhoc Move Region * `ADHOC_MOVE_SPOT` - Adhoc Move Spot (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # Get Work Summary
        api_response = api_instance.v2_work_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, type=type, workflow=workflow)
        print("The response of WorksAppWorksV2Api->v2_work_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV2Api->v2_work_summary_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | [optional] 
 **group_by** | **str**|  | [optional] 
 **interval** | **str**| * &#x60;daily&#x60; - daily * &#x60;weekly&#x60; - weekly * &#x60;monthly&#x60; - monthly * &#x60;annually&#x60; - annually | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **type** | [**List[str]**](str.md)| Type of the work  * &#x60;CHARGE&#x60; - Charge * &#x60;EXPLORE&#x60; - Explore * &#x60;PAYLOAD_MOVE&#x60; - Payload Move * &#x60;ADHOC_MOVE_POSITION&#x60; - Adhoc Move Position * &#x60;ADHOC_MOVE_REGION&#x60; - Adhoc Move Region * &#x60;ADHOC_MOVE_SPOT&#x60; - Adhoc Move Spot | [optional] 
 **workflow** | **str**|  | [optional] 

### Return type

[**Work**](Work.md)

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

