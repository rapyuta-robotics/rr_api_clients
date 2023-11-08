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

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conint, conlist, constr, validator
from openapi_client.models.agent_task import AgentTask
from openapi_client.models.internal_work_payload_fragment_to_pos import InternalWorkPayloadFragmentToPos
from openapi_client.models.work_payload_fragment import WorkPayloadFragment

class Work(BaseModel):
    """
    Work
    """
    id: StrictInt = Field(...)
    name: Optional[constr(strict=True, max_length=50)] = Field(None, description="user provided name eg: `mywarehouse_move_2021-05-11T12:05:27Z`")
    created_at: datetime = Field(..., description="timestamp of creation")
    activated_at: Optional[datetime] = Field(..., description="Time of activation(ON_HOLD -> NEW)")
    priority: Optional[conint(strict=True, le=50, ge=0)] = Field(None, description="Priority of the work")
    type: StrictStr = Field(..., description="Type of the work  * `CHARGE` - Charge * `EXPLORE` - Explore * `PAYLOAD_MOVE` - Payload Move * `ADHOC_MOVE_POSITION` - Adhoc Move Position * `ADHOC_MOVE_REGION` - Adhoc Move Region * `ADHOC_MOVE_SPOT` - Adhoc Move Spot")
    status: Optional[StrictStr] = Field(None, description="Current status of the Work, this is set by the system via internal API  * `ON_HOLD` - On Hold * `NEW` - New * `LIVE` - Live * `IN_PROGRESS` - In Progress * `REJECTED` - Rejected * `CANCELLED` - Cancelled * `COMPLETED` - Completed * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted * `PARTIALLY_COMPLETED` - Partially Completed")
    cut_off_time: Optional[datetime] = Field(None, description="Cut off time of the work")
    rejection_reason: Optional[StrictStr] = Field(..., description="Used as a rejection reason if the work is rejected")
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for this object")
    workflow: Optional[constr(strict=True, max_length=32)] = Field(None, description="Examples: replenishment, transport")
    batch: Optional[constr(strict=True, max_length=64)] = None
    assigned_agent: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    spot: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    pos: Optional[InternalWorkPayloadFragmentToPos] = None
    yaw: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Desired orientation in radians of the agent")
    map: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    fragments: Optional[conlist(WorkPayloadFragment)] = None
    agent_tasks: conlist(AgentTask) = Field(...)
    region: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    __properties = ["id", "name", "created_at", "activated_at", "priority", "type", "status", "cut_off_time", "rejection_reason", "application_data", "workflow", "batch", "assigned_agent", "spot", "pos", "yaw", "map", "fragments", "agent_tasks", "region", "meta_data"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CHARGE', 'EXPLORE', 'PAYLOAD_MOVE', 'ADHOC_MOVE_POSITION', 'ADHOC_MOVE_REGION', 'ADHOC_MOVE_SPOT'):
            raise ValueError("must be one of enum values ('CHARGE', 'EXPLORE', 'PAYLOAD_MOVE', 'ADHOC_MOVE_POSITION', 'ADHOC_MOVE_REGION', 'ADHOC_MOVE_SPOT')")
        return value

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
    def from_json(cls, json_str: str) -> Work:
        """Create an instance of Work from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "activated_at",
                            "rejection_reason",
                            "agent_tasks",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pos
        if self.pos:
            _dict['pos'] = self.pos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fragments (list)
        _items = []
        if self.fragments:
            for _item in self.fragments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fragments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in agent_tasks (list)
        _items = []
        if self.agent_tasks:
            for _item in self.agent_tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agent_tasks'] = _items
        # set to None if activated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.activated_at is None and "activated_at" in self.__fields_set__:
            _dict['activated_at'] = None

        # set to None if cut_off_time (nullable) is None
        # and __fields_set__ contains the field
        if self.cut_off_time is None and "cut_off_time" in self.__fields_set__:
            _dict['cut_off_time'] = None

        # set to None if rejection_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.rejection_reason is None and "rejection_reason" in self.__fields_set__:
            _dict['rejection_reason'] = None

        # set to None if application_data (nullable) is None
        # and __fields_set__ contains the field
        if self.application_data is None and "application_data" in self.__fields_set__:
            _dict['application_data'] = None

        # set to None if pos (nullable) is None
        # and __fields_set__ contains the field
        if self.pos is None and "pos" in self.__fields_set__:
            _dict['pos'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Work:
        """Create an instance of Work from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Work.parse_obj(obj)

        _obj = Work.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "activated_at": obj.get("activated_at"),
            "priority": obj.get("priority"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "cut_off_time": obj.get("cut_off_time"),
            "rejection_reason": obj.get("rejection_reason"),
            "application_data": obj.get("application_data"),
            "workflow": obj.get("workflow"),
            "batch": obj.get("batch"),
            "assigned_agent": obj.get("assigned_agent"),
            "spot": obj.get("spot"),
            "pos": InternalWorkPayloadFragmentToPos.from_dict(obj.get("pos")) if obj.get("pos") is not None else None,
            "yaw": obj.get("yaw"),
            "map": obj.get("map"),
            "fragments": [WorkPayloadFragment.from_dict(_item) for _item in obj.get("fragments")] if obj.get("fragments") is not None else None,
            "agent_tasks": [AgentTask.from_dict(_item) for _item in obj.get("agent_tasks")] if obj.get("agent_tasks") is not None else None,
            "region": obj.get("region"),
            "meta_data": obj.get("meta_data")
        })
        return _obj


