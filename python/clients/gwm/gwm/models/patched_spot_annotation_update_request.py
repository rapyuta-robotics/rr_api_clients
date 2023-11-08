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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, conint, constr
from gwm.models.patched_spot_annotation_update_request_nav_pos import PatchedSpotAnnotationUpdateRequestNavPos
from gwm.models.point_serializer3_d_request import PointSerializer3DRequest

class PatchedSpotAnnotationUpdateRequest(BaseModel):
    """
    PatchedSpotAnnotationUpdateRequest
    """
    id: Optional[StrictInt] = None
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    node: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    type: Optional[constr(strict=True, max_length=50)] = Field(None, description="User defined spot type")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    external_device: Optional[StrictInt] = Field(None, description="`id` of relevant related element eg: agent,map,site,spot,node,edge,external_device")
    allocatable: Optional[StrictBool] = Field(None, description="If True, spot can be allocated in response to agent queries")
    preserve: Optional[StrictBool] = Field(None, description="If True, spot is excluded from deletion, unless deleted by force")
    priority: Optional[conint(strict=True, le=32767, ge=-32768)] = Field(None, description="Associate a priority to the spot, e.g. for spot queries to allocatable spots")
    pos: Optional[PointSerializer3DRequest] = None
    yaw: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Orientation of spot in radians")
    nav_pos: Optional[PatchedSpotAnnotationUpdateRequestNavPos] = None
    nav_yaw: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Orientation of navigation position for interacting with the spot")
    __properties = ["id", "name", "node", "type", "meta_data", "external_device", "allocatable", "preserve", "priority", "pos", "yaw", "nav_pos", "nav_yaw"]

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
    def from_json(cls, json_str: str) -> PatchedSpotAnnotationUpdateRequest:
        """Create an instance of PatchedSpotAnnotationUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pos
        if self.pos:
            _dict['pos'] = self.pos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nav_pos
        if self.nav_pos:
            _dict['nav_pos'] = self.nav_pos.to_dict()
        # set to None if node (nullable) is None
        # and __fields_set__ contains the field
        if self.node is None and "node" in self.__fields_set__:
            _dict['node'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        # set to None if nav_pos (nullable) is None
        # and __fields_set__ contains the field
        if self.nav_pos is None and "nav_pos" in self.__fields_set__:
            _dict['nav_pos'] = None

        # set to None if nav_yaw (nullable) is None
        # and __fields_set__ contains the field
        if self.nav_yaw is None and "nav_yaw" in self.__fields_set__:
            _dict['nav_yaw'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedSpotAnnotationUpdateRequest:
        """Create an instance of PatchedSpotAnnotationUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedSpotAnnotationUpdateRequest.parse_obj(obj)

        _obj = PatchedSpotAnnotationUpdateRequest.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "node": obj.get("node"),
            "type": obj.get("type"),
            "meta_data": obj.get("meta_data"),
            "external_device": obj.get("external_device"),
            "allocatable": obj.get("allocatable"),
            "preserve": obj.get("preserve"),
            "priority": obj.get("priority"),
            "pos": PointSerializer3DRequest.from_dict(obj.get("pos")) if obj.get("pos") is not None else None,
            "yaw": obj.get("yaw"),
            "nav_pos": PatchedSpotAnnotationUpdateRequestNavPos.from_dict(obj.get("nav_pos")) if obj.get("nav_pos") is not None else None,
            "nav_yaw": obj.get("nav_yaw")
        })
        return _obj


