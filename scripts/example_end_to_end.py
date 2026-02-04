from __future__ import annotations

from typing import Any, Mapping

from coding_helper.assembly import Assembly
from coding_helper.cad_export import auto_generate_anchor_points
from coding_helper.component_spec import BoundingBox, ComponentSpec, Vector3
from pipeline.pipeline import run_pipeline


def fake_llm(prompt: str) -> Mapping[str, Any]:
    """Stubbed LLM response used for the demo pipeline."""
    return {"shape": "box", "width": 10, "depth": 8, "height": 4}


def main() -> None:
    workplane = run_pipeline("Make a small box.", fake_llm)
    print(f"Generated CAD type: {type(workplane)}")

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

    print("Placed components:", assembly.list_components())


if __name__ == "__main__":
    main()
