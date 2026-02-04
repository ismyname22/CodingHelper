"""CodingHelper package for component specs and assembly placement."""

from .component_spec import AnchorPoint, BoundingBox, ComponentSpec, Vector3
from .assembly import Assembly
from .cad_export import auto_generate_anchor_points

__all__ = [
    "AnchorPoint",
    "Assembly",
    "BoundingBox",
    "ComponentSpec",
    "Vector3",
    "auto_generate_anchor_points",
]
