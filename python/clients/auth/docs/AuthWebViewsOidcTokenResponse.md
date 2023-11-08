# AuthWebViewsOidcTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**scope** | **str** |  | 

## Example

```python
from auth.models.auth_web_views_oidc_token_response import AuthWebViewsOidcTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthWebViewsOidcTokenResponse from a JSON string
auth_web_views_oidc_token_response_instance = AuthWebViewsOidcTokenResponse.from_json(json)
# print the JSON string representation of the object
print AuthWebViewsOidcTokenResponse.to_json()

# convert the object into a dict
auth_web_views_oidc_token_response_dict = auth_web_views_oidc_token_response_instance.to_dict()
# create an instance of AuthWebViewsOidcTokenResponse from a dict
auth_web_views_oidc_token_response_form_dict = auth_web_views_oidc_token_response.from_dict(auth_web_views_oidc_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


