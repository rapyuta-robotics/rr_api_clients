# io_amr_gwm.WorksAppWorkFragmentsV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_fragments_internal_update_partial_update**](WorksAppWorkFragmentsV2Api.md#v2_fragments_internal_update_partial_update) | **PATCH** /v2/fragments/{id}/internal_update | 
[**v2_fragments_internal_update_update**](WorksAppWorkFragmentsV2Api.md#v2_fragments_internal_update_update) | **PUT** /v2/fragments/{id}/internal_update | 
[**v2_fragments_list**](WorksAppWorkFragmentsV2Api.md#v2_fragments_list) | **GET** /v2/fragments | 
[**v2_fragments_retrieve**](WorksAppWorkFragmentsV2Api.md#v2_fragments_retrieve) | **GET** /v2/fragments/{id} | 
[**v2_fragments_summary_retrieve**](WorksAppWorkFragmentsV2Api.md#v2_fragments_summary_retrieve) | **GET** /v2/fragments/summary | Get Fragment Summary


# **v2_fragments_internal_update_partial_update**
> InternalWorkPayloadFragment v2_fragments_internal_update_partial_update(id, patched_internal_work_payload_fragment_request=patched_internal_work_payload_fragment_request)



Get Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.internal_work_payload_fragment import InternalWorkPayloadFragment
from io_amr_gwm.models.patched_internal_work_payload_fragment_request import PatchedInternalWorkPayloadFragmentRequest
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
    api_instance = io_amr_gwm.WorksAppWorkFragmentsV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work payload fragment.
    patched_internal_work_payload_fragment_request = io_amr_gwm.PatchedInternalWorkPayloadFragmentRequest() # PatchedInternalWorkPayloadFragmentRequest |  (optional)

    try:
        api_response = api_instance.v2_fragments_internal_update_partial_update(id, patched_internal_work_payload_fragment_request=patched_internal_work_payload_fragment_request)
        print("The response of WorksAppWorkFragmentsV2Api->v2_fragments_internal_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV2Api->v2_fragments_internal_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work payload fragment. | 
 **patched_internal_work_payload_fragment_request** | [**PatchedInternalWorkPayloadFragmentRequest**](PatchedInternalWorkPayloadFragmentRequest.md)|  | [optional] 

### Return type

[**InternalWorkPayloadFragment**](InternalWorkPayloadFragment.md)

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

# **v2_fragments_internal_update_update**
> InternalWorkPayloadFragment v2_fragments_internal_update_update(id, internal_work_payload_fragment_request=internal_work_payload_fragment_request)



Get Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.internal_work_payload_fragment import InternalWorkPayloadFragment
from io_amr_gwm.models.internal_work_payload_fragment_request import InternalWorkPayloadFragmentRequest
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
    api_instance = io_amr_gwm.WorksAppWorkFragmentsV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work payload fragment.
    internal_work_payload_fragment_request = io_amr_gwm.InternalWorkPayloadFragmentRequest() # InternalWorkPayloadFragmentRequest |  (optional)

    try:
        api_response = api_instance.v2_fragments_internal_update_update(id, internal_work_payload_fragment_request=internal_work_payload_fragment_request)
        print("The response of WorksAppWorkFragmentsV2Api->v2_fragments_internal_update_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV2Api->v2_fragments_internal_update_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work payload fragment. | 
 **internal_work_payload_fragment_request** | [**InternalWorkPayloadFragmentRequest**](InternalWorkPayloadFragmentRequest.md)|  | [optional] 

### Return type

[**InternalWorkPayloadFragment**](InternalWorkPayloadFragment.md)

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

# **v2_fragments_list**
> PaginatedWorkPayloadFragmentList v2_fragments_list(application_data=application_data, end_date=end_date, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, parent=parent, parent__application_data=parent__application_data, parent__meta_data=parent__meta_data, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type)



List Fragments

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_work_payload_fragment_list import PaginatedWorkPayloadFragmentList
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
    api_instance = io_amr_gwm.WorksAppWorkFragmentsV2Api(api_client)
    application_data = 'application_data_example' # str | filter by application_data query (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    id = [3.4] # List[float] | filter fragments by id (optional)
    meta_data = 'meta_data_example' # str | filter by meta_data query (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    parent = 3.4 # float | filter fragments by parent work (optional)
    parent__application_data = 'parent__application_data_example' # str | filter by parent__application_data query (optional)
    parent__meta_data = 'parent__meta_data_example' # str | filter by parent__meta_data query (optional)
    quantity_requested_max = 3.4 # float | filter by work fragment quantity_requested max value (optional)
    quantity_requested_min = 3.4 # float | filter by work fragment quantity_requested min value (optional)
    rejection_reason = 'rejection_reason_example' # str | filter by work fragment rejection_reason (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    status = 'status_example' # str | filter by work fragment status (optional)
    type = 'type_example' # str | * `ITEM_MOVE` - Item Move * `CONTAINER_MOVE` - Container Move (optional)

    try:
        api_response = api_instance.v2_fragments_list(application_data=application_data, end_date=end_date, id=id, meta_data=meta_data, name=name, ordering=ordering, page=page, page_size=page_size, parent=parent, parent__application_data=parent__application_data, parent__meta_data=parent__meta_data, quantity_requested_max=quantity_requested_max, quantity_requested_min=quantity_requested_min, rejection_reason=rejection_reason, start_date=start_date, status=status, type=type)
        print("The response of WorksAppWorkFragmentsV2Api->v2_fragments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV2Api->v2_fragments_list: %s\n" % e)
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
 **parent** | **float**| filter fragments by parent work | [optional] 
 **parent__application_data** | **str**| filter by parent__application_data query | [optional] 
 **parent__meta_data** | **str**| filter by parent__meta_data query | [optional] 
 **quantity_requested_max** | **float**| filter by work fragment quantity_requested max value | [optional] 
 **quantity_requested_min** | **float**| filter by work fragment quantity_requested min value | [optional] 
 **rejection_reason** | **str**| filter by work fragment rejection_reason | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **status** | **str**| filter by work fragment status | [optional] 
 **type** | **str**| * &#x60;ITEM_MOVE&#x60; - Item Move * &#x60;CONTAINER_MOVE&#x60; - Container Move | [optional] 

### Return type

[**PaginatedWorkPayloadFragmentList**](PaginatedWorkPayloadFragmentList.md)

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

# **v2_fragments_retrieve**
> WorkPayloadFragment v2_fragments_retrieve(id)



Get Fragment Detail

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.work_payload_fragment import WorkPayloadFragment
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
    api_instance = io_amr_gwm.WorksAppWorkFragmentsV2Api(api_client)
    id = 56 # int | A unique integer value identifying this work payload fragment.

    try:
        api_response = api_instance.v2_fragments_retrieve(id)
        print("The response of WorksAppWorkFragmentsV2Api->v2_fragments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV2Api->v2_fragments_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this work payload fragment. | 

### Return type

[**WorkPayloadFragment**](WorkPayloadFragment.md)

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

# **v2_fragments_summary_retrieve**
> WorkPayloadFragment v2_fragments_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, workflow=workflow)

Get Fragment Summary

Get Fragment Summary

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.work_payload_fragment import WorkPayloadFragment
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
    api_instance = io_amr_gwm.WorksAppWorkFragmentsV2Api(api_client)
    end_date = 'end_date_example' # str | filter by end date (optional)
    group_by = ['group_by_example'] # List[str] | group by (optional)
    interval = 'interval_example' # str | interval (optional)
    start_date = 'start_date_example' # str | filter by start date (optional)
    workflow = 'workflow_example' # str |  (optional)

    try:
        # Get Fragment Summary
        api_response = api_instance.v2_fragments_summary_retrieve(end_date=end_date, group_by=group_by, interval=interval, start_date=start_date, workflow=workflow)
        print("The response of WorksAppWorkFragmentsV2Api->v2_fragments_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorksAppWorkFragmentsV2Api->v2_fragments_summary_retrieve: %s\n" % e)
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

[**WorkPayloadFragment**](WorkPayloadFragment.md)

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

