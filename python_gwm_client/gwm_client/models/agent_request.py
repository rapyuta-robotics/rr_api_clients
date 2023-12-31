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
from pydantic import BaseModel, Field, StrictStr, conint, constr, validator

class AgentRequest(BaseModel):
    """
    AgentRequest
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    robot_id: conint(strict=True, le=2147483647, ge=0) = Field(...)
    robot_descriptor_id: conint(strict=True, le=2147483647, ge=0) = Field(...)
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    mode: Optional[StrictStr] = Field(None, description="* `Manual` - Manual * `Automatic` - Automatic * `Offline` - Offline * `Paused` - Paused * `Emergency Stop` - Emergency Stop")
    assigned_workflow: Optional[constr(strict=True, max_length=32)] = None
    __properties = ["id", "name", "robot_id", "robot_descriptor_id", "meta_data", "mode", "assigned_workflow"]

    @validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Manual', 'Automatic', 'Offline', 'Paused', 'Emergency Stop'):
            raise ValueError("must be one of enum values ('Manual', 'Automatic', 'Offline', 'Paused', 'Emergency Stop')")
        return value

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
    def from_json(cls, json_str: str) -> AgentRequest:
        """Create an instance of AgentRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AgentRequest:
        """Create an instance of AgentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AgentRequest.parse_obj(obj)

        _obj = AgentRequest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "robot_id": obj.get("robot_id"),
            "robot_descriptor_id": obj.get("robot_descriptor_id"),
            "meta_data": obj.get("meta_data"),
            "mode": obj.get("mode"),
            "assigned_workflow": obj.get("assigned_workflow")
        })
        return _obj


