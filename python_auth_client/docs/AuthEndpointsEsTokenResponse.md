# AuthEndpointsEsTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**expires_in** | **float** |  | 

## Example

```python
from auth_client.models.auth_endpoints_es_token_response import AuthEndpointsEsTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthEndpointsEsTokenResponse from a JSON string
auth_endpoints_es_token_response_instance = AuthEndpointsEsTokenResponse.from_json(json)
# print the JSON string representation of the object
print AuthEndpointsEsTokenResponse.to_json()

# convert the object into a dict
auth_endpoints_es_token_response_dict = auth_endpoints_es_token_response_instance.to_dict()
# create an instance of AuthEndpointsEsTokenResponse from a dict
auth_endpoints_es_token_response_form_dict = auth_endpoints_es_token_response.from_dict(auth_endpoints_es_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


