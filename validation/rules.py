from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from core.schema import ComponentSpec, Dimensions, ProjectSpec, ScrewHoleSpec


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    question: Optional[str] = None


_MIN_WALL_THICKNESS: Dict[str, float] = {
    "pla": 1.2,
    "petg": 1.5,
    "abs": 1.5,
    "nylon": 1.8,
    "aluminium": 1.0,
    "steel": 1.2,
}

_COMPONENT_SIZES: Dict[str, Dimensions] = {
    "raspberry_pi_4": Dimensions(width=85.0, depth=56.0, height=17.0),
    "raspberry_pi_zero": Dimensions(width=65.0, depth=30.0, height=5.0),
    "nema17_motor": Dimensions(width=42.0, depth=42.0, height=48.0),
    "sg90_servo": Dimensions(width=23.0, depth=12.0, height=29.0),
}

_COMPONENT_CLEARANCE_MM = 2.0


def validate(spec: ProjectSpec) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    _validate_material_wall_thickness(spec, issues)
    _validate_screw_hole_edges(spec, issues)
    _validate_component_clearance(spec, issues)
    return issues


def _validate_material_wall_thickness(
    spec: ProjectSpec,
    issues: List[ValidationIssue],
) -> None:
    if spec.material is None:
        issues.append(
            ValidationIssue(
                code="material.missing",
                message="Material wurde nicht angegeben.",
                question="Welches Material soll für das Gehäuse verwendet werden?",
            )
        )
        return

    if spec.wall_thickness is None:
        issues.append(
            ValidationIssue(
                code="wall_thickness.missing",
                message="Wandstärke fehlt.",
                question="Welche Wandstärke ist für das Gehäuse geplant?",
            )
        )
        return

    material_key = spec.material.strip().lower()
    min_thickness = _MIN_WALL_THICKNESS.get(material_key)
    if min_thickness is None:
        issues.append(
            ValidationIssue(
                code="material.unknown",
                message=f"Unbekanntes Material '{spec.material}'.",
                question="Kannst du das Material präzisieren oder ein bekanntes Material wählen?",
            )
        )
        return

    if spec.wall_thickness < min_thickness:
        issues.append(
            ValidationIssue(
                code="wall_thickness.too_thin",
                message=(
                    "Wandstärke unterschreitet die Mindestanforderung: "
                    f"{spec.wall_thickness:.2f} mm < {min_thickness:.2f} mm."
                ),
                question=(
                    "Welche Wandstärke möchtest du stattdessen verwenden? "
                    f"Empfohlen sind mindestens {min_thickness:.2f} mm für {spec.material}."
                ),
            )
        )


def _validate_screw_hole_edges(
    spec: ProjectSpec,
    issues: List[ValidationIssue],
) -> None:
    if not spec.screw_holes:
        issues.append(
            ValidationIssue(
                code="screws.missing",
                message="Keine Schraubenlöcher angegeben.",
                question="Wie viele Schraubenlöcher gibt es und wie groß sind sie?",
            )
        )
        return

    for index, hole in enumerate(spec.screw_holes, start=1):
        min_edge_distance = max(hole.diameter * 2.0, 2.0)
        if hole.distance_to_edge < min_edge_distance:
            issues.append(
                ValidationIssue(
                    code="screws.edge_distance.too_small",
                    message=(
                        "Schraubenloch-Abstand zur Kante ist zu klein: "
                        f"{hole.distance_to_edge:.2f} mm < {min_edge_distance:.2f} mm "
                        f"(Loch {index})."
                    ),
                    question=(
                        "Bitte gib den Abstand der Schraubenlöcher zur Gehäusekante an. "
                        f"Für Loch {index} sollten es mindestens {min_edge_distance:.2f} mm sein."
                    ),
                )
            )


def _validate_component_clearance(
    spec: ProjectSpec,
    issues: List[ValidationIssue],
) -> None:
    if not spec.components:
        issues.append(
            ValidationIssue(
                code="components.missing",
                message="Keine Bauteile angegeben.",
                question="Welche Standard-Bauteile (z. B. Raspberry Pi, Motoren) sollen hinein?",
            )
        )
        return

    if spec.enclosure_inner is None:
        issues.append(
            ValidationIssue(
                code="enclosure_inner.missing",
                message="Innenmaße des Gehäuses fehlen.",
                question="Welche Innenmaße (Breite, Tiefe, Höhe) sind geplant?",
            )
        )
        return

    for component in spec.components:
        _validate_component_dimensions(component, spec.enclosure_inner, issues)


def _validate_component_dimensions(
    component: ComponentSpec,
    enclosure_inner: Dimensions,
    issues: List[ValidationIssue],
) -> None:
    required = _resolve_component_dimensions(component)
    if required is None:
        issues.append(
            ValidationIssue(
                code="component.unknown",
                message=f"Keine Maße für Bauteil '{component.kind}' hinterlegt.",
                question=(
                    "Kannst du die Maße des Bauteils angeben (Breite, Tiefe, Höhe)?"
                ),
            )
        )
        return

    if not _fits(required, enclosure_inner):
        issues.append(
            ValidationIssue(
                code="component.no_clearance",
                message=(
                    f"Bauteil '{component.kind}' passt nicht in den verfügbaren Innenraum. "
                    f"Benötigt {required.width:.2f}x{required.depth:.2f}x{required.height:.2f} mm, "
                    "Innenraum ist "
                    f"{enclosure_inner.width:.2f}x{enclosure_inner.depth:.2f}x{enclosure_inner.height:.2f} mm."
                ),
                question=(
                    "Soll der Innenraum vergrößert werden oder gibt es alternative Bauteilgrößen?"
                ),
            )
        )


def _resolve_component_dimensions(component: ComponentSpec) -> Optional[Dimensions]:
    if component.clearance is not None:
        return component.clearance
    base = _COMPONENT_SIZES.get(component.kind.strip().lower())
    if base is None:
        return None
    return Dimensions(
        width=base.width + _COMPONENT_CLEARANCE_MM * 2,
        depth=base.depth + _COMPONENT_CLEARANCE_MM * 2,
        height=base.height + _COMPONENT_CLEARANCE_MM * 2,
    )


def _fits(required: Dimensions, available: Dimensions) -> bool:
    return (
        required.width <= available.width
        and required.depth <= available.depth
        and required.height <= available.height
    )
