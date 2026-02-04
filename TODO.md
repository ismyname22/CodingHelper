# Projektstand & Offene Aufgaben

## Aktueller Stand (Kurzüberblick)
- Grundlegende Datenmodelle für Komponenten, Assemblies und CAD-Pipeline sind vorhanden.
- Anchor-Generierung und einfache Assembly-Ausrichtung sind implementiert.
- Basis-Tests decken Anchor-Generierung und Alignment ab.

## Offene Aufgaben (TODO)
1. **Doppelte Spezifikationsmodelle konsolidieren** ✅
   - `project_spec.py` und `core/schema.py` überschneiden sich in der Domänenmodellierung.
   - Kanonisches Modell: `core/schema.py` (Migration abgeschlossen).

2. **Pipeline-Validierung testen** ✅
   - Tests für `conversation_to_spec`, `validate_spec` und `spec_to_geometry` ergänzen,
     inkl. Fehlerfällen (leere Konversation, negative Maße, unbekannte Shapes).

3. **CAD-Export konkretisieren**
   - Aktuell ist `export_component_to_cad` ein Platzhalter.
   - Ziel definieren (z. B. konkretes Exportformat) und Implementierung ergänzen.

4. **Dokumentation & Beispiele ergänzen** ✅
   - Minimaler README mit Quickstart, Beispielen für Anchor-Workflow und Pipeline-Nutzung.
   - Beispielskript in `scripts/` für einen End-to-End-Flow.

5. **Erweiterte Assembly-Logik**
   - Unterstützung für Rotationen/Orientierungen der Komponenten.
   - Kollisionsprüfungen oder Constraints in der Assembly.
