# AccessTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expiry** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from auth.models.access_token_response import AccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenResponse from a JSON string
access_token_response_instance = AccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print AccessTokenResponse.to_json()

# convert the object into a dict
access_token_response_dict = access_token_response_instance.to_dict()
# create an instance of AccessTokenResponse from a dict
access_token_response_form_dict = access_token_response.from_dict(access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


