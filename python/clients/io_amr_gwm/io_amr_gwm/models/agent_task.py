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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist, constr, validator
from io_amr_gwm.models.inline_agent_task_fragment import InlineAgentTaskFragment

class AgentTask(BaseModel):
    """
    AgentTask
    """
    agent: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    required_agent: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    work: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    id: Optional[StrictInt] = None
    status: Optional[StrictStr] = Field(None, description="Current status of the agent task  * `NOT_STARTED` - Not Started * `IN_PROGRESS` - In Progress * `COMPLETED` - Completed * `CANCELLED` - Cancelled * `TERMINAL_WITH_EXCEPTION` - Terminal With Exception * `ABORTED` - Aborted")
    type: Optional[StrictStr] = Field(None, description="Agent task type  * `ADHOC_MOVE` - Adhoc Move * `CHARGE` - Charge * `EXPLORE` - Explore * `PAYLOAD_MOVE` - Payload Move * `DYNAMIC_PAYLOAD_MOVE` - Dynamic Payload Move")
    assignment_data: Optional[Dict[str, Any]] = Field(None, description="Data set by the task assigner.  For example, the location on the robot corresponding to the task")
    action_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded action metadata")
    split_data: Optional[Dict[str, Any]] = Field(None, description="Data set by work splitter for the sake of task assignment")
    task_fragments: conlist(InlineAgentTaskFragment) = Field(...)
    workflow: Optional[constr(strict=True, max_length=32)] = Field(None, description="Examples: replenishment, transport")
    priority: Optional[conint(strict=True, le=50, ge=0)] = Field(None, description="Priority of the task")
    location: Optional[Dict[str, Any]] = None
    work_created_at: datetime = Field(..., description="timestamp of creation")
    work_cut_off_time: Optional[datetime] = Field(..., description="Cut off time of the work")
    __properties = ["agent", "required_agent", "work", "id", "status", "type", "assignment_data", "action_data", "split_data", "task_fragments", "workflow", "priority", "location", "work_created_at", "work_cut_off_time"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'ABORTED'):
            raise ValueError("must be one of enum values ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', 'TERMINAL_WITH_EXCEPTION', 'ABORTED')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ADHOC_MOVE', 'CHARGE', 'EXPLORE', 'PAYLOAD_MOVE', 'DYNAMIC_PAYLOAD_MOVE'):
            raise ValueError("must be one of enum values ('ADHOC_MOVE', 'CHARGE', 'EXPLORE', 'PAYLOAD_MOVE', 'DYNAMIC_PAYLOAD_MOVE')")
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
    def from_json(cls, json_str: str) -> AgentTask:
        """Create an instance of AgentTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "task_fragments",
                            "work_created_at",
                            "work_cut_off_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in task_fragments (list)
        _items = []
        if self.task_fragments:
            for _item in self.task_fragments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['task_fragments'] = _items
        # set to None if agent (nullable) is None
        # and __fields_set__ contains the field
        if self.agent is None and "agent" in self.__fields_set__:
            _dict['agent'] = None

        # set to None if required_agent (nullable) is None
        # and __fields_set__ contains the field
        if self.required_agent is None and "required_agent" in self.__fields_set__:
            _dict['required_agent'] = None

        # set to None if work (nullable) is None
        # and __fields_set__ contains the field
        if self.work is None and "work" in self.__fields_set__:
            _dict['work'] = None

        # set to None if assignment_data (nullable) is None
        # and __fields_set__ contains the field
        if self.assignment_data is None and "assignment_data" in self.__fields_set__:
            _dict['assignment_data'] = None

        # set to None if action_data (nullable) is None
        # and __fields_set__ contains the field
        if self.action_data is None and "action_data" in self.__fields_set__:
            _dict['action_data'] = None

        # set to None if split_data (nullable) is None
        # and __fields_set__ contains the field
        if self.split_data is None and "split_data" in self.__fields_set__:
            _dict['split_data'] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict['location'] = None

        # set to None if work_cut_off_time (nullable) is None
        # and __fields_set__ contains the field
        if self.work_cut_off_time is None and "work_cut_off_time" in self.__fields_set__:
            _dict['work_cut_off_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AgentTask:
        """Create an instance of AgentTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AgentTask.parse_obj(obj)

        _obj = AgentTask.parse_obj({
            "agent": obj.get("agent"),
            "required_agent": obj.get("required_agent"),
            "work": obj.get("work"),
            "id": obj.get("id"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "assignment_data": obj.get("assignment_data"),
            "action_data": obj.get("action_data"),
            "split_data": obj.get("split_data"),
            "task_fragments": [InlineAgentTaskFragment.from_dict(_item) for _item in obj.get("task_fragments")] if obj.get("task_fragments") is not None else None,
            "workflow": obj.get("workflow"),
            "priority": obj.get("priority"),
            "location": obj.get("location"),
            "work_created_at": obj.get("work_created_at"),
            "work_cut_off_time": obj.get("work_cut_off_time")
        })
        return _obj


