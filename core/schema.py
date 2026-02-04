"""Central data models for CAD workflows."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from uuid import UUID, uuid4


@dataclass(frozen=True)
class ProjectSpec:
    """High-level project definition."""

    id: UUID = field(default_factory=uuid4)
    project_type: str = ""
    dimensions_mm: Dict[str, float] = field(default_factory=dict)
    tolerances_mm: Dict[str, float] = field(default_factory=dict)
    target_material: str = ""


@dataclass(frozen=True)
class ComponentSpec:
    """Specification for a single component or standard part."""

    id: UUID = field(default_factory=uuid4)
    component_type: str = ""
    standard_part_id: Optional[str] = None
    manufacturer_specs: Dict[str, str] = field(default_factory=dict)
    footprint: Dict[str, float] = field(default_factory=dict)


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
