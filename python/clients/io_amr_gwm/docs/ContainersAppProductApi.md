# io_amr_gwm.ContainersAppProductApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1alpha1_products_bulk_patch_update_partial_update**](ContainersAppProductApi.md#v1alpha1_products_bulk_patch_update_partial_update) | **PATCH** /v1alpha1/products/bulk_patch_update | Patch products
[**v1alpha1_products_count_retrieve**](ContainersAppProductApi.md#v1alpha1_products_count_retrieve) | **GET** /v1alpha1/products/count | 
[**v1alpha1_products_create**](ContainersAppProductApi.md#v1alpha1_products_create) | **POST** /v1alpha1/products | Create Products
[**v1alpha1_products_delete_destroy**](ContainersAppProductApi.md#v1alpha1_products_delete_destroy) | **DELETE** /v1alpha1/products/delete | Bulk Delete products
[**v1alpha1_products_destroy**](ContainersAppProductApi.md#v1alpha1_products_destroy) | **DELETE** /v1alpha1/products/{id} | 
[**v1alpha1_products_list**](ContainersAppProductApi.md#v1alpha1_products_list) | **GET** /v1alpha1/products | 
[**v1alpha1_products_partial_update**](ContainersAppProductApi.md#v1alpha1_products_partial_update) | **PATCH** /v1alpha1/products/{id} | 
[**v1alpha1_products_retrieve**](ContainersAppProductApi.md#v1alpha1_products_retrieve) | **GET** /v1alpha1/products/{id} | 
[**v1alpha1_products_update**](ContainersAppProductApi.md#v1alpha1_products_update) | **PUT** /v1alpha1/products/{id} | 


# **v1alpha1_products_bulk_patch_update_partial_update**
> v1alpha1_products_bulk_patch_update_partial_update(patched_product_request)

Patch products

Patch products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_product_request import PatchedProductRequest
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    patched_product_request = [io_amr_gwm.PatchedProductRequest()] # List[PatchedProductRequest] | 

    try:
        # Patch products
        api_instance.v1alpha1_products_bulk_patch_update_partial_update(patched_product_request)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_bulk_patch_update_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_product_request** | [**List[PatchedProductRequest]**](PatchedProductRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha1_products_count_retrieve**
> int v1alpha1_products_count_retrieve(id=id, name=name, product_id=product_id)



Manage Products

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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    product_id = ['product_id_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.v1alpha1_products_count_retrieve(id=id, name=name, product_id=product_id)
        print("The response of ContainersAppProductApi->v1alpha1_products_count_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_count_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **product_id** | [**List[str]**](str.md)|  | [optional] 

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

# **v1alpha1_products_create**
> PaginatedProductList v1alpha1_products_create(product_request, id=id, name=name, page=page, page_size=page_size, product_id=product_id)

Create Products

Create Products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_product_list import PaginatedProductList
from io_amr_gwm.models.product_request import ProductRequest
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    product_request = [io_amr_gwm.ProductRequest()] # List[ProductRequest] | 
    id = 56 # int |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    product_id = ['product_id_example'] # List[str] |  (optional)

    try:
        # Create Products
        api_response = api_instance.v1alpha1_products_create(product_request, id=id, name=name, page=page, page_size=page_size, product_id=product_id)
        print("The response of ContainersAppProductApi->v1alpha1_products_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_request** | [**List[ProductRequest]**](ProductRequest.md)|  | 
 **id** | **int**|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **product_id** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedProductList**](PaginatedProductList.md)

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

# **v1alpha1_products_delete_destroy**
> v1alpha1_products_delete_destroy(id=id, name=name, product_id=product_id)

Bulk Delete products

Bulk Delete  products

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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = [3.4] # List[float] | List of Container Slot IDs (optional)
    name = ['name_example'] # List[str] | List of product names (optional)
    product_id = [3.4] # List[float] | List of product ids (optional)

    try:
        # Bulk Delete products
        api_instance.v1alpha1_products_delete_destroy(id=id, name=name, product_id=product_id)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_delete_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[float]**](float.md)| List of Container Slot IDs | [optional] 
 **name** | [**List[str]**](str.md)| List of product names | [optional] 
 **product_id** | [**List[float]**](float.md)| List of product ids | [optional] 

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

# **v1alpha1_products_destroy**
> v1alpha1_products_destroy(id)



Manage Products

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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int | A unique integer value identifying this product.

    try:
        api_instance.v1alpha1_products_destroy(id)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 

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

# **v1alpha1_products_list**
> PaginatedProductList v1alpha1_products_list(id=id, name=name, page=page, page_size=page_size, product_id=product_id)



Manage Products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.paginated_product_list import PaginatedProductList
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int |  (optional)
    name = ['name_example'] # List[str] |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    product_id = ['product_id_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.v1alpha1_products_list(id=id, name=name, page=page, page_size=page_size, product_id=product_id)
        print("The response of ContainersAppProductApi->v1alpha1_products_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **name** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **product_id** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedProductList**](PaginatedProductList.md)

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

# **v1alpha1_products_partial_update**
> Product v1alpha1_products_partial_update(id, patched_product_request=patched_product_request)



Manage Products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.patched_product_request import PatchedProductRequest
from io_amr_gwm.models.product import Product
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    patched_product_request = io_amr_gwm.PatchedProductRequest() # PatchedProductRequest |  (optional)

    try:
        api_response = api_instance.v1alpha1_products_partial_update(id, patched_product_request=patched_product_request)
        print("The response of ContainersAppProductApi->v1alpha1_products_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **patched_product_request** | [**PatchedProductRequest**](PatchedProductRequest.md)|  | [optional] 

### Return type

[**Product**](Product.md)

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

# **v1alpha1_products_retrieve**
> Product v1alpha1_products_retrieve(id)



Manage Products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.product import Product
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int | A unique integer value identifying this product.

    try:
        api_response = api_instance.v1alpha1_products_retrieve(id)
        print("The response of ContainersAppProductApi->v1alpha1_products_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 

### Return type

[**Product**](Product.md)

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

# **v1alpha1_products_update**
> Product v1alpha1_products_update(id, product_request)



Manage Products

### Example

* Bearer Authentication (tokenAuth):
```python
import time
import os
import io_amr_gwm
from io_amr_gwm.models.product import Product
from io_amr_gwm.models.product_request import ProductRequest
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
    api_instance = io_amr_gwm.ContainersAppProductApi(api_client)
    id = 56 # int | A unique integer value identifying this product.
    product_request = io_amr_gwm.ProductRequest() # ProductRequest | 

    try:
        api_response = api_instance.v1alpha1_products_update(id, product_request)
        print("The response of ContainersAppProductApi->v1alpha1_products_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersAppProductApi->v1alpha1_products_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **product_request** | [**ProductRequest**](ProductRequest.md)|  | 

### Return type

[**Product**](Product.md)

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

