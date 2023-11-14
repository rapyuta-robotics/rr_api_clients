# coding: utf-8

"""
    IO-AMR GWM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: api-client-testing
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, conint, constr

class SiteExport(BaseModel):
    """
    SiteExport
    """
    endpoint: StrictStr = Field(...)
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    type: Optional[constr(strict=True, max_length=50)] = Field(None, description="type fo site (e.g. warehouse)")
    __properties = ["endpoint", "id", "meta_data", "name", "type"]

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
    def from_json(cls, json_str: str) -> SiteExport:
        """Create an instance of SiteExport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "endpoint",
                          },
                          exclude_none=True)
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SiteExport:
        """Create an instance of SiteExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SiteExport.parse_obj(obj)

        _obj = SiteExport.parse_obj({
            "endpoint": obj.get("endpoint"),
            "id": obj.get("id"),
            "meta_data": obj.get("meta_data"),
            "name": obj.get("name"),
            "type": obj.get("type")
        })
        return _obj


