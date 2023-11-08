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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conint, constr, validator
from io_amr_gwm.models.internal_work_payload_fragment_request_to_pos import InternalWorkPayloadFragmentRequestToPos

class InternalWorkPayloadFragmentRequest(BaseModel):
    """
    InternalWorkPayloadFragmentRequest
    """
    status: Optional[StrictStr] = Field(None, description="Status  * `NOT_STARTED` - Not Started * `IN_PROGRESS` - In Progress * `COMPLETED` - Completed * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `SKIPPED` - Skipped * `PARTIALLY_COMPLETED` - Partially Completed")
    rejection_reason: Optional[constr(strict=True, max_length=500)] = Field(None, description="Used as a rejection reason if the work payload fragment is rejected")
    to_spot: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    to_region: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    to_pos: Optional[InternalWorkPayloadFragmentRequestToPos] = None
    to_yaw: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Desired orientation in radians of the agent")
    to_map: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    name: Optional[constr(strict=True, max_length=255, min_length=1)] = Field(None, description="Name")
    quantity_delivered: Optional[conint(strict=True, le=2147483647, ge=0)] = Field(None, description="How much was actually delivered to the customer")
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for this object")
    quantity_requested: Optional[conint(strict=True, le=2147483647, ge=0)] = Field(None, description="How many was requested by the order")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    __properties = ["status", "rejection_reason", "to_spot", "to_region", "to_pos", "to_yaw", "to_map", "name", "quantity_delivered", "application_data", "quantity_requested", "meta_data"]

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
    def from_json(cls, json_str: str) -> InternalWorkPayloadFragmentRequest:
        """Create an instance of InternalWorkPayloadFragmentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of to_pos
        if self.to_pos:
            _dict['to_pos'] = self.to_pos.to_dict()
        # set to None if rejection_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.rejection_reason is None and "rejection_reason" in self.__fields_set__:
            _dict['rejection_reason'] = None

        # set to None if to_spot (nullable) is None
        # and __fields_set__ contains the field
        if self.to_spot is None and "to_spot" in self.__fields_set__:
            _dict['to_spot'] = None

        # set to None if to_region (nullable) is None
        # and __fields_set__ contains the field
        if self.to_region is None and "to_region" in self.__fields_set__:
            _dict['to_region'] = None

        # set to None if to_pos (nullable) is None
        # and __fields_set__ contains the field
        if self.to_pos is None and "to_pos" in self.__fields_set__:
            _dict['to_pos'] = None

        # set to None if to_yaw (nullable) is None
        # and __fields_set__ contains the field
        if self.to_yaw is None and "to_yaw" in self.__fields_set__:
            _dict['to_yaw'] = None

        # set to None if to_map (nullable) is None
        # and __fields_set__ contains the field
        if self.to_map is None and "to_map" in self.__fields_set__:
            _dict['to_map'] = None

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
    def from_dict(cls, obj: dict) -> InternalWorkPayloadFragmentRequest:
        """Create an instance of InternalWorkPayloadFragmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InternalWorkPayloadFragmentRequest.parse_obj(obj)

        _obj = InternalWorkPayloadFragmentRequest.parse_obj({
            "status": obj.get("status"),
            "rejection_reason": obj.get("rejection_reason"),
            "to_spot": obj.get("to_spot"),
            "to_region": obj.get("to_region"),
            "to_pos": InternalWorkPayloadFragmentRequestToPos.from_dict(obj.get("to_pos")) if obj.get("to_pos") is not None else None,
            "to_yaw": obj.get("to_yaw"),
            "to_map": obj.get("to_map"),
            "name": obj.get("name"),
            "quantity_delivered": obj.get("quantity_delivered"),
            "application_data": obj.get("application_data"),
            "quantity_requested": obj.get("quantity_requested"),
            "meta_data": obj.get("meta_data")
        })
        return _obj


