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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator

class WorkflowExecutionBulkUpdateSerializerV1Request(BaseModel):
    """
    WorkflowExecutionBulkUpdateSerializerV1Request
    """
    id: Optional[StrictStr] = None
    status: Optional[StrictStr] = Field(None, description="Status of the workflow execution.  * `PENDING` - Pending * `RUNNING` - Running * `COMPLETED` - Completed * `FAILED` - Failed * `CANCELED` - Canceled * `TERMINATED` - Terminated * `CONTINUED_AS_NEW` - Continued as new * `TIMED_OUT` - Timed out")
    result: Optional[Dict[str, Any]] = Field(None, description="The workflow execution result.")
    context: Optional[Dict[str, Any]] = Field(None, description="The workflow execution context.")
    __properties = ["id", "status", "result", "context"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PENDING', 'RUNNING', 'COMPLETED', 'FAILED', 'CANCELED', 'TERMINATED', 'CONTINUED_AS_NEW', 'TIMED_OUT'):
            raise ValueError("must be one of enum values ('PENDING', 'RUNNING', 'COMPLETED', 'FAILED', 'CANCELED', 'TERMINATED', 'CONTINUED_AS_NEW', 'TIMED_OUT')")
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
    def from_json(cls, json_str: str) -> WorkflowExecutionBulkUpdateSerializerV1Request:
        """Create an instance of WorkflowExecutionBulkUpdateSerializerV1Request from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowExecutionBulkUpdateSerializerV1Request:
        """Create an instance of WorkflowExecutionBulkUpdateSerializerV1Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowExecutionBulkUpdateSerializerV1Request.parse_obj(obj)

        _obj = WorkflowExecutionBulkUpdateSerializerV1Request.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "result": obj.get("result"),
            "context": obj.get("context")
        })
        return _obj


