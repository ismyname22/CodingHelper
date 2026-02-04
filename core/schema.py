"""Central data models for CAD workflows."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from uuid import UUID, uuid4


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


@dataclass(frozen=True)
class AssemblySpec:
    """Definition of how components are assembled."""

    id: UUID = field(default_factory=uuid4)
    component_refs: List[UUID] = field(default_factory=list)
    rough_positions_mm: Dict[UUID, Dict[str, float]] = field(default_factory=dict)
    constraints: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class PrintProfile:
    """3D printing parameters."""

    id: UUID = field(default_factory=uuid4)
    layer_height_mm: float = 0.2
    infill_percent: float = 20.0
    wall_thickness_mm: float = 1.2
