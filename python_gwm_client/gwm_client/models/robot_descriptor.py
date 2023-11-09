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
from pydantic import BaseModel, Field, StrictStr, confloat, conint, constr, validator
from gwm_client.models.robot_descriptor_footprint import RobotDescriptorFootprint

class RobotDescriptor(BaseModel):
    """
    RobotDescriptor
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: constr(strict=True, max_length=100) = Field(..., description="Name of the robot")
    type: Optional[StrictStr] = Field(None, description="Type of robot  * `AMR` - Amr * `FORKLIFT` - Forklift")
    vendor: constr(strict=True, max_length=100) = Field(..., description="Name of system vendor")
    model: constr(strict=True, max_length=50) = Field(...)
    io_project_id: Optional[constr(strict=True, max_length=50)] = None
    labels: Dict[str, StrictStr] = Field(...)
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    footprint: Optional[RobotDescriptorFootprint] = None
    workflows: Optional[Dict[str, Any]] = None
    critical_battery_level: Optional[Union[confloat(le=100, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(None, description="Battery level under which a robot have to go to charge in %")
    chargeable_battery_level: Optional[Union[confloat(le=100, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(None, description="Battery level under which a robot can be sent to charge in %")
    minimum_charge_differential: Optional[Union[confloat(le=100, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(None, description="Minimum battery amount in % that robot needs to charge before stopping charging")
    minimum_fleet_availability: Optional[Union[confloat(le=100, ge=0, strict=True), conint(le=100, ge=0, strict=True)]] = Field(None, description="Robot fleet part that needs to be available at a given time in %")
    __properties = ["id", "name", "type", "vendor", "model", "io_project_id", "labels", "meta_data", "footprint", "workflows", "critical_battery_level", "chargeable_battery_level", "minimum_charge_differential", "minimum_fleet_availability"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AMR', 'FORKLIFT'):
            raise ValueError("must be one of enum values ('AMR', 'FORKLIFT')")
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
    def from_json(cls, json_str: str) -> RobotDescriptor:
        """Create an instance of RobotDescriptor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of footprint
        if self.footprint:
            _dict['footprint'] = self.footprint.to_dict()
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        # set to None if footprint (nullable) is None
        # and __fields_set__ contains the field
        if self.footprint is None and "footprint" in self.__fields_set__:
            _dict['footprint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RobotDescriptor:
        """Create an instance of RobotDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RobotDescriptor.parse_obj(obj)

        _obj = RobotDescriptor.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "vendor": obj.get("vendor"),
            "model": obj.get("model"),
            "io_project_id": obj.get("io_project_id"),
            "labels": obj.get("labels"),
            "meta_data": obj.get("meta_data"),
            "footprint": RobotDescriptorFootprint.from_dict(obj.get("footprint")) if obj.get("footprint") is not None else None,
            "workflows": obj.get("workflows"),
            "critical_battery_level": obj.get("critical_battery_level"),
            "chargeable_battery_level": obj.get("chargeable_battery_level"),
            "minimum_charge_differential": obj.get("minimum_charge_differential"),
            "minimum_fleet_availability": obj.get("minimum_fleet_availability")
        })
        return _obj


