# DownloadGraphResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[NodeDbJson]**](NodeDbJson.md) |  | 
**edges** | [**List[Edge]**](Edge.md) |  | 

## Example

```python
from io_amr_gwm.models.download_graph_response import DownloadGraphResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadGraphResponse from a JSON string
download_graph_response_instance = DownloadGraphResponse.from_json(json)
# print the JSON string representation of the object
print DownloadGraphResponse.to_json()

# convert the object into a dict
download_graph_response_dict = download_graph_response_instance.to_dict()
# create an instance of DownloadGraphResponse from a dict
download_graph_response_form_dict = download_graph_response.from_dict(download_graph_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


