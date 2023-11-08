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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, constr, validator

class V3WorkFragmentBulkUpdateRequest(BaseModel):
    """
    V3WorkFragmentBulkUpdateRequest
    """
    id: StrictInt = Field(...)
    quantity_delivered: Optional[conint(strict=True, ge=0)] = None
    status: Optional[StrictStr] = Field(None, description="Status  * `NOT_STARTED` - Not Started * `IN_PROGRESS` - In Progress * `COMPLETED` - Completed * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `SKIPPED` - Skipped * `PARTIALLY_COMPLETED` - Partially Completed")
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for this object")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    rejection_reason: Optional[constr(strict=True, max_length=500)] = Field(None, description="Used as a rejection reason if the work payload fragment is rejected")
    __properties = ["id", "quantity_delivered", "status", "application_data", "meta_data", "rejection_reason"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED', 'REJECTED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'SKIPPED', 'PARTIALLY_COMPLETED'):
            raise ValueError("must be one of enum values ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED', 'REJECTED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'SKIPPED', 'PARTIALLY_COMPLETED')")
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
    def from_json(cls, json_str: str) -> V3WorkFragmentBulkUpdateRequest:
        """Create an instance of V3WorkFragmentBulkUpdateRequest from a JSON string"""
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

        # set to None if rejection_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.rejection_reason is None and "rejection_reason" in self.__fields_set__:
            _dict['rejection_reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V3WorkFragmentBulkUpdateRequest:
        """Create an instance of V3WorkFragmentBulkUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V3WorkFragmentBulkUpdateRequest.parse_obj(obj)

        _obj = V3WorkFragmentBulkUpdateRequest.parse_obj({
            "id": obj.get("id"),
            "quantity_delivered": obj.get("quantity_delivered"),
            "status": obj.get("status"),
            "application_data": obj.get("application_data"),
            "meta_data": obj.get("meta_data"),
            "rejection_reason": obj.get("rejection_reason")
        })
        return _obj


