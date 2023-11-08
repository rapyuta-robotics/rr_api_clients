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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictInt, confloat, conint, conlist, constr

class ContainerDescriptorRequest(BaseModel):
    """
    ContainerDescriptorRequest
    """
    id: Optional[StrictInt] = None
    name: constr(strict=True, max_length=100, min_length=1) = Field(...)
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for objects of this type")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    type: Optional[constr(strict=True, max_length=50)] = Field(None, description="Type of the object")
    length: Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)] = Field(...)
    width: Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)] = Field(...)
    height: Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)] = Field(...)
    groups: Optional[conlist(constr(strict=True, max_length=64, min_length=1))] = None
    __properties = ["id", "name", "application_data", "meta_data", "type", "length", "width", "height", "groups"]

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
    def from_json(cls, json_str: str) -> ContainerDescriptorRequest:
        """Create an instance of ContainerDescriptorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if application_data (nullable) is None
        # and __fields_set__ contains the field
        if self.application_data is None and "application_data" in self.__fields_set__:
            _dict['application_data'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContainerDescriptorRequest:
        """Create an instance of ContainerDescriptorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContainerDescriptorRequest.parse_obj(obj)

        _obj = ContainerDescriptorRequest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "application_data": obj.get("application_data"),
            "meta_data": obj.get("meta_data"),
            "type": obj.get("type"),
            "length": obj.get("length"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "groups": obj.get("groups")
        })
        return _obj


