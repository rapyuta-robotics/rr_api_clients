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

from datetime import datetime

from pydantic import BaseModel, Field, StrictInt, StrictStr

class SiteStatus(BaseModel):
    """
    SiteStatus
    """
    error_type_version: StrictInt = Field(...)
    spot_version: StrictInt = Field(...)
    region_version: StrictInt = Field(...)
    robot_descriptor_version: StrictInt = Field(...)
    agent_version: StrictInt = Field(...)
    site_version: StrictInt = Field(...)
    id: StrictInt = Field(..., description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: StrictStr = Field(..., description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    created_at: datetime = Field(..., description="Timestamp at which this site was created")
    container_version: StrictInt = Field(...)
    container_descriptor_version: StrictInt = Field(...)
    product_version: StrictInt = Field(...)
    __properties = ["error_type_version", "spot_version", "region_version", "robot_descriptor_version", "agent_version", "site_version", "id", "name", "created_at", "container_version", "container_descriptor_version", "product_version"]

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
    def from_json(cls, json_str: str) -> SiteStatus:
        """Create an instance of SiteStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "error_type_version",
                            "spot_version",
                            "region_version",
                            "robot_descriptor_version",
                            "agent_version",
                            "site_version",
                            "id",
                            "name",
                            "created_at",
                            "container_version",
                            "container_descriptor_version",
                            "product_version",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SiteStatus:
        """Create an instance of SiteStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SiteStatus.parse_obj(obj)

        _obj = SiteStatus.parse_obj({
            "error_type_version": obj.get("error_type_version"),
            "spot_version": obj.get("spot_version"),
            "region_version": obj.get("region_version"),
            "robot_descriptor_version": obj.get("robot_descriptor_version"),
            "agent_version": obj.get("agent_version"),
            "site_version": obj.get("site_version"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "container_version": obj.get("container_version"),
            "container_descriptor_version": obj.get("container_descriptor_version"),
            "product_version": obj.get("product_version")
        })
        return _obj


