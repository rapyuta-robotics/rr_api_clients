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
from pydantic import BaseModel, Field, constr

class ProductRequest(BaseModel):
    """
    ProductRequest
    """
    meta_data: Optional[Dict[str, Any]] = Field(None, description="optional JSON encoded metadata for this object")
    product_id: constr(strict=True, max_length=200, min_length=1) = Field(..., description="Identification key for the product.")
    name: constr(strict=True, max_length=200, min_length=1) = Field(..., description="Name for the product")
    image_url: Optional[constr(strict=True, max_length=500)] = None
    __properties = ["meta_data", "product_id", "name", "image_url"]

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
    def from_json(cls, json_str: str) -> ProductRequest:
        """Create an instance of ProductRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if meta_data (nullable) is None
        # and __fields_set__ contains the field
        if self.meta_data is None and "meta_data" in self.__fields_set__:
            _dict['meta_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductRequest:
        """Create an instance of ProductRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductRequest.parse_obj(obj)

        _obj = ProductRequest.parse_obj({
            "meta_data": obj.get("meta_data"),
            "product_id": obj.get("product_id"),
            "name": obj.get("name"),
            "image_url": obj.get("image_url")
        })
        return _obj


