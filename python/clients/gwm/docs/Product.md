# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**meta_data** | **Dict[str, object]** | optional JSON encoded metadata for this object | [optional] 
**product_id** | **str** | Identification key for the product. | 
**name** | **str** | Name for the product | 
**image_url** | **str** |  | [optional] 

## Example

```python
from gwm.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


