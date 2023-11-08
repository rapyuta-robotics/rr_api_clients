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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, conint, constr
from io_amr_gwm.models.asset import Asset
from io_amr_gwm.models.asset_location_location import AssetLocationLocation

class AssetLocation(BaseModel):
    """
    AssetLocation
    """
    id: StrictInt = Field(...)
    modified: datetime = Field(...)
    application_data: Optional[Dict[str, Any]] = Field(None, description="JSON encoded application data for objects of this type")
    asset: Asset = Field(...)
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    location: AssetLocationLocation = Field(...)
    type: Optional[constr(strict=True, max_length=50)] = Field(None, description="User defined asset location type")
    index: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = Field(None, description="Unique per spot if present")
    status: Optional[constr(strict=True, max_length=32)] = None
    __properties = ["id", "modified", "application_data", "asset", "meta_data", "location", "type", "index", "status"]

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
    def from_json(cls, json_str: str) -> AssetLocation:
        """Create an instance of AssetLocation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "modified",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if application_data (nullable) is None
        # and __fields_set__ contains the field
        if self.application_data is None and "application_data" in self.__fields_set__:
            _dict['application_data'] = None

        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        # set to None if index (nullable) is None
        # and __fields_set__ contains the field
        if self.index is None and "index" in self.__fields_set__:
            _dict['index'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetLocation:
        """Create an instance of AssetLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetLocation.parse_obj(obj)

        _obj = AssetLocation.parse_obj({
            "id": obj.get("id"),
            "modified": obj.get("modified"),
            "application_data": obj.get("application_data"),
            "asset": Asset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "meta_data": obj.get("meta_data"),
            "location": AssetLocationLocation.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "type": obj.get("type"),
            "index": obj.get("index"),
            "status": obj.get("status")
        })
        return _obj


