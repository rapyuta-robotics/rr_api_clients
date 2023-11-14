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


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from gwm_client.models.v3_work import V3Work

class PaginatedV3WorkList(BaseModel):
    """
    PaginatedV3WorkList
    """
    count: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    results: Optional[conlist(V3Work)] = None
    __properties = ["count", "next", "previous", "results"]

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
    def from_json(cls, json_str: str) -> PaginatedV3WorkList:
        """Create an instance of PaginatedV3WorkList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # set to None if next (nullable) is None
        # and __fields_set__ contains the field
        if self.next is None and "next" in self.__fields_set__:
            _dict['next'] = None

        # set to None if previous (nullable) is None
        # and __fields_set__ contains the field
        if self.previous is None and "previous" in self.__fields_set__:
            _dict['previous'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaginatedV3WorkList:
        """Create an instance of PaginatedV3WorkList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaginatedV3WorkList.parse_obj(obj)

        _obj = PaginatedV3WorkList.parse_obj({
            "count": obj.get("count"),
            "next": obj.get("next"),
            "previous": obj.get("previous"),
            "results": [V3Work.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


