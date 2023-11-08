# LayerImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file | [optional] 

## Example

```python
from openapi_client.models.layer_image import LayerImage

# TODO update the JSON string below
json = "{}"
# create an instance of LayerImage from a JSON string
layer_image_instance = LayerImage.from_json(json)
# print the JSON string representation of the object
print LayerImage.to_json()

# convert the object into a dict
layer_image_dict = layer_image_instance.to_dict()
# create an instance of LayerImage from a dict
layer_image_form_dict = layer_image.from_dict(layer_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


