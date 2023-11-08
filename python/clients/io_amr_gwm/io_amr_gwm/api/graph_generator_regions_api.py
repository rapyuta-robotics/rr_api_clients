# coding: utf-8

"""
    IO-AMR GWM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: devel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBytes, StrictFloat, StrictInt, StrictStr, constr

from typing import List, Optional, Union

from io_amr_gwm.models.region import Region
from io_amr_gwm.models.region_db_json import RegionDbJson

from io_amr_gwm.api_client import ApiClient
from io_amr_gwm.api_response import ApiResponse
from io_amr_gwm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GraphGeneratorRegionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def v1_graph_generator_download_aisle_regions_list(self, map_name : Annotated[StrictStr, Field(..., description="Map to download the regions from")], **kwargs) -> List[RegionDbJson]:  # noqa: E501
        """v1_graph_generator_download_aisle_regions_list  # noqa: E501

        Download the Aisle Regions of a Map  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_download_aisle_regions_list(map_name, async_req=True)
        >>> result = thread.get()

        :param map_name: Map to download the regions from (required)
        :type map_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[RegionDbJson]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v1_graph_generator_download_aisle_regions_list_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v1_graph_generator_download_aisle_regions_list_with_http_info(map_name, **kwargs)  # noqa: E501

    @validate_arguments
    def v1_graph_generator_download_aisle_regions_list_with_http_info(self, map_name : Annotated[StrictStr, Field(..., description="Map to download the regions from")], **kwargs) -> ApiResponse:  # noqa: E501
        """v1_graph_generator_download_aisle_regions_list  # noqa: E501

        Download the Aisle Regions of a Map  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_download_aisle_regions_list_with_http_info(map_name, async_req=True)
        >>> result = thread.get()

        :param map_name: Map to download the regions from (required)
        :type map_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[RegionDbJson], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'map_name'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_graph_generator_download_aisle_regions_list" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('map_name') is not None:  # noqa: E501
            _query_params.append(('map_name', _params['map_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['tokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[RegionDbJson]",
        }

        return self.api_client.call_api(
            '/v1/graph_generator/download_aisle_regions', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v1_graph_generator_generate_aisle_regions_create(self, map_name : constr(strict=True, min_length=1), map_layer_name : constr(strict=True, min_length=1), origin_x : Union[StrictFloat, StrictInt], origin_y : Union[StrictFloat, StrictInt], resolution : Optional[Union[StrictFloat, StrictInt]] = None, min_aisle_width : Optional[Union[StrictFloat, StrictInt]] = None, min_shelf_area : Optional[Union[StrictFloat, StrictInt]] = None, min_shelf_ratio : Optional[Union[StrictFloat, StrictInt]] = None, shelf_approx : Optional[Union[StrictFloat, StrictInt]] = None, **kwargs) -> Region:  # noqa: E501
        """v1_graph_generator_generate_aisle_regions_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_generate_aisle_regions_create(map_name, map_layer_name, origin_x, origin_y, resolution, min_aisle_width, min_shelf_area, min_shelf_ratio, shelf_approx, async_req=True)
        >>> result = thread.get()

        :param map_name: (required)
        :type map_name: str
        :param map_layer_name: (required)
        :type map_layer_name: str
        :param origin_x: (required)
        :type origin_x: float
        :param origin_y: (required)
        :type origin_y: float
        :param resolution:
        :type resolution: float
        :param min_aisle_width:
        :type min_aisle_width: float
        :param min_shelf_area:
        :type min_shelf_area: float
        :param min_shelf_ratio:
        :type min_shelf_ratio: float
        :param shelf_approx:
        :type shelf_approx: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Region
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v1_graph_generator_generate_aisle_regions_create_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v1_graph_generator_generate_aisle_regions_create_with_http_info(map_name, map_layer_name, origin_x, origin_y, resolution, min_aisle_width, min_shelf_area, min_shelf_ratio, shelf_approx, **kwargs)  # noqa: E501

    @validate_arguments
    def v1_graph_generator_generate_aisle_regions_create_with_http_info(self, map_name : constr(strict=True, min_length=1), map_layer_name : constr(strict=True, min_length=1), origin_x : Union[StrictFloat, StrictInt], origin_y : Union[StrictFloat, StrictInt], resolution : Optional[Union[StrictFloat, StrictInt]] = None, min_aisle_width : Optional[Union[StrictFloat, StrictInt]] = None, min_shelf_area : Optional[Union[StrictFloat, StrictInt]] = None, min_shelf_ratio : Optional[Union[StrictFloat, StrictInt]] = None, shelf_approx : Optional[Union[StrictFloat, StrictInt]] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """v1_graph_generator_generate_aisle_regions_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_generate_aisle_regions_create_with_http_info(map_name, map_layer_name, origin_x, origin_y, resolution, min_aisle_width, min_shelf_area, min_shelf_ratio, shelf_approx, async_req=True)
        >>> result = thread.get()

        :param map_name: (required)
        :type map_name: str
        :param map_layer_name: (required)
        :type map_layer_name: str
        :param origin_x: (required)
        :type origin_x: float
        :param origin_y: (required)
        :type origin_y: float
        :param resolution:
        :type resolution: float
        :param min_aisle_width:
        :type min_aisle_width: float
        :param min_shelf_area:
        :type min_shelf_area: float
        :param min_shelf_ratio:
        :type min_shelf_ratio: float
        :param shelf_approx:
        :type shelf_approx: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Region, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'map_name',
            'map_layer_name',
            'origin_x',
            'origin_y',
            'resolution',
            'min_aisle_width',
            'min_shelf_area',
            'min_shelf_ratio',
            'shelf_approx'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_graph_generator_generate_aisle_regions_create" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['map_name']:
            _form_params.append(('map_name', _params['map_name']))

        if _params['map_layer_name']:
            _form_params.append(('map_layer_name', _params['map_layer_name']))

        if _params['origin_x']:
            _form_params.append(('origin_x', _params['origin_x']))

        if _params['origin_y']:
            _form_params.append(('origin_y', _params['origin_y']))

        if _params['resolution']:
            _form_params.append(('resolution', _params['resolution']))

        if _params['min_aisle_width']:
            _form_params.append(('min_aisle_width', _params['min_aisle_width']))

        if _params['min_shelf_area']:
            _form_params.append(('min_shelf_area', _params['min_shelf_area']))

        if _params['min_shelf_ratio']:
            _form_params.append(('min_shelf_ratio', _params['min_shelf_ratio']))

        if _params['shelf_approx']:
            _form_params.append(('shelf_approx', _params['shelf_approx']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['tokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "Region",
        }

        return self.api_client.call_api(
            '/v1/graph_generator/generate_aisle_regions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def v1_graph_generator_upload_aisle_regions_create(self, map_name : Annotated[StrictStr, Field(..., description="Map to upload the regions to")], aisle_regions : Union[StrictBytes, StrictStr], **kwargs) -> None:  # noqa: E501
        """v1_graph_generator_upload_aisle_regions_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_upload_aisle_regions_create(map_name, aisle_regions, async_req=True)
        >>> result = thread.get()

        :param map_name: Map to upload the regions to (required)
        :type map_name: str
        :param aisle_regions: (required)
        :type aisle_regions: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the v1_graph_generator_upload_aisle_regions_create_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.v1_graph_generator_upload_aisle_regions_create_with_http_info(map_name, aisle_regions, **kwargs)  # noqa: E501

    @validate_arguments
    def v1_graph_generator_upload_aisle_regions_create_with_http_info(self, map_name : Annotated[StrictStr, Field(..., description="Map to upload the regions to")], aisle_regions : Union[StrictBytes, StrictStr], **kwargs) -> ApiResponse:  # noqa: E501
        """v1_graph_generator_upload_aisle_regions_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_graph_generator_upload_aisle_regions_create_with_http_info(map_name, aisle_regions, async_req=True)
        >>> result = thread.get()

        :param map_name: Map to upload the regions to (required)
        :type map_name: str
        :param aisle_regions: (required)
        :type aisle_regions: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'map_name',
            'aisle_regions'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_graph_generator_upload_aisle_regions_create" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('map_name') is not None:  # noqa: E501
            _query_params.append(('map_name', _params['map_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['aisle_regions']:
            _files['aisle_regions'] = _params['aisle_regions']

        # process the body parameter
        _body_params = None
        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['tokenAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v1/graph_generator/upload_aisle_regions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
