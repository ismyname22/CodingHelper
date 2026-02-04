from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .component_spec import AnchorPoint, ComponentSpec, Vector3


@dataclass(frozen=True)
class Placement:
    component: ComponentSpec
    translation: Vector3

    def world_anchor(self, anchor: AnchorPoint) -> Vector3:
        return anchor.position + self.translation


@dataclass
class Assembly:
    name: str
    placements: Dict[str, Placement] = field(default_factory=dict)

    def add_component_at_anchor(
        self,
        component: ComponentSpec,
        anchor_name: str,
        target_position: Vector3,
    ) -> Placement:
        anchor = self._get_anchor(component, anchor_name)
        translation = target_position - anchor.position
        placement = Placement(component=component, translation=translation)
        self.placements[component.name] = placement
        return placement

    def align_components_by_anchor(
        self,
        moving_component: ComponentSpec,
        moving_anchor_name: str,
        target_component: ComponentSpec,
        target_anchor_name: str,
    ) -> Placement:
        target_anchor = self._get_anchor(target_component, target_anchor_name)
        target_placement = self.placements.get(target_component.name)
        if target_placement is None:
            raise ValueError(f"Target component '{target_component.name}' is not placed.")
        target_world = target_placement.world_anchor(target_anchor)
        return self.add_component_at_anchor(moving_component, moving_anchor_name, target_world)

    def list_components(self) -> List[str]:
        return list(self.placements.keys())

    @staticmethod
    def _get_anchor(component: ComponentSpec, anchor_name: str) -> AnchorPoint:
        try:
            return component.anchor_points[anchor_name]
        except KeyError as exc:
            raise ValueError(
                f"Anchor '{anchor_name}' not found on component '{component.name}'."
            ) from exc
