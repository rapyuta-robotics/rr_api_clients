# Userinfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** |  | 
**preferred_username** | **str** |  | 
**name** | **str** |  | 
**group** | **str** |  | 
**group_name** | **str** |  | 
**expiry** | **str** |  | 
**scope** | **str** |  | 
**picture** | **str** |  | 

## Example

```python
from auth_client.models.userinfo import Userinfo

# TODO update the JSON string below
json = "{}"
# create an instance of Userinfo from a JSON string
userinfo_instance = Userinfo.from_json(json)
# print the JSON string representation of the object
print Userinfo.to_json()

# convert the object into a dict
userinfo_dict = userinfo_instance.to_dict()
# create an instance of Userinfo from a dict
userinfo_form_dict = userinfo.from_dict(userinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


