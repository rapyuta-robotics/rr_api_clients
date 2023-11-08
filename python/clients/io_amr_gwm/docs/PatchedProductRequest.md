# PatchedProductRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**product_id** | **str** | Identification key for the product. | [optional] 
**name** | **str** | Name for the product | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.patched_product_request import PatchedProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProductRequest from a JSON string
patched_product_request_instance = PatchedProductRequest.from_json(json)
# print the JSON string representation of the object
print PatchedProductRequest.to_json()

# convert the object into a dict
patched_product_request_dict = patched_product_request_instance.to_dict()
# create an instance of PatchedProductRequest from a dict
patched_product_request_form_dict = patched_product_request.from_dict(patched_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


