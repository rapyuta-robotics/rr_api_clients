# coding: utf-8

"""
    IO-AMR GWM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: devel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from gwm_client.models.edge import Edge
from gwm_client.models.node_db_json import NodeDbJson

class DownloadGraphResponse(BaseModel):
    """
    DownloadGraphResponse
    """
    nodes: conlist(NodeDbJson) = Field(...)
    edges: conlist(Edge) = Field(...)
    __properties = ["nodes", "edges"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DownloadGraphResponse:
        """Create an instance of DownloadGraphResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item in self.nodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item in self.edges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloadGraphResponse:
        """Create an instance of DownloadGraphResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DownloadGraphResponse.parse_obj(obj)

        _obj = DownloadGraphResponse.parse_obj({
            "nodes": [NodeDbJson.from_dict(_item) for _item in obj.get("nodes")] if obj.get("nodes") is not None else None,
            "edges": [Edge.from_dict(_item) for _item in obj.get("edges")] if obj.get("edges") is not None else None
        })
        return _obj


