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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, conint, constr
from gwm_client.models.polygon_request import PolygonRequest

class RegionExportRequest(BaseModel):
    """
    RegionExportRequest
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    geom: PolygonRequest = Field(...)
    external_device: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    meta_data: Optional[Dict[str, Any]] = None
    type: Optional[constr(strict=True, max_length=50)] = Field(None, description="User defined type of polygon")
    __properties = ["id", "name", "geom", "external_device", "meta_data", "type"]

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
    def from_json(cls, json_str: str) -> RegionExportRequest:
        """Create an instance of RegionExportRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of geom
        if self.geom:
            _dict['geom'] = self.geom.to_dict()
        # set to None if external_device (nullable) is None
        # and __fields_set__ contains the field
        if self.external_device is None and "external_device" in self.__fields_set__:
            _dict['external_device'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegionExportRequest:
        """Create an instance of RegionExportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegionExportRequest.parse_obj(obj)

        _obj = RegionExportRequest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "geom": PolygonRequest.from_dict(obj.get("geom")) if obj.get("geom") is not None else None,
            "external_device": obj.get("external_device"),
            "meta_data": obj.get("meta_data"),
            "type": obj.get("type")
        })
        return _obj


