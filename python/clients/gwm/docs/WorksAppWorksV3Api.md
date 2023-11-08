# gwm.WorksAppWorksV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_works_activate_create**](WorksAppWorksV3Api.md#v3_works_activate_create) | **POST** /v3/works/activate | Activate work
[**v3_works_bulk_internal_update**](WorksAppWorksV3Api.md#v3_works_bulk_internal_update) | **PATCH** /v3/works/internal_update | Bulk Internal Update Work
[**v3_works_clear_create**](WorksAppWorksV3Api.md#v3_works_clear_create) | **POST** /v3/works/clear | Delete works by ids
[**v3_works_count_retrieve**](WorksAppWorksV3Api.md#v3_works_count_retrieve) | **GET** /v3/works/count | 
[**v3_works_create**](WorksAppWorksV3Api.md#v3_works_create) | **POST** /v3/works | Create A Work
[**v3_works_destroy**](WorksAppWorksV3Api.md#v3_works_destroy) | **DELETE** /v3/works/{id} | Delete work in terminal or on_hold state
[**v3_works_internal_update_partial_update**](WorksAppWorksV3Api.md#v3_works_internal_update_partial_update) | **PATCH** /v3/works/{id}/internal_update | Internal Update Work
[**v3_works_list**](WorksAppWorksV3Api.md#v3_works_list) | **GET** /v3/works | List Works
[**v3_works_partial_update**](WorksAppWorksV3Api.md#v3_works_partial_update) | **PATCH** /v3/works/{id} | Partially Update Work
[**v3_works_retrieve**](WorksAppWorksV3Api.md#v3_works_retrieve) | **GET** /v3/works/{id} | Get A Work information
[**v3_works_summary_retrieve**](WorksAppWorksV3Api.md#v3_works_summary_retrieve) | **GET** /v3/works/summary | Get Work Summary


# **v3_works_activate_create**
> V3ActivateWork v3_works_activate_create(v3_activate_work_request=v3_activate_work_request)

Activate work

Activate work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_activate_work import V3ActivateWork
from gwm.models.v3_activate_work_request import V3ActivateWorkRequest
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    v3_activate_work_request = gwm.V3ActivateWorkRequest() # V3ActivateWorkRequest |  (optional)

    try:
        # Activate work
        api_response = api_instance.v3_works_activate_create(v3_activate_work_request=v3_activate_work_request)
        print("The response of WorksAppWorksV3Api->v3_works_activate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_activate_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_activate_work_request** | [**V3ActivateWorkRequest**](V3ActivateWorkRequest.md)|  | [optional] 

### Return type

[**V3ActivateWork**](V3ActivateWork.md)

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

# **v3_works_bulk_internal_update**
> V3Work v3_works_bulk_internal_update(v3_work_internal_update_request)

Bulk Internal Update Work

Bulk Internal Update Work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_work import V3Work
from gwm.models.v3_work_internal_update_request import V3WorkInternalUpdateRequest
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    v3_work_internal_update_request = [gwm.V3WorkInternalUpdateRequest()] # List[V3WorkInternalUpdateRequest] | 

    try:
        # Bulk Internal Update Work
        api_response = api_instance.v3_works_bulk_internal_update(v3_work_internal_update_request)
        print("The response of WorksAppWorksV3Api->v3_works_bulk_internal_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_bulk_internal_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_work_internal_update_request** | [**List[V3WorkInternalUpdateRequest]**](V3WorkInternalUpdateRequest.md)|  | 

### Return type

[**V3Work**](V3Work.md)

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

# **v3_works_clear_create**
> V3ActivateWork v3_works_clear_create(v3_activate_work_request=v3_activate_work_request)

Delete works by ids

Delete works by ids

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_activate_work import V3ActivateWork
from gwm.models.v3_activate_work_request import V3ActivateWorkRequest
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    v3_activate_work_request = {"work_ids":[1,2]} # V3ActivateWorkRequest |  (optional)

    try:
        # Delete works by ids
        api_response = api_instance.v3_works_clear_create(v3_activate_work_request=v3_activate_work_request)
        print("The response of WorksAppWorksV3Api->v3_works_clear_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_clear_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_activate_work_request** | [**V3ActivateWorkRequest**](V3ActivateWorkRequest.md)|  | [optional] 

### Return type

[**V3ActivateWork**](V3ActivateWork.md)

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

# **v3_works_count_retrieve**
> int v3_works_count_retrieve(activated_at_after=activated_at_after, activated_at_before=activated_at_before, assigned_agent=assigned_agent, batch=batch, batch_contains=batch_contains, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, name=name, name_contains=name_contains, ordering=ordering, priority=priority, status=status, task_agent=task_agent, type=type, workflow=workflow)



Manage Works

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    activated_at_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    activated_at_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    assigned_agent = [gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    batch = ['batch_example'] # List[str] |  (optional)
    batch_contains = 'batch_contains_example' # str |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    cut_off_time_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    cut_off_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [56] # List[int] |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    name_contains = 'name_contains_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    priority = [56] # List[int] |  (optional)
    status = ['status_example'] # List[str] | Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed (optional)
    task_agent = [gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    type = ['type_example'] # List[str] | Type of the work  * `CHARGE` - Charge * `EXPLORE` - Explore * `PAYLOAD_MOVE` - Payload Move * `ADHOC_MOVE_POSITION` - Adhoc Move Position * `ADHOC_MOVE_REGION` - Adhoc Move Region * `ADHOC_MOVE_SPOT` - Adhoc Move Spot (optional)
    workflow = ['workflow_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.v3_works_count_retrieve(activated_at_after=activated_at_after, activated_at_before=activated_at_before, assigned_agent=assigned_agent, batch=batch, batch_contains=batch_contains, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, name=name, name_contains=name_contains, ordering=ordering, priority=priority, status=status, task_agent=task_agent, type=type, workflow=workflow)
        print("The response of WorksAppWorksV3Api->v3_works_count_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_count_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activated_at_after** | **datetime**|  | [optional] 
 **activated_at_before** | **datetime**|  | [optional] 
 **assigned_agent** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **batch** | [**List[str]**](str.md)|  | [optional] 
 **batch_contains** | **str**|  | [optional] 
 **created_at_after** | **datetime**|  | [optional] 
 **created_at_before** | **datetime**|  | [optional] 
 **cut_off_time_after** | **datetime**|  | [optional] 
 **cut_off_time_before** | **datetime**|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **name_contains** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **priority** | [**List[int]**](int.md)|  | [optional] 
 **status** | [**List[str]**](str.md)| Current status of the Work, this is set by the system via internal API  * &#x60;ON_HOLD&#x60; - On Hold * &#x60;NEW&#x60; - New * &#x60;LIVE&#x60; - Live * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;COMPLETED&#x60; - Completed * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;ABORTED&#x60; - Aborted * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
 **task_agent** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **type** | [**List[str]**](str.md)| Type of the work  * &#x60;CHARGE&#x60; - Charge * &#x60;EXPLORE&#x60; - Explore * &#x60;PAYLOAD_MOVE&#x60; - Payload Move * &#x60;ADHOC_MOVE_POSITION&#x60; - Adhoc Move Position * &#x60;ADHOC_MOVE_REGION&#x60; - Adhoc Move Region * &#x60;ADHOC_MOVE_SPOT&#x60; - Adhoc Move Spot | [optional] 
 **workflow** | [**List[str]**](str.md)|  | [optional] 

### Return type

**int**

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

# **v3_works_create**
> List[V3Work] v3_works_create(v3_work_request)

Create A Work

Create A Work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_work import V3Work
from gwm.models.v3_work_request import V3WorkRequest
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    v3_work_request = [{"type":"ADHOC_MOVE_POSITION","map":1,"priority":0,"pos":{"coordinates":[2,4],"type":"Point"},"yaw":0,"assigned_agent":1,"meta_data":{"attribute_1":"value_1"}}] # List[V3WorkRequest] | 

    try:
        # Create A Work
        api_response = api_instance.v3_works_create(v3_work_request)
        print("The response of WorksAppWorksV3Api->v3_works_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_work_request** | [**List[V3WorkRequest]**](V3WorkRequest.md)|  | 

### Return type

[**List[V3Work]**](V3Work.md)

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

# **v3_works_destroy**
> v3_works_destroy(id)

Delete work in terminal or on_hold state

Delete work in terminal or on_hold state

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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.

    try:
        # Delete work in terminal or on_hold state
        api_instance.v3_works_destroy(id)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 

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

# **v3_works_internal_update_partial_update**
> V3WorkInternalUpdate v3_works_internal_update_partial_update(id, patched_v3_work_internal_update_request=patched_v3_work_internal_update_request)

Internal Update Work

Do not use this, this is for internal updates only

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.patched_v3_work_internal_update_request import PatchedV3WorkInternalUpdateRequest
from gwm.models.v3_work_internal_update import V3WorkInternalUpdate
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.
    patched_v3_work_internal_update_request = gwm.PatchedV3WorkInternalUpdateRequest() # PatchedV3WorkInternalUpdateRequest |  (optional)

    try:
        # Internal Update Work
        api_response = api_instance.v3_works_internal_update_partial_update(id, patched_v3_work_internal_update_request=patched_v3_work_internal_update_request)
        print("The response of WorksAppWorksV3Api->v3_works_internal_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_internal_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 
 **patched_v3_work_internal_update_request** | [**PatchedV3WorkInternalUpdateRequest**](PatchedV3WorkInternalUpdateRequest.md)|  | [optional] 

### Return type

[**V3WorkInternalUpdate**](V3WorkInternalUpdate.md)

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

# **v3_works_list**
> PaginatedV3WorkList v3_works_list(activated_at_after=activated_at_after, activated_at_before=activated_at_before, application_data=application_data, assigned_agent=assigned_agent, batch=batch, batch_contains=batch_contains, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, meta_data=meta_data, name=name, name_contains=name_contains, ordering=ordering, page=page, page_size=page_size, priority=priority, status=status, task_agent=task_agent, type=type, with_fragment_count=with_fragment_count, workflow=workflow)

List Works

List Works

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.paginated_v3_work_list import PaginatedV3WorkList
from gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    activated_at_after = '2013-10-20T19:20:30+01:00' # datetime | filter works activated after given timestamp (optional)
    activated_at_before = '2013-10-20T19:20:30+01:00' # datetime | filter works activated before given timestamp (optional)
    application_data = 'application_data_example' # str | filter by application_data query (optional)
    assigned_agent = [] # List[float] | filter by work assigned to any agents with ids (optional) (default to [])
    batch = ['batch_example'] # List[str] |  (optional)
    batch_contains = 'batch_contains_example' # str |  (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | filter works created after given timestamp (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | filter works created before given timestamp (optional)
    cut_off_time_after = '2013-10-20T19:20:30+01:00' # datetime | filter works cut off time after given timestamp (optional)
    cut_off_time_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [3.4] # List[float] | filter works by ids (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = ['name_example'] # List[str] | User provided names eg: `mywarehouse_move_2021-05-11T12:05:27Z` (optional)
    name_contains = 'name_contains_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | Page number, this is only applicable if page_size param is passed (optional)
    page_size = 56 # int |  (optional)
    priority = [56] # List[int] |  (optional)
    status = ['status_example'] # List[str] | filter by work status (optional)
    task_agent = [gwm.V1ContainersCreateDescriptorParameterInner()] # List[V1ContainersCreateDescriptorParameterInner] |  (optional)
    type = ['type_example'] # List[str] | filter by work type (optional)
    with_fragment_count = True # bool | Include fragment counts in payload works (optional)
    workflow = ['workflow_example'] # List[str] |  (optional)

    try:
        # List Works
        api_response = api_instance.v3_works_list(activated_at_after=activated_at_after, activated_at_before=activated_at_before, application_data=application_data, assigned_agent=assigned_agent, batch=batch, batch_contains=batch_contains, created_at_after=created_at_after, created_at_before=created_at_before, cut_off_time_after=cut_off_time_after, cut_off_time_before=cut_off_time_before, id=id, meta_data=meta_data, name=name, name_contains=name_contains, ordering=ordering, page=page, page_size=page_size, priority=priority, status=status, task_agent=task_agent, type=type, with_fragment_count=with_fragment_count, workflow=workflow)
        print("The response of WorksAppWorksV3Api->v3_works_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activated_at_after** | **datetime**| filter works activated after given timestamp | [optional] 
 **activated_at_before** | **datetime**| filter works activated before given timestamp | [optional] 
 **application_data** | **str**| filter by application_data query | [optional] 
 **assigned_agent** | [**List[float]**](float.md)| filter by work assigned to any agents with ids | [optional] [default to []]
 **batch** | [**List[str]**](str.md)|  | [optional] 
 **batch_contains** | **str**|  | [optional] 
 **created_at_after** | **datetime**| filter works created after given timestamp | [optional] 
 **created_at_before** | **datetime**| filter works created before given timestamp | [optional] 
 **cut_off_time_after** | **datetime**| filter works cut off time after given timestamp | [optional] 
 **cut_off_time_before** | **datetime**|  | [optional] 
 **id** | [**List[float]**](float.md)| filter works by ids | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **name** | [**List[str]**](str.md)| User provided names eg: &#x60;mywarehouse_move_2021-05-11T12:05:27Z&#x60; | [optional] 
 **name_contains** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| Page number, this is only applicable if page_size param is passed | [optional] 
 **page_size** | **int**|  | [optional] 
 **priority** | [**List[int]**](int.md)|  | [optional] 
 **status** | [**List[str]**](str.md)| filter by work status | [optional] 
 **task_agent** | [**List[V1ContainersCreateDescriptorParameterInner]**](V1ContainersCreateDescriptorParameterInner.md)|  | [optional] 
 **type** | [**List[str]**](str.md)| filter by work type | [optional] 
 **with_fragment_count** | **bool**| Include fragment counts in payload works | [optional] 
 **workflow** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedV3WorkList**](PaginatedV3WorkList.md)

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

# **v3_works_partial_update**
> V3WorkExternalUpdate v3_works_partial_update(id, patched_v3_work_external_update_request=patched_v3_work_external_update_request)

Partially Update Work

Partially Update Work

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.patched_v3_work_external_update_request import PatchedV3WorkExternalUpdateRequest
from gwm.models.v3_work_external_update import V3WorkExternalUpdate
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.
    patched_v3_work_external_update_request = {"priority":10} # PatchedV3WorkExternalUpdateRequest |  (optional)

    try:
        # Partially Update Work
        api_response = api_instance.v3_works_partial_update(id, patched_v3_work_external_update_request=patched_v3_work_external_update_request)
        print("The response of WorksAppWorksV3Api->v3_works_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 
 **patched_v3_work_external_update_request** | [**PatchedV3WorkExternalUpdateRequest**](PatchedV3WorkExternalUpdateRequest.md)|  | [optional] 

### Return type

[**V3WorkExternalUpdate**](V3WorkExternalUpdate.md)

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

# **v3_works_retrieve**
> V3Work v3_works_retrieve(id)

Get A Work information

Get A Work information

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_work import V3Work
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work base.

    try:
        # Get A Work information
        api_response = api_instance.v3_works_retrieve(id)
        print("The response of WorksAppWorksV3Api->v3_works_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work base. | 

### Return type

[**V3Work**](V3Work.md)

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

# **v3_works_summary_retrieve**
> V3Work v3_works_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, type=type, workflow=workflow)

Get Work Summary

Get Work Summary

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.v3_work import V3Work
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
    api_instance = gwm.WorksAppWorksV3Api(api_client)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    group_by = 'group_by_example' # str |  (optional)
    interval = 'interval_example' # str | * `daily` - daily * `weekly` - weekly * `monthly` - monthly * `annually` - annually (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    type = ['type_example'] # List[str] | Type of the work  * `CHARGE` - Charge * `EXPLORE` - Explore * `PAYLOAD_MOVE` - Payload Move * `ADHOC_MOVE_POSITION` - Adhoc Move Position * `ADHOC_MOVE_REGION` - Adhoc Move Region * `ADHOC_MOVE_SPOT` - Adhoc Move Spot (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # Get Work Summary
        api_response = api_instance.v3_works_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, type=type, workflow=workflow)
        print("The response of WorksAppWorksV3Api->v3_works_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorksV3Api->v3_works_summary_retrieve: %s\n" % e)
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

[**V3Work**](V3Work.md)

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

