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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, conint, constr

class MapGraphUpdate(BaseModel):
    """
    MapGraphUpdate
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    created_at: datetime = Field(..., description="Timestamp at which this map was created")
    floor: Optional[conint(strict=True, le=32767, ge=-32768)] = Field(None, description="Floor of the site this map corresponds to")
    graph_version: StrictInt = Field(..., description="System generated monotonic integer that is updated for each mutation to nodes or edges ")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    __properties = ["id", "name", "created_at", "floor", "graph_version", "meta_data"]

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
    def from_json(cls, json_str: str) -> MapGraphUpdate:
        """Create an instance of MapGraphUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "graph_version",
                          },
                          exclude_none=True)
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapGraphUpdate:
        """Create an instance of MapGraphUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapGraphUpdate.parse_obj(obj)

        _obj = MapGraphUpdate.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "floor": obj.get("floor"),
            "graph_version": obj.get("graph_version"),
            "meta_data": obj.get("meta_data")
        })
        return _obj


