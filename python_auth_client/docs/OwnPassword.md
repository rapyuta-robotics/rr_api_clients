# OwnPassword


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from auth_client.models.own_password import OwnPassword

# TODO update the JSON string below
json = "{}"
# create an instance of OwnPassword from a JSON string
own_password_instance = OwnPassword.from_json(json)
# print the JSON string representation of the object
print OwnPassword.to_json()

# convert the object into a dict
own_password_dict = own_password_instance.to_dict()
# create an instance of OwnPassword from a dict
own_password_form_dict = own_password.from_dict(own_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


