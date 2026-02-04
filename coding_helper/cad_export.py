from __future__ import annotations

from typing import Dict, Iterable, List

from .component_spec import AnchorPoint, BoundingBox, ComponentSpec, Vector3


def _face_normals() -> Dict[str, Vector3]:
    return {
        "face_xmin": Vector3(-1.0, 0.0, 0.0),
        "face_xmax": Vector3(1.0, 0.0, 0.0),
        "face_ymin": Vector3(0.0, -1.0, 0.0),
        "face_ymax": Vector3(0.0, 1.0, 0.0),
        "face_zmin": Vector3(0.0, 0.0, -1.0),
        "face_zmax": Vector3(0.0, 0.0, 1.0),
    }


def auto_generate_anchor_points(component: ComponentSpec) -> Dict[str, AnchorPoint]:
    """Populate anchors based on the component's bounding box.

    Anchors include the center point, edge centers, and face centers (mounting surfaces).
    """
    bbox: BoundingBox = component.bounding_box
    anchors: List[AnchorPoint] = [
        AnchorPoint("center", bbox.center, category="center"),
    ]

    for name, position in bbox.edge_centers().items():
        anchors.append(AnchorPoint(name, position, category="edge"))

    face_normals = _face_normals()
    for name, position in bbox.face_centers().items():
        anchors.append(AnchorPoint(name, position, normal=face_normals.get(name), category="face"))

    component.update_anchor_points(anchors)
    return component.anchor_points


def export_component_to_cad(component: ComponentSpec) -> Dict[str, Iterable[AnchorPoint]]:
    """Fake CAD export that ensures anchors are present for downstream assembly placement."""
    if not component.anchor_points:
        auto_generate_anchor_points(component)
    return {
        "component": component,
        "anchors": list(component.anchor_points.values()),
    }
