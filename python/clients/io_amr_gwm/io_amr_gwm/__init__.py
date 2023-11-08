# coding: utf-8

# flake8: noqa

"""
    IO-AMR GWM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: devel
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from io_amr_gwm.api.containers_app_asset_location_api import ContainersAppAssetLocationApi
from io_amr_gwm.api.containers_app_container_descriptor_api import ContainersAppContainerDescriptorApi
from io_amr_gwm.api.containers_app_container_master_api import ContainersAppContainerMasterApi
from io_amr_gwm.api.containers_app_product_api import ContainersAppProductApi
from io_amr_gwm.api.errors_app_error_actions_api import ErrorsAppErrorActionsApi
from io_amr_gwm.api.errors_app_error_types_api import ErrorsAppErrorTypesApi
from io_amr_gwm.api.graph_generator_graph_api import GraphGeneratorGraphApi
from io_amr_gwm.api.graph_generator_locations_api import GraphGeneratorLocationsApi
from io_amr_gwm.api.graph_generator_regions_api import GraphGeneratorRegionsApi
from io_amr_gwm.api.maps_app_edges_api import MapsAppEdgesApi
from io_amr_gwm.api.maps_app_layers_api import MapsAppLayersApi
from io_amr_gwm.api.maps_app_maps_api import MapsAppMapsApi
from io_amr_gwm.api.maps_app_nodes_api import MapsAppNodesApi
from io_amr_gwm.api.maps_app_regions_api import MapsAppRegionsApi
from io_amr_gwm.api.maps_app_spots_api import MapsAppSpotsApi
from io_amr_gwm.api.robots_app_agents_api import RobotsAppAgentsApi
from io_amr_gwm.api.robots_app_robot_descriptors_api import RobotsAppRobotDescriptorsApi
from io_amr_gwm.api.robots_app_robots_api import RobotsAppRobotsApi
from io_amr_gwm.api.sites_app_external_devices_api import SitesAppExternalDevicesApi
from io_amr_gwm.api.sites_app_schemas_api import SitesAppSchemasApi
from io_amr_gwm.api.sites_app_sites_api import SitesAppSitesApi
from io_amr_gwm.api.works_app_agent_task_fragments_api import WorksAppAgentTaskFragmentsApi
from io_amr_gwm.api.works_app_agent_tasks_api import WorksAppAgentTasksApi
from io_amr_gwm.api.works_app_work_fragments_v2_api import WorksAppWorkFragmentsV2Api
from io_amr_gwm.api.works_app_work_fragments_v3_api import WorksAppWorkFragmentsV3Api
from io_amr_gwm.api.works_app_works_v2_api import WorksAppWorksV2Api
from io_amr_gwm.api.works_app_works_v3_api import WorksAppWorksV3Api

# import ApiClient
from io_amr_gwm.api_response import ApiResponse
from io_amr_gwm.api_client import ApiClient
from io_amr_gwm.configuration import Configuration
from io_amr_gwm.exceptions import OpenApiException
from io_amr_gwm.exceptions import ApiTypeError
from io_amr_gwm.exceptions import ApiValueError
from io_amr_gwm.exceptions import ApiKeyError
from io_amr_gwm.exceptions import ApiAttributeError
from io_amr_gwm.exceptions import ApiException

# import models into sdk package
from io_amr_gwm.models.activate_work import ActivateWork
from io_amr_gwm.models.activate_work_request import ActivateWorkRequest
from io_amr_gwm.models.agent import Agent
from io_amr_gwm.models.agent_mode_request import AgentModeRequest
from io_amr_gwm.models.agent_request import AgentRequest
from io_amr_gwm.models.agent_task import AgentTask
from io_amr_gwm.models.agent_task_fragment import AgentTaskFragment
from io_amr_gwm.models.agent_task_fragment_request import AgentTaskFragmentRequest
from io_amr_gwm.models.agent_task_request import AgentTaskRequest
from io_amr_gwm.models.asset import Asset
from io_amr_gwm.models.asset_location import AssetLocation
from io_amr_gwm.models.asset_location_location import AssetLocationLocation
from io_amr_gwm.models.asset_location_location_request import AssetLocationLocationRequest
from io_amr_gwm.models.asset_location_request import AssetLocationRequest
from io_amr_gwm.models.asset_request import AssetRequest
from io_amr_gwm.models.auto_recovery_action import AutoRecoveryAction
from io_amr_gwm.models.auto_recovery_action_request import AutoRecoveryActionRequest
from io_amr_gwm.models.container import Container
from io_amr_gwm.models.container_descriptor import ContainerDescriptor
from io_amr_gwm.models.container_descriptor_request import ContainerDescriptorRequest
from io_amr_gwm.models.container_request import ContainerRequest
from io_amr_gwm.models.download_graph_response import DownloadGraphResponse
from io_amr_gwm.models.edge import Edge
from io_amr_gwm.models.edge_request import EdgeRequest
from io_amr_gwm.models.error_action import ErrorAction
from io_amr_gwm.models.error_action_request import ErrorActionRequest
from io_amr_gwm.models.error_type import ErrorType
from io_amr_gwm.models.error_type_request import ErrorTypeRequest
from io_amr_gwm.models.external_device import ExternalDevice
from io_amr_gwm.models.external_device_request import ExternalDeviceRequest
from io_amr_gwm.models.inline_agent_task_fragment import InlineAgentTaskFragment
from io_amr_gwm.models.inline_agent_task_fragment_request import InlineAgentTaskFragmentRequest
from io_amr_gwm.models.internal_work_payload_fragment import InternalWorkPayloadFragment
from io_amr_gwm.models.internal_work_payload_fragment_request import InternalWorkPayloadFragmentRequest
from io_amr_gwm.models.internal_work_payload_fragment_request_to_pos import InternalWorkPayloadFragmentRequestToPos
from io_amr_gwm.models.internal_work_payload_fragment_to_pos import InternalWorkPayloadFragmentToPos
from io_amr_gwm.models.layer import Layer
from io_amr_gwm.models.layer_data import LayerData
from io_amr_gwm.models.layer_image import LayerImage
from io_amr_gwm.models.layer_origin_pos import LayerOriginPos
from io_amr_gwm.models.layer_request import LayerRequest
from io_amr_gwm.models.layer_request_origin_pos import LayerRequestOriginPos
from io_amr_gwm.models.layer_yaml import LayerYAML
from io_amr_gwm.models.location import Location
from io_amr_gwm.models.location_request import LocationRequest
from io_amr_gwm.models.map import Map
from io_amr_gwm.models.map_export_request import MapExportRequest
from io_amr_gwm.models.map_graph_update import MapGraphUpdate
from io_amr_gwm.models.map_request import MapRequest
from io_amr_gwm.models.model_schema import ModelSchema
from io_amr_gwm.models.node import Node
from io_amr_gwm.models.node_db_json import NodeDbJson
from io_amr_gwm.models.node_request import NodeRequest
from io_amr_gwm.models.paginated_agent_task_fragment_list import PaginatedAgentTaskFragmentList
from io_amr_gwm.models.paginated_agent_task_list import PaginatedAgentTaskList
from io_amr_gwm.models.paginated_asset_location_list import PaginatedAssetLocationList
from io_amr_gwm.models.paginated_container_descriptor_list import PaginatedContainerDescriptorList
from io_amr_gwm.models.paginated_container_list import PaginatedContainerList
from io_amr_gwm.models.paginated_product_list import PaginatedProductList
from io_amr_gwm.models.paginated_v3_work_fragment_list import PaginatedV3WorkFragmentList
from io_amr_gwm.models.paginated_v3_work_list import PaginatedV3WorkList
from io_amr_gwm.models.paginated_work_payload_fragment_list import PaginatedWorkPayloadFragmentList
from io_amr_gwm.models.patched_agent_request import PatchedAgentRequest
from io_amr_gwm.models.patched_agent_task_fragment_request import PatchedAgentTaskFragmentRequest
from io_amr_gwm.models.patched_agent_task_request import PatchedAgentTaskRequest
from io_amr_gwm.models.patched_asset_location_patch_request import PatchedAssetLocationPatchRequest
from io_amr_gwm.models.patched_asset_location_request import PatchedAssetLocationRequest
from io_amr_gwm.models.patched_container_descriptor_request import PatchedContainerDescriptorRequest
from io_amr_gwm.models.patched_container_request import PatchedContainerRequest
from io_amr_gwm.models.patched_edge_request import PatchedEdgeRequest
from io_amr_gwm.models.patched_error_action_request import PatchedErrorActionRequest
from io_amr_gwm.models.patched_error_type_request import PatchedErrorTypeRequest
from io_amr_gwm.models.patched_external_device_request import PatchedExternalDeviceRequest
from io_amr_gwm.models.patched_internal_work_payload_fragment_request import PatchedInternalWorkPayloadFragmentRequest
from io_amr_gwm.models.patched_layer_request import PatchedLayerRequest
from io_amr_gwm.models.patched_map_graph_update_request import PatchedMapGraphUpdateRequest
from io_amr_gwm.models.patched_node_request import PatchedNodeRequest
from io_amr_gwm.models.patched_product_request import PatchedProductRequest
from io_amr_gwm.models.patched_region_request import PatchedRegionRequest
from io_amr_gwm.models.patched_robot_descriptor_request import PatchedRobotDescriptorRequest
from io_amr_gwm.models.patched_robot_descriptor_request_footprint import PatchedRobotDescriptorRequestFootprint
from io_amr_gwm.models.patched_robot_request import PatchedRobotRequest
from io_amr_gwm.models.patched_schema_request import PatchedSchemaRequest
from io_amr_gwm.models.patched_site_request import PatchedSiteRequest
from io_amr_gwm.models.patched_spot_annotation_update_request import PatchedSpotAnnotationUpdateRequest
from io_amr_gwm.models.patched_spot_annotation_update_request_nav_pos import PatchedSpotAnnotationUpdateRequestNavPos
from io_amr_gwm.models.patched_v3_work_external_update_request import PatchedV3WorkExternalUpdateRequest
from io_amr_gwm.models.patched_v3_work_fragment_request import PatchedV3WorkFragmentRequest
from io_amr_gwm.models.patched_v3_work_internal_update_request import PatchedV3WorkInternalUpdateRequest
from io_amr_gwm.models.patched_work_external_update_request import PatchedWorkExternalUpdateRequest
from io_amr_gwm.models.patched_work_internal_update_request import PatchedWorkInternalUpdateRequest
from io_amr_gwm.models.patched_work_payload_fragment_request import PatchedWorkPayloadFragmentRequest
from io_amr_gwm.models.point import Point
from io_amr_gwm.models.point_request import PointRequest
from io_amr_gwm.models.point_serializer3_d import PointSerializer3D
from io_amr_gwm.models.point_serializer3_d_request import PointSerializer3DRequest
from io_amr_gwm.models.polygon import Polygon
from io_amr_gwm.models.polygon_request import PolygonRequest
from io_amr_gwm.models.product import Product
from io_amr_gwm.models.product_request import ProductRequest
from io_amr_gwm.models.region import Region
from io_amr_gwm.models.region_db_json import RegionDbJson
from io_amr_gwm.models.region_export_request import RegionExportRequest
from io_amr_gwm.models.region_request import RegionRequest
from io_amr_gwm.models.robot import Robot
from io_amr_gwm.models.robot_descriptor import RobotDescriptor
from io_amr_gwm.models.robot_descriptor_footprint import RobotDescriptorFootprint
from io_amr_gwm.models.robot_descriptor_request import RobotDescriptorRequest
from io_amr_gwm.models.robot_request import RobotRequest
from io_amr_gwm.models.schema_request import SchemaRequest
from io_amr_gwm.models.site import Site
from io_amr_gwm.models.site_export import SiteExport
from io_amr_gwm.models.site_request import SiteRequest
from io_amr_gwm.models.site_status import SiteStatus
from io_amr_gwm.models.spot_annotation import SpotAnnotation
from io_amr_gwm.models.spot_annotation_db_json import SpotAnnotationDbJson
from io_amr_gwm.models.spot_annotation_export_request import SpotAnnotationExportRequest
from io_amr_gwm.models.spot_annotation_nav_pos import SpotAnnotationNavPos
from io_amr_gwm.models.spot_annotation_request import SpotAnnotationRequest
from io_amr_gwm.models.spot_annotation_update import SpotAnnotationUpdate
from io_amr_gwm.models.v1_containers_create_descriptor_parameter_inner import V1ContainersCreateDescriptorParameterInner
from io_amr_gwm.models.v3_activate_work import V3ActivateWork
from io_amr_gwm.models.v3_activate_work_request import V3ActivateWorkRequest
from io_amr_gwm.models.v3_work import V3Work
from io_amr_gwm.models.v3_work_external_update import V3WorkExternalUpdate
from io_amr_gwm.models.v3_work_fragment import V3WorkFragment
from io_amr_gwm.models.v3_work_fragment_bulk_update_request import V3WorkFragmentBulkUpdateRequest
from io_amr_gwm.models.v3_work_fragment_request import V3WorkFragmentRequest
from io_amr_gwm.models.v3_work_internal_update import V3WorkInternalUpdate
from io_amr_gwm.models.v3_work_internal_update_request import V3WorkInternalUpdateRequest
from io_amr_gwm.models.v3_work_request import V3WorkRequest
from io_amr_gwm.models.work import Work
from io_amr_gwm.models.work_external_update import WorkExternalUpdate
from io_amr_gwm.models.work_internal_update import WorkInternalUpdate
from io_amr_gwm.models.work_payload_fragment import WorkPayloadFragment
from io_amr_gwm.models.work_request import WorkRequest
