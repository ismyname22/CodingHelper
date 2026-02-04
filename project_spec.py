from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Dimensions:
    width: float
    depth: float
    height: float


@dataclass(frozen=True)
class ScrewHoleSpec:
    diameter: float
    distance_to_edge: float


@dataclass(frozen=True)
class ComponentSpec:
    kind: str
    clearance: Optional[Dimensions] = None


@dataclass(frozen=True)
class ProjectSpec:
    material: Optional[str] = None
    wall_thickness: Optional[float] = None
    enclosure_inner: Optional[Dimensions] = None
    screw_holes: List[ScrewHoleSpec] = field(default_factory=list)
    components: List[ComponentSpec] = field(default_factory=list)
