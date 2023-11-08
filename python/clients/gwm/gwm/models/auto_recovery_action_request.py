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
from pydantic import BaseModel, Field, StrictInt, confloat, conint

class AutoRecoveryActionRequest(BaseModel):
    """
    AutoRecoveryActionRequest
    """
    action: StrictInt = Field(..., description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    content: Dict[str, Any] = Field(..., description="Information to fill in that should match the schema of the recovery action")
    first_attempt_after: Union[confloat(ge=0.0, strict=True), conint(ge=0, strict=True)] = Field(..., description="Amount of time before making the first attempt")
    retry_interval: Union[confloat(ge=0.0, strict=True), conint(ge=0, strict=True)] = Field(..., description="Amount of time between subsequent attempts")
    max_attempts: Optional[conint(strict=True, le=32767, ge=0)] = Field(None, description="Number of times to retry the specific action")
    __properties = ["action", "content", "first_attempt_after", "retry_interval", "max_attempts"]

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
    def from_json(cls, json_str: str) -> AutoRecoveryActionRequest:
        """Create an instance of AutoRecoveryActionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutoRecoveryActionRequest:
        """Create an instance of AutoRecoveryActionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutoRecoveryActionRequest.parse_obj(obj)

        _obj = AutoRecoveryActionRequest.parse_obj({
            "action": obj.get("action"),
            "content": obj.get("content"),
            "first_attempt_after": obj.get("first_attempt_after"),
            "retry_interval": obj.get("retry_interval"),
            "max_attempts": obj.get("max_attempts")
        })
        return _obj


