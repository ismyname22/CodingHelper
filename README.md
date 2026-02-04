# CodingHelper

Lightweight helpers for translating conversational input into simple CAD geometry and
assembling components via anchor points.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install cadquery
```

```python
from pipeline.pipeline import run_pipeline

def fake_llm(prompt: str) -> dict[str, float | str]:
    return {"shape": "box", "width": 10, "depth": 8, "height": 4}

workplane = run_pipeline("Make a small box.", fake_llm)
```

## Anchor workflow example

```python
from coding_helper.assembly import Assembly
from coding_helper.cad_export import auto_generate_anchor_points
from coding_helper.component_spec import BoundingBox, ComponentSpec, Vector3

base = ComponentSpec(
    name="base",
    bounding_box=BoundingBox(Vector3(0, 0, 0), Vector3(10, 10, 2)),
)
bracket = ComponentSpec(
    name="bracket",
    bounding_box=BoundingBox(Vector3(0, 0, 0), Vector3(2, 2, 6)),
)

auto_generate_anchor_points(base)
auto_generate_anchor_points(bracket)

assembly = Assembly(name="demo")
assembly.add_component_at_anchor(base, "center", Vector3(0, 0, 0))
assembly.align_components_by_anchor(bracket, "face_zmin", base, "face_zmax")
```

## Example script

See `scripts/example_end_to_end.py` for a simple end-to-end flow that:

1. Uses a fake LLM response to build a `Spec`.
2. Generates a CadQuery `Workplane`.
3. Creates anchor points and aligns two components.
