from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


ShapeType = Literal["box", "cylinder"]


@dataclass(frozen=True)
class Spec:
    shape: ShapeType
    width: float
    depth: float
    height: float

