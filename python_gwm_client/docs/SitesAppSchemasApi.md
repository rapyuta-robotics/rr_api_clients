# gwm_client.SitesAppSchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_schema_create**](SitesAppSchemasApi.md#v1_schema_create) | **POST** /v1/schema | 
[**v1_schema_destroy**](SitesAppSchemasApi.md#v1_schema_destroy) | **DELETE** /v1/schema/{id_or_name} | 
[**v1_schema_list**](SitesAppSchemasApi.md#v1_schema_list) | **GET** /v1/schema | 
[**v1_schema_partial_update**](SitesAppSchemasApi.md#v1_schema_partial_update) | **PATCH** /v1/schema/{id_or_name} | 
[**v1_schema_retrieve**](SitesAppSchemasApi.md#v1_schema_retrieve) | **GET** /v1/schema/{id_or_name} | 
[**v1_schema_update**](SitesAppSchemasApi.md#v1_schema_update) | **PUT** /v1/schema/{id_or_name} | 


# **v1_schema_create**
> ModelSchema v1_schema_create(schema_request)



Manage Site Schemas<br>                    Schemas are ways to validate metadata and provide the information to fill into the metadata.                     An additional field (type) can also be provided to                      narrow down the validation. For example: A spot with type drop will look                            through all the schema for schemas that match spot and type drop. The type field is optionally                            provided. It will validate with both a schema that has (type=None) and (type=Drop).                            Next it will compare the schema with the schema field for both schemas and uses fastjsonschema (https://jsonschema.net/home)

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.model_schema import ModelSchema
from gwm_client.models.schema_request import SchemaRequest
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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    schema_request = {"id":4,"resource":"node","type":"drop","schema":{"errorMessage":{"properties":{"spin_turn":"should be of type integer & should be one of 0,1,2"}},"properties":{"spin_turn":{"default":1,"enum":[0,1,2],"enumNames":["Disabled","Optimal","Always"],"title":"Spin Turn","type":"number"}}}} # SchemaRequest | 

    try:
        api_response = api_instance.v1_schema_create(schema_request)
        print("The response of SitesAppSchemasApi->v1_schema_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_request** | [**SchemaRequest**](SchemaRequest.md)|  | 

### Return type

[**ModelSchema**](ModelSchema.md)

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

# **v1_schema_destroy**
> v1_schema_destroy(id_or_name)



Manage Site Schemas

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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    id_or_name = '1' # str | Schema ID or Name.

    try:
        api_instance.v1_schema_destroy(id_or_name)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Schema ID or Name. | 

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

# **v1_schema_list**
> List[ModelSchema] v1_schema_list(field_name=field_name, name=name, resource=resource, type=type)



Manage Site Schemas

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.model_schema import ModelSchema
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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    field_name = 'field_name_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    resource = 'resource_example' # str | Which resource applies this schema (node, edge)  * `site` - Site * `spotannotation` - Spot * `region` - Region * `node` - Node * `edge` - Edge * `map` - Map * `robot` - Robot * `robotdescriptor` - Robot Descriptor * `agent` - Agent * `externaldevice` - External Device * `errortype` - Error Type * `erroraction` - Error Action * `work` - Work * `workpayloadfragment` - Work Payload Fragment * `layer` - Layer * `agenttask` - Agent Task * `agenttaskfragment` - Agent Task Fragment * `container` - Container * `containerdescriptor` - Container Descriptor * `assetlocation` - Asset Location (optional)
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.v1_schema_list(field_name=field_name, name=name, resource=resource, type=type)
        print("The response of SitesAppSchemasApi->v1_schema_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **resource** | **str**| Which resource applies this schema (node, edge)  * &#x60;site&#x60; - Site * &#x60;spotannotation&#x60; - Spot * &#x60;region&#x60; - Region * &#x60;node&#x60; - Node * &#x60;edge&#x60; - Edge * &#x60;map&#x60; - Map * &#x60;robot&#x60; - Robot * &#x60;robotdescriptor&#x60; - Robot Descriptor * &#x60;agent&#x60; - Agent * &#x60;externaldevice&#x60; - External Device * &#x60;errortype&#x60; - Error Type * &#x60;erroraction&#x60; - Error Action * &#x60;work&#x60; - Work * &#x60;workpayloadfragment&#x60; - Work Payload Fragment * &#x60;layer&#x60; - Layer * &#x60;agenttask&#x60; - Agent Task * &#x60;agenttaskfragment&#x60; - Agent Task Fragment * &#x60;container&#x60; - Container * &#x60;containerdescriptor&#x60; - Container Descriptor * &#x60;assetlocation&#x60; - Asset Location | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**List[ModelSchema]**](ModelSchema.md)

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

# **v1_schema_partial_update**
> ModelSchema v1_schema_partial_update(id_or_name, patched_schema_request=patched_schema_request)



Manage Site Schemas

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.model_schema import ModelSchema
from gwm_client.models.patched_schema_request import PatchedSchemaRequest
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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    id_or_name = '1' # str | Schema ID or Name.
    patched_schema_request = {"id":4,"resource":"node","type":"drop","schema":{"errorMessage":{"properties":{"spin_turn":"should be of type integer & should be one of 0,1,2"}},"properties":{"spin_turn":{"default":1,"enum":[0,1,2],"enumNames":["Disabled","Optimal","Always"],"title":"Spin Turn","type":"number"}}}} # PatchedSchemaRequest |  (optional)

    try:
        api_response = api_instance.v1_schema_partial_update(id_or_name, patched_schema_request=patched_schema_request)
        print("The response of SitesAppSchemasApi->v1_schema_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Schema ID or Name. | 
 **patched_schema_request** | [**PatchedSchemaRequest**](PatchedSchemaRequest.md)|  | [optional] 

### Return type

[**ModelSchema**](ModelSchema.md)

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

# **v1_schema_retrieve**
> ModelSchema v1_schema_retrieve(id_or_name)



Manage Site Schemas

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.model_schema import ModelSchema
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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    id_or_name = '1' # str | Schema ID or Name.

    try:
        api_response = api_instance.v1_schema_retrieve(id_or_name)
        print("The response of SitesAppSchemasApi->v1_schema_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Schema ID or Name. | 

### Return type

[**ModelSchema**](ModelSchema.md)

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

# **v1_schema_update**
> ModelSchema v1_schema_update(id_or_name, schema_request)



Manage Site Schemas

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import gwm_client
from gwm_client.models.model_schema import ModelSchema
from gwm_client.models.schema_request import SchemaRequest
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
    api_instance = gwm_client.SitesAppSchemasApi(api_client)
    id_or_name = '1' # str | Schema ID or Name.
    schema_request = {"id":4,"resource":"node","type":"drop","schema":{"errorMessage":{"properties":{"spin_turn":"should be of type integer & should be one of 0,1,2"}},"properties":{"spin_turn":{"default":1,"enum":[0,1,2],"enumNames":["Disabled","Optimal","Always"],"title":"Spin Turn","type":"number"}}}} # SchemaRequest | 

    try:
        api_response = api_instance.v1_schema_update(id_or_name, schema_request)
        print("The response of SitesAppSchemasApi->v1_schema_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesAppSchemasApi->v1_schema_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Schema ID or Name. | 
 **schema_request** | [**SchemaRequest**](SchemaRequest.md)|  | 

### Return type

[**ModelSchema**](ModelSchema.md)

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

