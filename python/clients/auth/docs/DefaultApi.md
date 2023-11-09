# auth.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_own_password**](DefaultApi.md#change_own_password) | **POST** /me/password | Change Own Password
[**change_user_password**](DefaultApi.md#change_user_password) | **PATCH** /users/{username}/password | Change User Password
[**create_user**](DefaultApi.md#create_user) | **PUT** /users/{username} | Create User
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{username} | Delete User
[**get_access_tokens**](DefaultApi.md#get_access_tokens) | **GET** /access-tokens | Get Access Tokens
[**get_api_tokens**](DefaultApi.md#get_api_tokens) | **GET** /api-tokens | Get Api Tokens
[**get_elastic_search_token**](DefaultApi.md#get_elastic_search_token) | **POST** /elastic-search/token | Get Token
[**get_own_user**](DefaultApi.md#get_own_user) | **GET** /me | Get Own User
[**get_token**](DefaultApi.md#get_token) | **POST** /token | Token
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{username} | Get User
[**get_users**](DefaultApi.md#get_users) | **GET** /users | Get Users
[**merge_users**](DefaultApi.md#merge_users) | **PATCH** /users | Merge Users
[**update_own_user**](DefaultApi.md#update_own_user) | **PATCH** /me | Update Own User
[**update_user**](DefaultApi.md#update_user) | **PATCH** /users/{username} | Update User
[**userinfo**](DefaultApi.md#userinfo) | **GET** /userinfo | Userinfo


# **change_own_password**
> object change_own_password(own_password)

Change Own Password

Change own password

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.own_password import OwnPassword
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    own_password = auth.OwnPassword() # OwnPassword | 

    try:
        # Change Own Password
        api_response = api_instance.change_own_password(own_password)
        print("The response of DefaultApi->change_own_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->change_own_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **own_password** | [**OwnPassword**](OwnPassword.md)|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**204** | No Content |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> Response change_user_password(username, password)

Change User Password

Change given user's password (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.password import Password
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str | 
    password = auth.Password() # Password | 

    try:
        # Change User Password
        api_response = api_instance.change_user_password(username, password)
        print("The response of DefaultApi->change_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->change_user_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | [**Password**](Password.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> Response create_user(username, create)

Create User

Create a new user (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.create import Create
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str | 
    create = auth.Create() # Create | 

    try:
        # Create User
        api_response = api_instance.create_user(username, create)
        print("The response of DefaultApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **create** | [**Create**](Create.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

Delete User

Delete given user (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str | 

    try:
        # Delete User
        api_instance.delete_user(username)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_tokens**
> List[AccessTokenResponse] get_access_tokens()

Get Access Tokens

Get all access tokens

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.access_token_response import AccessTokenResponse
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)

    try:
        # Get Access Tokens
        api_response = api_instance.get_access_tokens()
        print("The response of DefaultApi->get_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_access_tokens: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AccessTokenResponse]**](AccessTokenResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_tokens**
> List[APITokenResponse] get_api_tokens()

Get Api Tokens

Get all API tokens

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.api_token_response import APITokenResponse
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)

    try:
        # Get Api Tokens
        api_response = api_instance.get_api_tokens()
        print("The response of DefaultApi->get_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_api_tokens: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[APITokenResponse]**](APITokenResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elastic_search_token**
> AuthWebViewsEsTokenResponse get_elastic_search_token()

Get Token

Get an access token for hosted Elastic Search

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.auth_web_views_es_token_response import AuthWebViewsEsTokenResponse
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)

    try:
        # Get Token
        api_response = api_instance.get_elastic_search_token()
        print("The response of DefaultApi->get_elastic_search_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_elastic_search_token: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthWebViewsEsTokenResponse**](AuthWebViewsEsTokenResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_own_user**
> Response get_own_user()

Get Own User

Get own user / profile details

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)

    try:
        # Get Own User
        api_response = api_instance.get_own_user()
        print("The response of DefaultApi->get_own_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_own_user: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> AuthWebViewsOidcTokenResponse get_token(username=username, password=password)

Token

OIDC-/OAuth2-compliant token endpoint for machine-to-machine communication

### Example

```python
import time
import os
import auth
from auth.models.auth_web_views_oidc_token_response import AuthWebViewsOidcTokenResponse
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str |  (optional)
    password = 'password_example' # str |  (optional)

    try:
        # Token
        api_response = api_instance.get_token(username=username, password=password)
        print("The response of DefaultApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

[**AuthWebViewsOidcTokenResponse**](AuthWebViewsOidcTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> Response get_user(username)

Get User

Get given user / profile details (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(username)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[Response] get_users(username=username, display_name=display_name, group=group)

Get Users

Get all users / profile details (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = '' # str |  (optional) (default to '')
    display_name = '' # str |  (optional) (default to '')
    group = '' # str |  (optional) (default to '')

    try:
        # Get Users
        api_response = api_instance.get_users(username=username, display_name=display_name, group=group)
        print("The response of DefaultApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] [default to &#39;&#39;]
 **display_name** | **str**|  | [optional] [default to &#39;&#39;]
 **group** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[Response]**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_users**
> List[Response] merge_users(merge)

Merge Users

Merge (mass create or update) users (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.merge import Merge
from auth.models.response import Response
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    merge = [auth.Merge()] # List[Merge] | 

    try:
        # Merge Users
        api_response = api_instance.merge_users(merge)
        print("The response of DefaultApi->merge_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->merge_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge** | [**List[Merge]**](Merge.md)|  | 

### Return type

[**List[Response]**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_own_user**
> Response update_own_user(update_self)

Update Own User

Update own user

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.response import Response
from auth.models.update_self import UpdateSelf
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    update_self = auth.UpdateSelf() # UpdateSelf | 

    try:
        # Update Own User
        api_response = api_instance.update_own_user(update_self)
        print("The response of DefaultApi->update_own_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_own_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_self** | [**UpdateSelf**](UpdateSelf.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> Response update_user(username, update)

Update User

Update given user / profile details (by admin)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.response import Response
from auth.models.update import Update
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)
    username = 'username_example' # str | 
    update = auth.Update() # Update | 

    try:
        # Update User
        api_response = api_instance.update_user(username, update)
        print("The response of DefaultApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **update** | [**Update**](Update.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userinfo**
> Userinfo userinfo()

Userinfo

OIDC-/OAuth2-compliant userinfo endpoint for machine-to-machine communication

### Example

* OAuth Authentication (OAuth2PasswordBearer):
* Bearer (opaque) Authentication (Bearer):
```python
import time
import os
import auth
from auth.models.userinfo import Userinfo
from auth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (opaque): Bearer
configuration = auth.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth.DefaultApi(api_client)

    try:
        # Userinfo
        api_response = api_instance.userinfo()
        print("The response of DefaultApi->userinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->userinfo: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Userinfo**](Userinfo.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

