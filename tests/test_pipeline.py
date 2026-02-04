import unittest

from pipeline.pipeline import conversation_to_spec, spec_to_geometry, validate_spec
from pipeline.spec import Spec

try:
    import cadquery as cq
except ModuleNotFoundError:
    cq = None


class ConversationToSpecTests(unittest.TestCase):
    def test_rejects_empty_conversation(self) -> None:
        with self.assertRaises(ValueError):
            conversation_to_spec("   ", lambda _: {})

    def test_builds_spec_from_llm_payload(self) -> None:
        def fake_llm(_: str) -> dict[str, float | str]:
            return {"shape": "box", "width": 10, "depth": 20, "height": 30}

        spec = conversation_to_spec("Box bitte.", fake_llm)
        self.assertEqual(spec, Spec(shape="box", width=10.0, depth=20.0, height=30.0))


class ValidateSpecTests(unittest.TestCase):
    def test_rejects_unknown_shape(self) -> None:
        with self.assertRaises(ValueError):
            validate_spec(Spec(shape="sphere", width=1, depth=1, height=1))

    def test_rejects_non_positive_dimensions(self) -> None:
        with self.assertRaises(ValueError):
            validate_spec(Spec(shape="box", width=-1, depth=1, height=1))


class SpecToGeometryTests(unittest.TestCase):
    @unittest.skipUnless(cq is not None, "cadquery is required for geometry conversion")
    def test_box_geometry(self) -> None:
        workplane = spec_to_geometry(Spec(shape="box", width=1, depth=2, height=3))
        self.assertIsInstance(workplane, cq.Workplane)

    @unittest.skipUnless(cq is not None, "cadquery is required for geometry conversion")
    def test_cylinder_geometry(self) -> None:
        workplane = spec_to_geometry(Spec(shape="cylinder", width=4, depth=4, height=2))
        self.assertIsInstance(workplane, cq.Workplane)


if __name__ == "__main__":
    unittest.main()
