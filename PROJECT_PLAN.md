# Projektplan: Aufgaben & Agenten

Dieser Plan teilt die offenen TODOs in klar abgegrenzte Rollen auf, damit mehrere
Agenten parallel arbeiten können, ohne sich gegenseitig zu blockieren.

## 1) Agent: Spec-Architekt ✅ (abgeschlossen)

**Ziel:** Konsolidierung der doppelten Domänenmodelle (`project_spec.py` vs. `core/schema.py`).

**Aufgaben**
- Unterschiede zwischen den Modellen dokumentieren.
- Kanonisches Modell definieren (Quelle der Wahrheit).
- Migrationspfad festlegen (Imports, Naming, Deprecations).
- Alte Modelle entfernen oder sauber delegieren.

**Ergebnisse**
- Konsolidiertes Datenmodell.
- Migration-Notizen + ggf. Changelog-Eintrag.

## 2) Agent: Pipeline-Tester ✅ (abgeschlossen)

**Ziel:** Stabiler Testumfang für die Pipeline-Validierung.

**Aufgaben**
- Tests für `conversation_to_spec`, `validate_spec`, `spec_to_geometry` erstellen.
- Positive und negative Fälle abdecken:
  - leere Konversation
  - negative Maße
  - unbekannte Shapes
- Test-Hilfsfunktionen/Fixtures definieren.

**Ergebnisse**
- Testabdeckung für Pipeline-Kernlogik.
- Fehlerfälle reproduzierbar abgesichert.

## 3) Agent: CAD-Export-Owner
**Ziel:** CAD-Export konkretisieren und implementieren.

**Aufgaben**
- Zielformat festlegen (z. B. STEP, STL).
- API-Design für `export_component_to_cad` definieren.
- Implementieren inkl. sinnvollem Rückgabeformat.

**Ergebnisse**
- Nutzbare Exportfunktion mit dokumentiertem Verhalten.

## 4) Agent: Docs & Examples ✅ (abgeschlossen)

**Ziel:** Dokumentation & Beispiele für Onboarding.

**Aufgaben**
- README um Quickstart, Pipeline-Flow und Anchor-Workflow erweitern.
- Beispielskript für End-to-End-Flow in `scripts/` pflegen.

**Ergebnisse**
- Konsistente, leicht verständliche Doku + Demo.

## 5) Agent: Assembly-Logic
**Ziel:** Erweiterte Assembly-Logik (Rotationen, Constraints).

**Aufgaben**
- Rotationen/Orientierungen definieren und modellieren.
- Kollisionsprüfung oder Constraints einführen.
- API- und Datenmodell-Anpassungen evaluieren.

**Ergebnisse**
- Erweiterte Assemblies für realistischere Szenarien.

## Abhängigkeiten & Reihenfolge (empfohlen)
1. Spec-Architekt → legt Datenmodell fest.
2. Pipeline-Tester → baut Tests auf stabiler Grundlage.
3. CAD-Export-Owner → konkretisiert Export-Schnittstelle.
4. Docs & Examples → dokumentiert verlässlichen Stand.
5. Assembly-Logic → erweitert nach soliden Basen.
