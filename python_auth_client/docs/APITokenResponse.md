# APITokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**token** | **str** |  | 
**scope** | **List[str]** |  | 

## Example

```python
from auth_client.models.api_token_response import APITokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APITokenResponse from a JSON string
api_token_response_instance = APITokenResponse.from_json(json)
# print the JSON string representation of the object
print APITokenResponse.to_json()

# convert the object into a dict
api_token_response_dict = api_token_response_instance.to_dict()
# create an instance of APITokenResponse from a dict
api_token_response_form_dict = api_token_response.from_dict(api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


