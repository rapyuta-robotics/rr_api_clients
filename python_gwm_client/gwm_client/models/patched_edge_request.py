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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictInt, confloat, conint

class PatchedEdgeRequest(BaseModel):
    """
    PatchedEdgeRequest
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    directed: Optional[StrictBool] = Field(False, description="If True, edge direction is from node1 to node2")
    node1: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    node2: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    speed_scale_estimate: Optional[Union[confloat(le=1.0, ge=0.01, strict=True), conint(le=1, ge=1, strict=True)]] = None
    preserve: Optional[StrictBool] = Field(None, description="If True, edge is excluded from deletion, unless deleted by force")
    __properties = ["id", "directed", "node1", "node2", "meta_data", "speed_scale_estimate", "preserve"]

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
    def from_json(cls, json_str: str) -> PatchedEdgeRequest:
        """Create an instance of PatchedEdgeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedEdgeRequest:
        """Create an instance of PatchedEdgeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedEdgeRequest.parse_obj(obj)

        _obj = PatchedEdgeRequest.parse_obj({
            "id": obj.get("id"),
            "directed": obj.get("directed") if obj.get("directed") is not None else False,
            "node1": obj.get("node1"),
            "node2": obj.get("node2"),
            "meta_data": obj.get("meta_data"),
            "speed_scale_estimate": obj.get("speed_scale_estimate"),
            "preserve": obj.get("preserve")
        })
        return _obj


