from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Tuple


@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, scalar: float) -> "Vector3":
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __mul__(self, scalar: float) -> "Vector3":
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def as_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)


@dataclass(frozen=True)
class BoundingBox:
    minimum: Vector3
    maximum: Vector3

    @property
    def center(self) -> Vector3:
        return (self.minimum + self.maximum) / 2.0

    @property
    def extents(self) -> Vector3:
        return self.maximum - self.minimum

    def face_centers(self) -> Dict[str, Vector3]:
        min_pt = self.minimum
        max_pt = self.maximum
        center = self.center
        return {
            "face_xmin": Vector3(min_pt.x, center.y, center.z),
            "face_xmax": Vector3(max_pt.x, center.y, center.z),
            "face_ymin": Vector3(center.x, min_pt.y, center.z),
            "face_ymax": Vector3(center.x, max_pt.y, center.z),
            "face_zmin": Vector3(center.x, center.y, min_pt.z),
            "face_zmax": Vector3(center.x, center.y, max_pt.z),
        }

    def edge_centers(self) -> Dict[str, Vector3]:
        min_pt = self.minimum
        max_pt = self.maximum
        return {
            "edge_xmin_ymin": Vector3(min_pt.x, min_pt.y, (min_pt.z + max_pt.z) / 2.0),
            "edge_xmin_ymax": Vector3(min_pt.x, max_pt.y, (min_pt.z + max_pt.z) / 2.0),
            "edge_xmax_ymin": Vector3(max_pt.x, min_pt.y, (min_pt.z + max_pt.z) / 2.0),
            "edge_xmax_ymax": Vector3(max_pt.x, max_pt.y, (min_pt.z + max_pt.z) / 2.0),
            "edge_xmin_zmin": Vector3(min_pt.x, (min_pt.y + max_pt.y) / 2.0, min_pt.z),
            "edge_xmin_zmax": Vector3(min_pt.x, (min_pt.y + max_pt.y) / 2.0, max_pt.z),
            "edge_xmax_zmin": Vector3(max_pt.x, (min_pt.y + max_pt.y) / 2.0, min_pt.z),
            "edge_xmax_zmax": Vector3(max_pt.x, (min_pt.y + max_pt.y) / 2.0, max_pt.z),
            "edge_ymin_zmin": Vector3((min_pt.x + max_pt.x) / 2.0, min_pt.y, min_pt.z),
            "edge_ymin_zmax": Vector3((min_pt.x + max_pt.x) / 2.0, min_pt.y, max_pt.z),
            "edge_ymax_zmin": Vector3((min_pt.x + max_pt.x) / 2.0, max_pt.y, min_pt.z),
            "edge_ymax_zmax": Vector3((min_pt.x + max_pt.x) / 2.0, max_pt.y, max_pt.z),
        }


@dataclass(frozen=True)
class AnchorPoint:
    name: str
    position: Vector3
    normal: Vector3 | None = None
    category: str | None = None


@dataclass
class ComponentSpec:
    name: str
    bounding_box: BoundingBox
    anchor_points: Dict[str, AnchorPoint] = field(default_factory=dict)

    def update_anchor_points(self, anchors: Iterable[AnchorPoint]) -> None:
        for anchor in anchors:
            self.anchor_points[anchor.name] = anchor
