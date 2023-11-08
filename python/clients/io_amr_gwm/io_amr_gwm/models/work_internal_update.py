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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from io_amr_gwm.models.work_payload_fragment import WorkPayloadFragment

class WorkInternalUpdate(BaseModel):
    """
    WorkInternalUpdate
    """
    status: Optional[StrictStr] = Field(None, description="Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed")
    rejection_reason: Optional[constr(strict=True, max_length=500)] = Field(None, description="Used as a rejection reason if the work is rejected")
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for this object")
    fragments: Optional[conlist(WorkPayloadFragment)] = None
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    __properties = ["status", "rejection_reason", "application_data", "fragments", "meta_data"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ON_HOLD', 'NEW', 'LIVE', 'IN_PROGRESS', 'REJECTED', 'CANCELLED', 'COMPLETED', 'TERMINAL_WITH_EXCEPTION', 'ABORTED', 'PARTIALLY_COMPLETED'):
            raise ValueError("must be one of enum values ('ON_HOLD', 'NEW', 'LIVE', 'IN_PROGRESS', 'REJECTED', 'CANCELLED', 'COMPLETED', 'TERMINAL_WITH_EXCEPTION', 'ABORTED', 'PARTIALLY_COMPLETED')")
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
    def from_json(cls, json_str: str) -> WorkInternalUpdate:
        """Create an instance of WorkInternalUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fragments (list)
        _items = []
        if self.fragments:
            for _item in self.fragments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fragments'] = _items
        # set to None if rejection_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.rejection_reason is None and "rejection_reason" in self.__fields_set__:
            _dict['rejection_reason'] = None

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
    def from_dict(cls, obj: dict) -> WorkInternalUpdate:
        """Create an instance of WorkInternalUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkInternalUpdate.parse_obj(obj)

        _obj = WorkInternalUpdate.parse_obj({
            "status": obj.get("status"),
            "rejection_reason": obj.get("rejection_reason"),
            "application_data": obj.get("application_data"),
            "fragments": [WorkPayloadFragment.from_dict(_item) for _item in obj.get("fragments")] if obj.get("fragments") is not None else None,
            "meta_data": obj.get("meta_data")
        })
        return _obj


