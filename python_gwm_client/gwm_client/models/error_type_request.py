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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conint, conlist, constr, validator
from gwm_client.models.auto_recovery_action_request import AutoRecoveryActionRequest

class ErrorTypeRequest(BaseModel):
    """
    ErrorTypeRequest
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: constr(strict=True, max_length=100) = Field(..., description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    local_error_code: conint(strict=True, le=32767, ge=0) = Field(..., description="This is the internal error code that io amr uses ; each corresponds to a specific failure condition")
    reporting_component: constr(strict=True, min_length=1) = Field(..., description="This is the reporting_component of the error")
    global_error_code: Optional[conint(strict=True, le=32767, ge=0)] = Field(None, description="This is the global error code that the customer assigns ")
    criticality: Optional[conint(strict=True, le=32767, ge=0)] = Field(None, description="Severity of the error  * `1` - Warning * `2` - Error * `3` - Ignore")
    clearing_options: Optional[conlist(Any)] = None
    auto_recovery_actions: Optional[conlist(AutoRecoveryActionRequest)] = None
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    __properties = ["id", "name", "local_error_code", "reporting_component", "global_error_code", "criticality", "clearing_options", "auto_recovery_actions", "meta_data"]

    @validator('criticality')
    def criticality_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (1, 2, 3):
            raise ValueError("must be one of enum values (1, 2, 3)")
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
    def from_json(cls, json_str: str) -> ErrorTypeRequest:
        """Create an instance of ErrorTypeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in auto_recovery_actions (list)
        _items = []
        if self.auto_recovery_actions:
            for _item in self.auto_recovery_actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['auto_recovery_actions'] = _items
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorTypeRequest:
        """Create an instance of ErrorTypeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorTypeRequest.parse_obj(obj)

        _obj = ErrorTypeRequest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "local_error_code": obj.get("local_error_code"),
            "reporting_component": obj.get("reporting_component"),
            "global_error_code": obj.get("global_error_code"),
            "criticality": obj.get("criticality"),
            "clearing_options": obj.get("clearing_options"),
            "auto_recovery_actions": [AutoRecoveryActionRequest.from_dict(_item) for _item in obj.get("auto_recovery_actions")] if obj.get("auto_recovery_actions") is not None else None,
            "meta_data": obj.get("meta_data")
        })
        return _obj


