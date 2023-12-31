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
from gwm_client.models.location import Location

class InlineAgentTaskFragment(BaseModel):
    """
    InlineAgentTaskFragment
    """
    work_fragment: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    id: Optional[StrictInt] = None
    status: Optional[StrictStr] = Field(None, description="Current status of the agent task  * `NOT_STARTED` - Not Started * `ASSIGNED` - Assigned * `PREPARING_TO_PICK` - Preparing To Pick * `PICKING` - Picking * `PICKED` - Picked * `PREPARING_TO_DROP` - Preparing To Drop * `DROPPING` - Dropping * `PREPARING_ACTION` - Preparing Action * `ACTION_IN_PROGRESS` - Action In Progress * `COMPLETED` - Completed * `CANCELLED` - Cancelled * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `SKIPPED` - Skipped")
    type: Optional[StrictStr] = Field(None, description="Payload move type  * `ITEM_MOVE` - Item Move * `CONTAINER_MOVE` - Container Move * `ACTION` - Action")
    quantity_requested: Optional[conint(strict=True, le=2147483647, ge=0)] = Field(None, description="Quantity requested to deliver for this task fragment")
    quantity_delivered: Optional[conint(strict=True, le=2147483647, ge=0)] = Field(None, description="Quantity delivered to destination")
    quantity_picked: Optional[conint(strict=True, le=2147483647, ge=0)] = Field(None, description="Quantity picked")
    payload_data: Optional[Dict[str, Any]] = Field(None, description="meta_data generated by work splitter to pass to Pick/Drop/RecognizePayload actions")
    detection_data: Optional[Dict[str, Any]] = Field(None, description="Info recorded if RecognizePayload action is called")
    action_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded action metadata")
    pick_data: Optional[Dict[str, Any]] = Field(None, description="Info recorded when picking from PickDrop server")
    drop_data: Optional[Dict[str, Any]] = Field(None, description="Info recorded when dropping from PickDrop server")
    from_location: Optional[Dict[str, Any]] = Field(None, description="From location")
    to_location: Optional[Dict[str, Any]] = Field(None, description="To location")
    action_location: Optional[Location] = None
    name: Optional[constr(strict=True, max_length=50)] = Field(None, description="Fragment name")
    workflow: Optional[constr(strict=True, max_length=32)] = Field(None, description="Examples: replenishment, transport")
    __properties = ["work_fragment", "id", "status", "type", "quantity_requested", "quantity_delivered", "quantity_picked", "payload_data", "detection_data", "action_data", "pick_data", "drop_data", "from_location", "to_location", "action_location", "name", "workflow"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NOT_STARTED', 'ASSIGNED', 'PREPARING_TO_PICK', 'PICKING', 'PICKED', 'PREPARING_TO_DROP', 'DROPPING', 'PREPARING_ACTION', 'ACTION_IN_PROGRESS', 'COMPLETED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'SKIPPED'):
            raise ValueError("must be one of enum values ('NOT_STARTED', 'ASSIGNED', 'PREPARING_TO_PICK', 'PICKING', 'PICKED', 'PREPARING_TO_DROP', 'DROPPING', 'PREPARING_ACTION', 'ACTION_IN_PROGRESS', 'COMPLETED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'SKIPPED')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ITEM_MOVE', 'CONTAINER_MOVE', 'ACTION'):
            raise ValueError("must be one of enum values ('ITEM_MOVE', 'CONTAINER_MOVE', 'ACTION')")
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
    def from_json(cls, json_str: str) -> InlineAgentTaskFragment:
        """Create an instance of InlineAgentTaskFragment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action_location
        if self.action_location:
            _dict['action_location'] = self.action_location.to_dict()
        # set to None if work_fragment (nullable) is None
        # and __fields_set__ contains the field
        if self.work_fragment is None and "work_fragment" in self.__fields_set__:
            _dict['work_fragment'] = None

        # set to None if payload_data (nullable) is None
        # and __fields_set__ contains the field
        if self.payload_data is None and "payload_data" in self.__fields_set__:
            _dict['payload_data'] = None

        # set to None if detection_data (nullable) is None
        # and __fields_set__ contains the field
        if self.detection_data is None and "detection_data" in self.__fields_set__:
            _dict['detection_data'] = None

        # set to None if action_data (nullable) is None
        # and __fields_set__ contains the field
        if self.action_data is None and "action_data" in self.__fields_set__:
            _dict['action_data'] = None

        # set to None if pick_data (nullable) is None
        # and __fields_set__ contains the field
        if self.pick_data is None and "pick_data" in self.__fields_set__:
            _dict['pick_data'] = None

        # set to None if drop_data (nullable) is None
        # and __fields_set__ contains the field
        if self.drop_data is None and "drop_data" in self.__fields_set__:
            _dict['drop_data'] = None

        # set to None if from_location (nullable) is None
        # and __fields_set__ contains the field
        if self.from_location is None and "from_location" in self.__fields_set__:
            _dict['from_location'] = None

        # set to None if to_location (nullable) is None
        # and __fields_set__ contains the field
        if self.to_location is None and "to_location" in self.__fields_set__:
            _dict['to_location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InlineAgentTaskFragment:
        """Create an instance of InlineAgentTaskFragment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InlineAgentTaskFragment.parse_obj(obj)

        _obj = InlineAgentTaskFragment.parse_obj({
            "work_fragment": obj.get("work_fragment"),
            "id": obj.get("id"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "quantity_requested": obj.get("quantity_requested"),
            "quantity_delivered": obj.get("quantity_delivered"),
            "quantity_picked": obj.get("quantity_picked"),
            "payload_data": obj.get("payload_data"),
            "detection_data": obj.get("detection_data"),
            "action_data": obj.get("action_data"),
            "pick_data": obj.get("pick_data"),
            "drop_data": obj.get("drop_data"),
            "from_location": obj.get("from_location"),
            "to_location": obj.get("to_location"),
            "action_location": Location.from_dict(obj.get("action_location")) if obj.get("action_location") is not None else None,
            "name": obj.get("name"),
            "workflow": obj.get("workflow")
        })
        return _obj


