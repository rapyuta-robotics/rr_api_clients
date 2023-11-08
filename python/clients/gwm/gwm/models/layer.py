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
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint, constr
from gwm.models.layer_origin_pos import LayerOriginPos

class Layer(BaseModel):
    """
    Layer
    """
    id: Optional[conint(strict=True, le=9007199254740991, ge=1)] = Field(None, description="user defined `id` of this object. Must be unique in the site or map (for nodes and edges); Default random 53 bit integer")
    name: Optional[constr(strict=True, max_length=100)] = Field(None, description="user defined `name` of this object. Must be unique in the site or map (for nodes and edges)")
    type: constr(strict=True, max_length=100) = Field(..., description="Type of the layer")
    order: Optional[conint(strict=True, le=32767, ge=0)] = Field(None, description="Layer height of the small integer (0 indicates default and on the bottom)")
    resolution: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Resolution of the map, meters / pixel")
    origin_pos: Optional[LayerOriginPos] = None
    origin_yaw: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Orientation of the map in radians")
    negate: Optional[StrictBool] = Field(None, description="Whether the white/black free/occupied semantics should be reversed (interpretation of thresholds is unaffected)")
    occupied_thresh: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Pixels with occupancy probability greater than this threshold are considered completely occupied.")
    image: Optional[StrictStr] = Field(..., description="Path to the image file containing the occupancy data; can be absolute, or relative to the location of the YAML file")
    data: Optional[StrictStr] = Field(...)
    properties: Optional[Dict[str, Any]] = Field(None, description="Additional properties for this layer in JSON format")
    free_thresh: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Pixels with occupancy probability less than this threshold are considered completely free.")
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    version: StrictInt = Field(..., description="System generated monotonic integer that is updated for each mutation to layer properties or image")
    created_at: Optional[datetime] = Field(..., description="Timestamp at which this layer was created")
    __properties = ["id", "name", "type", "order", "resolution", "origin_pos", "origin_yaw", "negate", "occupied_thresh", "image", "data", "properties", "free_thresh", "meta_data", "version", "created_at"]

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
    def from_json(cls, json_str: str) -> Layer:
        """Create an instance of Layer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "image",
                            "data",
                            "version",
                            "created_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of origin_pos
        if self.origin_pos:
            _dict['origin_pos'] = self.origin_pos.to_dict()
        # set to None if resolution (nullable) is None
        # and __fields_set__ contains the field
        if self.resolution is None and "resolution" in self.__fields_set__:
            _dict['resolution'] = None

        # set to None if origin_pos (nullable) is None
        # and __fields_set__ contains the field
        if self.origin_pos is None and "origin_pos" in self.__fields_set__:
            _dict['origin_pos'] = None

        # set to None if origin_yaw (nullable) is None
        # and __fields_set__ contains the field
        if self.origin_yaw is None and "origin_yaw" in self.__fields_set__:
            _dict['origin_yaw'] = None

        # set to None if negate (nullable) is None
        # and __fields_set__ contains the field
        if self.negate is None and "negate" in self.__fields_set__:
            _dict['negate'] = None

        # set to None if occupied_thresh (nullable) is None
        # and __fields_set__ contains the field
        if self.occupied_thresh is None and "occupied_thresh" in self.__fields_set__:
            _dict['occupied_thresh'] = None

        # set to None if image (nullable) is None
        # and __fields_set__ contains the field
        if self.image is None and "image" in self.__fields_set__:
            _dict['image'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if free_thresh (nullable) is None
        # and __fields_set__ contains the field
        if self.free_thresh is None and "free_thresh" in self.__fields_set__:
            _dict['free_thresh'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Layer:
        """Create an instance of Layer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Layer.parse_obj(obj)

        _obj = Layer.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "order": obj.get("order"),
            "resolution": obj.get("resolution"),
            "origin_pos": LayerOriginPos.from_dict(obj.get("origin_pos")) if obj.get("origin_pos") is not None else None,
            "origin_yaw": obj.get("origin_yaw"),
            "negate": obj.get("negate"),
            "occupied_thresh": obj.get("occupied_thresh"),
            "image": obj.get("image"),
            "data": obj.get("data"),
            "properties": obj.get("properties"),
            "free_thresh": obj.get("free_thresh"),
            "meta_data": obj.get("meta_data"),
            "version": obj.get("version"),
            "created_at": obj.get("created_at")
        })
        return _obj


