from __future__ import annotations

from dataclasses import asdict
from typing import Any, Callable, Mapping

import cadquery as cq

from pipeline.spec import Spec


def conversation_to_spec(
    conversation: str,
    llm_callable: Callable[[str], Mapping[str, Any]],
) -> Spec:
    """Use an LLM to map a conversation into a structured Spec."""
    if not conversation.strip():
        raise ValueError("conversation must be non-empty")

    raw_spec = llm_callable(conversation)
    return Spec(
        shape=str(raw_spec["shape"]),
        width=float(raw_spec["width"]),
        depth=float(raw_spec["depth"]),
        height=float(raw_spec["height"]),
    )


def validate_spec(spec: Spec) -> Spec:
    """Deterministically validate the Spec."""
    if spec.shape not in {"box", "cylinder"}:
        raise ValueError(f"Unsupported shape: {spec.shape}")

    for name, value in asdict(spec).items():
        if name == "shape":
            continue
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
    return spec


def spec_to_geometry(spec: Spec) -> cq.Workplane:
    """Deterministically convert a validated Spec into CadQuery geometry."""
    if spec.shape == "box":
        return cq.Workplane("XY").box(spec.width, spec.depth, spec.height)
    if spec.shape == "cylinder":
        radius = min(spec.width, spec.depth) / 2.0
        return cq.Workplane("XY").cylinder(spec.height, radius)
    raise ValueError(f"Unsupported shape: {spec.shape}")


def run_pipeline(
    conversation: str,
    llm_callable: Callable[[str], Mapping[str, Any]],
) -> cq.Workplane:
    """Run the full pipeline with deterministic steps after LLM parsing."""
    spec = conversation_to_spec(conversation, llm_callable)
    validated = validate_spec(spec)
    return spec_to_geometry(validated)

