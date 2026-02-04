# CodingHelper – Dokumentation

## Überblick
CodingHelper ist eine leichtgewichtige Python-Bibliothek, die Konversationen (z. B. Prompts) in einfache CAD-Geometrien übersetzt und Komponenten über Ankerpunkte zueinander ausrichten kann. Der Fokus liegt auf einem klaren, deterministischen Pipeline-Flow: LLM-Ausgabe wird strukturiert, validiert und anschließend in CadQuery-Geometrie überführt. Zusätzlich unterstützt das Projekt das Platzieren und Ausrichten von Komponenten in Assemblies über vordefinierte Anchor Points.

## Was ist die Software?
CodingHelper ist ein „Baukasten“ für:
- **LLM→Spec→Geometrie**: Textuelle Anfragen werden in eine strukturierte Spezifikation (Spec) umgewandelt, geprüft und als CAD-Geometrie erstellt.
- **Komponenten-Assembly**: Komponenten erhalten Anchor Points (z. B. Flächenmittelpunkte) und lassen sich über diese Anker präzise zueinander ausrichten.

## Was kann die Software aktuell?
### 1) Pipeline für Geometrie-Erstellung
Die Pipeline besteht aus drei klaren Schritten:
1. **conversation_to_spec** – mappt eine Konversation auf ein strukturiertes `Spec` (Form + Maße).
2. **validate_spec** – validiert, ob Form und Maße zulässig sind.
3. **spec_to_geometry** – erzeugt deterministische CadQuery-Geometrie auf Basis des Specs.

Der Helper `run_pipeline` führt alle Schritte in der Reihenfolge aus.

### 2) Komponenten & Anchor-Workflow
Komponenten werden als `ComponentSpec` mit Bounding Box definiert. Daraus lassen sich automatisch Anchor Points generieren (z. B. Mittelpunkt, Kanten- und Flächenzentren). Diese Anchors dienen als Referenzpunkte für Assemblies:
- Komponenten können an einem Ankerpunkt platziert werden.
- Komponenten können über Ankerpunkte zueinander ausgerichtet werden.

### 3) Platzhalter-CAD-Export
Es existiert eine einfache Export-Schnittstelle, die sicherstellt, dass Anchor Points für eine Komponente vorhanden sind. Der eigentliche CAD-Export ist derzeit noch ein Platzhalter und soll in der Roadmap konkretisiert werden.

## Architekturüberblick
Die Kernbausteine sind:
- **pipeline/**: Pipeline zur Übersetzung von Konversation → Spec → Geometrie.
- **coding_helper/**: Domänenmodelle für Komponenten/Anchor Points sowie Assembly-Logik.
- **scripts/**: Beispiele, die einen End-to-End-Flow demonstrieren.

## Quickstart (kurz)
Die Kurzform ist im README enthalten. Grober Ablauf:
1. CadQuery installieren.
2. `run_pipeline()` aufrufen und ein LLM-Callable übergeben.

Für eine konkrete Code-Skizze siehe `README.md` oder `scripts/example_end_to_end.py`.

## Roadmap
Die folgenden Punkte sind die nächsten Meilensteine (basierend auf Projektplan/TODO):
1. **CAD-Export konkretisieren**
   - Zielformat festlegen (z. B. STEP/STL).
   - API-Design für den Export definieren und implementieren.

2. **Erweiterte Assembly-Logik**
   - Rotationen/Orientierungen in Assemblies einführen.
   - Kollisionsprüfung bzw. Constraints ergänzen.

3. **Weitere Doku & Beispiele**
   - Ausbau von Anwendungsbeispielen und Best Practices.

## Nicht-Ziele (aktuell)
- Vollwertiger CAD-Editor oder Visualisierungstool.
- Komplexe Geometrie-Operationen jenseits der Basisformen.
- Produktionsreifer CAD-Export (befindet sich in Planung).

## Status
Das Projekt ist bewusst schlank und fokussiert: Basis-Pipeline, Anchor-Workflow und Testabdeckung sind vorhanden; Export und erweiterte Assembly-Funktionen sind als nächste Schritte vorgesehen.
