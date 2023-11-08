# ModelSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | user defined &#x60;id&#x60; of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer | [optional] 
**name** | **str** | user defined &#x60;name&#x60; of this object. Must be unique in the site or map (for nodes and edges) | [optional] 
**type** | **str** | Type of the object (if its a spot, what kind of spot) | [optional] 
**resource** | **str** | Which resource applies this schema (node, edge)  * &#x60;site&#x60; - Site * &#x60;spotannotation&#x60; - Spot * &#x60;region&#x60; - Region * &#x60;node&#x60; - Node * &#x60;edge&#x60; - Edge * &#x60;map&#x60; - Map * &#x60;robot&#x60; - Robot * &#x60;robotdescriptor&#x60; - Robot Descriptor * &#x60;agent&#x60; - Agent * &#x60;externaldevice&#x60; - External Device * &#x60;errortype&#x60; - Error Type * &#x60;erroraction&#x60; - Error Action * &#x60;work&#x60; - Work * &#x60;workpayloadfragment&#x60; - Work Payload Fragment * &#x60;layer&#x60; - Layer * &#x60;agenttask&#x60; - Agent Task * &#x60;agenttaskfragment&#x60; - Agent Task Fragment * &#x60;container&#x60; - Container * &#x60;containerdescriptor&#x60; - Container Descriptor * &#x60;assetlocation&#x60; - Asset Location | 
**var_schema** | **Dict[str, object]** | Schema description for the meta_data using (http://json-schema.org/learn/getting-started-step-by-step) | 
**field_name** | **str** | The field on the given resource that this schema applies to (default: &#39;meta_data&#39;). | [optional] 
**workflow** | **str** | Workflow of the object(only for models that have workflow) | [optional] 
**application_data** | **Dict[str, object]** | JSON encoded application data for objects of this type | [optional] 

## Example

```python
from openapi_client.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print ModelSchema.to_json()

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_form_dict = model_schema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


