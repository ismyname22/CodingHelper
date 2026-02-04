from __future__ import annotations

from typing import List

from core.schema import ProjectSpec
from validation.rules import ValidationIssue, validate


def collect_followup_questions(spec: ProjectSpec) -> List[str]:
    issues = validate(spec)
    return [issue.question for issue in issues if issue.question]


def format_validation_summary(issues: List[ValidationIssue]) -> str:
    if not issues:
        return "Keine Validierungsprobleme gefunden."
    lines = ["Validierungsprobleme:"]
    for issue in issues:
        lines.append(f"- {issue.message}")
    return "\n".join(lines)
