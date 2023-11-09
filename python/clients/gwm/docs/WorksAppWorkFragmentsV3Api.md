# gwm_client.WorksAppWorkFragmentsV3Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_fragments_bulk_internal_update**](WorksAppWorkFragmentsV3Api.md#v3_fragments_bulk_internal_update) | **PATCH** /v3/fragments/internal_update | Bulk Internal Update Fragments
[**v3_fragments_count_retrieve**](WorksAppWorkFragmentsV3Api.md#v3_fragments_count_retrieve) | **GET** /v3/fragments/count | 
[**v3_fragments_create**](WorksAppWorkFragmentsV3Api.md#v3_fragments_create) | **POST** /v3/fragments | Create  Fragments
[**v3_fragments_internal_update_partial_update**](WorksAppWorkFragmentsV3Api.md#v3_fragments_internal_update_partial_update) | **PATCH** /v3/fragments/{id}/internal_update | Internal Update Fragment
[**v3_fragments_list**](WorksAppWorkFragmentsV3Api.md#v3_fragments_list) | **GET** /v3/fragments | 
[**v3_fragments_retrieve**](WorksAppWorkFragmentsV3Api.md#v3_fragments_retrieve) | **GET** /v3/fragments/{id} | 
[**v3_fragments_summary_retrieve**](WorksAppWorkFragmentsV3Api.md#v3_fragments_summary_retrieve) | **GET** /v3/fragments/summary | Get Fragment Summary


# **v3_fragments_bulk_internal_update**
> V3WorkFragment v3_fragments_bulk_internal_update(v3_work_fragment_bulk_update_request)

Bulk Internal Update Fragments

Bulk Internal Update Fragnments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.v3_work_fragment import V3WorkFragment
from gwm_client.models.v3_work_fragment_bulk_update_request import V3WorkFragmentBulkUpdateRequest
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    v3_work_fragment_bulk_update_request = [gwm_client.V3WorkFragmentBulkUpdateRequest()] # List[V3WorkFragmentBulkUpdateRequest] | 

    try:
        # Bulk Internal Update Fragments
        api_response = api_instance.v3_fragments_bulk_internal_update(v3_work_fragment_bulk_update_request)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_bulk_internal_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_bulk_internal_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_work_fragment_bulk_update_request** | [**List[V3WorkFragmentBulkUpdateRequest]**](V3WorkFragmentBulkUpdateRequest.md)|  | 

### Return type

[**V3WorkFragment**](V3WorkFragment.md)

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

# **v3_fragments_count_retrieve**
> int v3_fragments_count_retrieve(end_date=end_date, id=id, name=name, ordering=ordering, parent=parent, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type)



Get Fragments

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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [56] # List[int] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    parent = [56] # List[int] |  (optional)
    quantity_requested_max = 56 # int | How many was requested by the order (optional)
    quantity_requested_min = 56 # int | How many was requested by the order (optional)
    rejection_reason = 'rejection_reason_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = ['status_example'] # List[str] | Status  * `NOT_STARTED` - Not Started * `IN_PROGRESS` - In Progress * `COMPLETED` - Completed * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `SKIPPED` - Skipped * `PARTIALLY_COMPLETED` - Partially Completed (optional)
    type = 'type_example' # str | * `ITEM_MOVE` - Item Move * `CONTAINER_MOVE` - Container Move (optional)

    try:
        api_response = api_instance.v3_fragments_count_retrieve(end_date=end_date, id=id, name=name, ordering=ordering, parent=parent, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_count_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_count_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | [optional] 
 **id** | [**List[int]**](int.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **parent** | [**List[int]**](int.md)|  | [optional] 
 **quantity_requested_max** | **int**| How many was requested by the order | [optional] 
 **quantity_requested_min** | **int**| How many was requested by the order | [optional] 
 **rejection_reason** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **status** | [**List[str]**](str.md)| Status  * &#x60;NOT_STARTED&#x60; - Not Started * &#x60;IN_PROGRESS&#x60; - In Progress * &#x60;COMPLETED&#x60; - Completed * &#x60;REJECTED&#x60; - Rejected * &#x60;CANCELLED&#x60; - Cancelled * &#x60;TERMINAL_WITH_EXCEPTION&#x60; - Terminal With Exception * &#x60;SKIPPED&#x60; - Skipped * &#x60;PARTIALLY_COMPLETED&#x60; - Partially Completed | [optional] 
 **type** | **str**| * &#x60;ITEM_MOVE&#x60; - Item Move * &#x60;CONTAINER_MOVE&#x60; - Container Move | [optional] 

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

# **v3_fragments_create**
> List[V3WorkFragment] v3_fragments_create(v3_work_fragment_request)

Create  Fragments

Create Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.v3_work_fragment import V3WorkFragment
from gwm_client.models.v3_work_fragment_request import V3WorkFragmentRequest
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    v3_work_fragment_request = [gwm_client.V3WorkFragmentRequest()] # List[V3WorkFragmentRequest] | 

    try:
        # Create  Fragments
        api_response = api_instance.v3_fragments_create(v3_work_fragment_request)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v3_work_fragment_request** | [**List[V3WorkFragmentRequest]**](V3WorkFragmentRequest.md)|  | 

### Return type

[**List[V3WorkFragment]**](V3WorkFragment.md)

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

# **v3_fragments_internal_update_partial_update**
> V3WorkFragment v3_fragments_internal_update_partial_update(id, patched_v3_work_fragment_request=patched_v3_work_fragment_request)

Internal Update Fragment

Internal Update Fragment

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.patched_v3_work_fragment_request import PatchedV3WorkFragmentRequest
from gwm_client.models.v3_work_fragment import V3WorkFragment
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work payload fragment.
    patched_v3_work_fragment_request = {"status":"REJECTED","quantity_delivered":5} # PatchedV3WorkFragmentRequest |  (optional)

    try:
        # Internal Update Fragment
        api_response = api_instance.v3_fragments_internal_update_partial_update(id, patched_v3_work_fragment_request=patched_v3_work_fragment_request)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_internal_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_internal_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work payload fragment. | 
 **patched_v3_work_fragment_request** | [**PatchedV3WorkFragmentRequest**](PatchedV3WorkFragmentRequest.md)|  | [optional] 

### Return type

[**V3WorkFragment**](V3WorkFragment.md)

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

# **v3_fragments_list**
> PaginatedV3WorkFragmentList v3_fragments_list(application_data=application_data, end_date=end_date, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, parent=parent, parent__application_data=parent__application_data, parent__meta_data=parent__meta_data, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type, with_task_fragments=with_task_fragments)



List Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.paginated_v3_work_fragment_list import PaginatedV3WorkFragmentList
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    application_data = 'application_data_example' # str | filter by application_data query (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [3.4] # List[float] | filter fragments by id (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent = [3.4] # List[float] | filter fragments by parent work (optional)
    parent__application_data = 'parent__application_data_example' # str | filter by parent__application_data query (optional)
    parent__meta_data = 'parent__meta_data_example' # str | filter by parent__meta_data query (optional)
    quantity_requested_max = 56 # int | How many was requested by the order (optional)
    quantity_requested_min = 56 # int | How many was requested by the order (optional)
    rejection_reason = 'rejection_reason_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = 'status_example' # str | filter by work fragment status (optional)
    type = 'type_example' # str | * `ITEM_MOVE` - Item Move * `CONTAINER_MOVE` - Container Move (optional)
    with_task_fragments = True # bool | filter fragments by parent work (optional)

    try:
        api_response = api_instance.v3_fragments_list(application_data=application_data, end_date=end_date, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, parent=parent, parent__application_data=parent__application_data, parent__meta_data=parent__meta_data, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type, with_task_fragments=with_task_fragments)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_data** | **str**| filter by application_data query | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **id** | [**List[float]**](float.md)| filter fragments by id | [optional] 
 **meta_data** | **str**| filter by meta_data query | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent** | [**List[float]**](float.md)| filter fragments by parent work | [optional] 
 **parent__application_data** | **str**| filter by parent__application_data query | [optional] 
 **parent__meta_data** | **str**| filter by parent__meta_data query | [optional] 
 **quantity_requested_max** | **int**| How many was requested by the order | [optional] 
 **quantity_requested_min** | **int**| How many was requested by the order | [optional] 
 **rejection_reason** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **status** | **str**| filter by work fragment status | [optional] 
 **type** | **str**| * &#x60;ITEM_MOVE&#x60; - Item Move * &#x60;CONTAINER_MOVE&#x60; - Container Move | [optional] 
 **with_task_fragments** | **bool**| filter fragments by parent work | [optional] 

### Return type

[**PaginatedV3WorkFragmentList**](PaginatedV3WorkFragmentList.md)

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

# **v3_fragments_retrieve**
> V3WorkFragment v3_fragments_retrieve(id)



Get Fragment Detail

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.v3_work_fragment import V3WorkFragment
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    id = 56 # int | A unique integer value identifying this work payload fragment.

    try:
        api_response = api_instance.v3_fragments_retrieve(id)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work payload fragment. | 

### Return type

[**V3WorkFragment**](V3WorkFragment.md)

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

# **v3_fragments_summary_retrieve**
> V3WorkFragment v3_fragments_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, workflow=workflow)

Get Fragment Summary

Get Fragment Summary

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.v3_work_fragment import V3WorkFragment
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
    api_instance = gwm_client.WorksAppWorkFragmentsV3Api(api_client)
    end_date = 'end_date_example' # str | filter by end date (optional)
    group_by = ['group_by_example'] # List[str] | group by (optional)
    interval = 'interval_example' # str | interval (optional)
    start_date = 'start_date_example' # str | filter by start date (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # Get Fragment Summary
        api_response = api_instance.v3_fragments_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, workflow=workflow)
        print("The response of WorksAppWorkFragmentsV3Api->v3_fragments_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV3Api->v3_fragments_summary_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| filter by end date | [optional] 
 **group_by** | [**List[str]**](str.md)| group by | [optional] 
 **interval** | **str**| interval | [optional] 
 **start_date** | **str**| filter by start date | [optional] 
 **workflow** | **str**|  | [optional] 

### Return type

[**V3WorkFragment**](V3WorkFragment.md)

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

