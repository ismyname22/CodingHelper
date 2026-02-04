import unittest

from coding_helper.assembly import Assembly
from coding_helper.cad_export import auto_generate_anchor_points
from coding_helper.component_spec import BoundingBox, ComponentSpec, Vector3


class AnchorGenerationTests(unittest.TestCase):
    def setUp(self) -> None:
        bbox = BoundingBox(Vector3(0.0, 0.0, 0.0), Vector3(10.0, 20.0, 30.0))
        self.component = ComponentSpec(name="Bracket", bounding_box=bbox)

    def test_auto_generates_center_face_edge_anchors(self) -> None:
        anchors = auto_generate_anchor_points(self.component)
        self.assertIn("center", anchors)
        self.assertIn("face_xmin", anchors)
        self.assertIn("edge_xmin_ymin", anchors)
        self.assertEqual(anchors["center"].position.as_tuple(), (5.0, 10.0, 15.0))


class AssemblyPlacementTests(unittest.TestCase):
    def test_align_components_by_anchor(self) -> None:
        bbox = BoundingBox(Vector3(0.0, 0.0, 0.0), Vector3(2.0, 2.0, 2.0))
        base = ComponentSpec(name="Base", bounding_box=bbox)
        top = ComponentSpec(name="Top", bounding_box=bbox)
        auto_generate_anchor_points(base)
        auto_generate_anchor_points(top)

        assembly = Assembly(name="Demo")
        assembly.add_component_at_anchor(base, "center", Vector3(0.0, 0.0, 0.0))
        placement = assembly.align_components_by_anchor(top, "face_zmin", base, "face_zmax")

        top_face_min = placement.world_anchor(top.anchor_points["face_zmin"]).as_tuple()
        base_face_max = assembly.placements["Base"].world_anchor(base.anchor_points["face_zmax"]).as_tuple()
        self.assertEqual(top_face_min, base_face_max)


if __name__ == "__main__":
    unittest.main()
