# gwm.SitesAppSitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_site_create**](SitesAppSitesApi.md#v1_site_create) | **POST** /v1/site | Create new site
[**v1_site_destroy**](SitesAppSitesApi.md#v1_site_destroy) | **DELETE** /v1/site/{id_or_name} | Delete a site
[**v1_site_export_retrieve**](SitesAppSitesApi.md#v1_site_export_retrieve) | **GET** /v1/site/{id_or_name}/export | Export a site
[**v1_site_import_site_create**](SitesAppSitesApi.md#v1_site_import_site_create) | **POST** /v1/site/import_site | Import a site
[**v1_site_list**](SitesAppSitesApi.md#v1_site_list) | **GET** /v1/site | List all sites
[**v1_site_partial_update**](SitesAppSitesApi.md#v1_site_partial_update) | **PATCH** /v1/site/{id_or_name} | Update a site
[**v1_site_retrieve**](SitesAppSitesApi.md#v1_site_retrieve) | **GET** /v1/site/{id_or_name} | Get a site
[**v1_site_status_retrieve**](SitesAppSitesApi.md#v1_site_status_retrieve) | **GET** /v1/site/{id_or_name}/status | Get site status
[**v1_site_update**](SitesAppSitesApi.md#v1_site_update) | **PUT** /v1/site/{id_or_name} | Update a site


# **v1_site_create**
> Site v1_site_create(site_request=site_request)

Create new site

Create new site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site import Site
from gwm.models.site_request import SiteRequest
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    site_request = {"id":"123912","name":"hirano","type":"warehouse","meta_data":{},"endpoint":"https://example.com"} # SiteRequest |  (optional)

    try:
        # Create new site
        api_response = api_instance.v1_site_create(site_request=site_request)
        print("The response of SitesAppSitesApi->v1_site_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_request** | [**SiteRequest**](SiteRequest.md)|  | [optional] 

### Return type

[**Site**](Site.md)

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

# **v1_site_destroy**
> v1_site_destroy(id_or_name)

Delete a site

Delete a site

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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 

    try:
        # Delete a site
        api_instance.v1_site_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 

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

# **v1_site_export_retrieve**
> SiteExport v1_site_export_retrieve(id_or_name)

Export a site

Export a site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site_export import SiteExport
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 

    try:
        # Export a site
        api_response = api_instance.v1_site_export_retrieve(id_or_name)
        print("The response of SitesAppSitesApi->v1_site_export_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_export_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 

### Return type

[**SiteExport**](SiteExport.md)

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

# **v1_site_import_site_create**
> Site v1_site_import_site_create(site_request=site_request)

Import a site

Import a site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site import Site
from gwm.models.site_request import SiteRequest
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    site_request = {"id":"123912","name":"hirano","type":"warehouse","meta_data":{},"endpoint":"https://example.com"} # SiteRequest |  (optional)

    try:
        # Import a site
        api_response = api_instance.v1_site_import_site_create(site_request=site_request)
        print("The response of SitesAppSitesApi->v1_site_import_site_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_import_site_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_request** | [**SiteRequest**](SiteRequest.md)|  | [optional] 

### Return type

[**Site**](Site.md)

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

# **v1_site_list**
> List[Site] v1_site_list(id=id, name=name, type=type)

List all sites

Get all sites

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site import Site
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id = 56 # int |  (optional)
    name = 'name_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # List all sites
        api_response = api_instance.v1_site_list(id=id, name=name, type=type)
        print("The response of SitesAppSitesApi->v1_site_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**List[Site]**](Site.md)

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

# **v1_site_partial_update**
> Site v1_site_partial_update(id_or_name, patched_site_request=patched_site_request)

Update a site

Partially update a site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.patched_site_request import PatchedSiteRequest
from gwm.models.site import Site
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 
    patched_site_request = {"id":"123912","name":"hirano","type":"warehouse","meta_data":{},"endpoint":"https://example.com"} # PatchedSiteRequest |  (optional)

    try:
        # Update a site
        api_response = api_instance.v1_site_partial_update(id_or_name, patched_site_request=patched_site_request)
        print("The response of SitesAppSitesApi->v1_site_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 
 **patched_site_request** | [**PatchedSiteRequest**](PatchedSiteRequest.md)|  | [optional] 

### Return type

[**Site**](Site.md)

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

# **v1_site_retrieve**
> Site v1_site_retrieve(id_or_name)

Get a site

Get a site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site import Site
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 

    try:
        # Get a site
        api_response = api_instance.v1_site_retrieve(id_or_name)
        print("The response of SitesAppSitesApi->v1_site_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 

### Return type

[**Site**](Site.md)

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

# **v1_site_status_retrieve**
> SiteStatus v1_site_status_retrieve(id_or_name)

Get site status

Get site status

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site_status import SiteStatus
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 

    try:
        # Get site status
        api_response = api_instance.v1_site_status_retrieve(id_or_name)
        print("The response of SitesAppSitesApi->v1_site_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_status_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 

### Return type

[**SiteStatus**](SiteStatus.md)

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

# **v1_site_update**
> Site v1_site_update(id_or_name, site_request=site_request)

Update a site

Update a site

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm
from gwm.models.site import Site
from gwm.models.site_request import SiteRequest
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
    api_instance = gwm.SitesAppSitesApi(api_client)
    id_or_name = None # object | 
    site_request = {"id":"123912","name":"hirano","type":"warehouse","meta_data":{},"endpoint":"https://example.com"} # SiteRequest |  (optional)

    try:
        # Update a site
        api_response = api_instance.v1_site_update(id_or_name, site_request=site_request)
        print("The response of SitesAppSitesApi->v1_site_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSitesApi->v1_site_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | [**object**](.md)|  | 
 **site_request** | [**SiteRequest**](SiteRequest.md)|  | [optional] 

### Return type

[**Site**](Site.md)

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

