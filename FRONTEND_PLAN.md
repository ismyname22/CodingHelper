# Frontend-Plan: PWA & moderne Web-Architektur

## Zielbild
Ein modernes, performantes Frontend als **Progressive Web App (PWA)**, das die
LLM→Spec→Geometrie-Pipeline visuell bedienbar macht, Assemblies verwaltet und
Ergebnisse klar nachvollziehbar darstellt. Fokus: **produktive UX**, **skalierbare
Architektur**, **offline-fähige Kernfunktionen** (Lesen, Wiederverwenden von Projekten).

## 1) Geplante UI-Bereiche (Information Architecture)

### 1.0 Navigation & Layout
- **Hauptnavigation**: Projekte, Editor, Assembly, Export, Einstellungen.
- **Arbeitsbereich**: Split-Layout (links Eingaben/Spec, rechts Vorschau).
- **Context Bar**: Projektstatus, Validierung, Sync/Offline-Status.

### 1.1 Start / Projekte
- **Projektliste**: zuletzt geöffnete Projekte, Tags, Suche.
- **Projekt erstellen**: Name, Beschreibung, Ziel-Format (STEP/STL).
- **Statusindikator**: Pipeline-Status (Idle/Validierung/Erfolg/Fehler).

### 1.2 Prompt & Spezifikation
- **Prompt-Panel**: Eingabe der Konversation (LLM-Input), Verlauf, Quick-Templates.
- **Spec-Panel**: strukturierte Darstellung der generierten Spec (form, Maße).
- **Validierungsfeedback**: Inline-Fehler + Hinweise.
- **Aktionen**: „Validieren“, „Geometrie erzeugen“, „Export vorbereiten“.

### 1.3 Geometrie & Vorschau
- **3D-Preview**: WebGL (z. B. Three.js) für Workplane/Komponenten.
- **Bounding-Box & Anchor-Ansicht**: Umschaltbar, Anchor-Labels ein/aus.
- **Messwerkzeuge**: Maße ablesen, Achsen/Grids.

### 1.4 Assembly-Editor
- **Komponentenliste**: Komponenten, Anchors, Status.
- **Placement-Workflow**: „An Anker platzieren“ & „Anker ausrichten“.
- **Alignment-History**: Undo/Redo, Step-by-Step.

### 1.5 Export & Versionierung
- **Export-Zentrum**: Formatwahl, Version, Dateiname.
- **Revisionen**: Spec-Änderungen, Unterschiede, Kommentare.
- **Download/Share**: Export als Datei, ggf. Link.

### 1.6 Einstellungen & System
- **PWA-Status**: Offline-Status, Sync-Queue, Cache.
- **Theming**: Dark/Light, Accessibility (Kontrast, Schrift).
- **Telemetry (optional)**: Opt-in, Fehlerberichte.

## 2) Geplante UI-Funktionalität (User Flows)

### Flow A: Prompt → Spec → Geometrie
1. Nutzer erstellt Projekt.
2. Prompt eingeben, „Validieren“.
3. Spec-Panel zeigt strukturierte Ausgabe + Fehler/Warnings.
4. „Geometrie erzeugen“ → 3D-Preview aktualisiert.
5. Optionale Anpassung, erneute Validierung.

### Flow B: Assembly erstellen
1. Komponenten importieren/erstellen.
2. Anchors anzeigen.
3. „Komponente an Anker platzieren“ oder „Anker ausrichten“.
4. Vorschau zeigt Ergebnis, Undo/Redo verfügbar.

### Flow C: Export
1. Projekt-Version wählen.
2. Export-Format bestimmen (STEP/STL).
3. Export erstellen & herunterladen.

### Flow D: Offline & Sync
1. Nutzer arbeitet offline → Aktionen in Queue.
2. UI zeigt „ausstehende Änderungen“ + Konfliktindikator.
3. Bei Online-Status: Sync & Konfliktauflösung (letzte Änderung, manuell).

## 3) Middleware-Plan (Frontend → Backend/Services)

### 3.1 API-Schicht (Client)
- **API-Client Modul** mit klaren Methoden:
  - `createProject`, `fetchProject`, `updateProject`
  - `submitPrompt`, `validateSpec`, `generateGeometry`
  - `listComponents`, `alignComponents`, `exportCad`
- **Beispiel-Endpunkte (REST)**:
  - `POST /projects`, `GET /projects/:id`, `PATCH /projects/:id`
  - `POST /projects/:id/prompt`, `POST /projects/:id/spec/validate`
  - `POST /projects/:id/geometry`, `POST /projects/:id/assembly/align`
  - `POST /projects/:id/export`
- **Request/Response-Models** als TypeScript-Types.
- **Fehlerbehandlung**: standardisierte Fehlerobjekte, UI-Mappings.

### 3.2 State-Management (UI-Middleware)
- **Globaler Store** (z. B. Zustand/Redux Toolkit):
  - `projects`, `currentProject`, `spec`, `geometry`, `assembly`
  - `status` + `errors`
- **Side-Effect Layer**:
  - Async Actions für API-Calls
  - Optimistic Updates, Retry-Mechanismen

### 3.3 Offline-First (PWA Middleware)
- **Service Worker**:
  - Caching für Shell & Assets
  - Stale-While-Revalidate für Projektlisten
- **Sync Queue**:
  - Änderungen sammeln, sobald offline
  - Wiederholung bei Online-Status

### 3.4 Observability & Logging
- **Client Logging**: Konsole + optionaler Remote-Endpoint
- **Tracing**: Pipeline-Schritte mit IDs
- **Telemetry** (optional, opt-in)

### 3.5 Datenkontrakte (Minimal)
- **Project**: `id`, `name`, `description`, `targetFormat`, `status`, `updatedAt`
- **Spec**: `shape`, `dimensions`, `units`, `validation`
- **Geometry**: `id`, `format`, `createdAt`, `previewUrl?`
- **Assembly**: `components[]`, `anchors[]`, `placements[]`

### 3.6 Sicherheits- & Stabilitätsaspekte
- **Input-Sanitizing** für Prompt-Uploads (Länge, Inhalt).
- **Rate-Limits** und Debounce für Validierung/Generierung.
- **Error Boundaries** + Fallback UIs.

## 4) Architekturvorschlag (Frontend)

### 4.1 Tech-Stack (Vorschlag)
- **Framework**: React + Vite + TypeScript
- **Styling**: CSS Modules + design tokens
- **3D**: Three.js (optional React Three Fiber)
- **PWA**: Workbox + Vite-PWA Plugin

### 4.2 Routing (Beispiel)
- `/projects` → Projektliste
- `/projects/:id/editor` → Prompt/Spec/Preview
- `/projects/:id/assembly` → Assembly-Editor
- `/projects/:id/export` → Export-Center
- `/settings` → PWA/Theme/Telemetry

### 4.3 Projektstruktur
```
src/
  app/               # App Entry, Routing, Providers
  features/
    projects/
    prompt/
    spec/
    geometry/
    assembly/
    export/
  components/
  services/          # API, PWA, logging
  store/             # Global state & middleware
  styles/
```

## 5) Qualitätsstrategie (MVP)
- **Unit-Tests**: Store-Reducer, API-Client, Utilities.
- **Integration**: Prompt→Spec→Preview Flow.
- **E2E (später)**: kritische Pfade (Projekt anlegen, exportieren).
- **Performance**: Lighthouse PWA, Bundle-Analyse.

## 6) Nächste Schritte
1. Validierung des Plans & Priorisierung.
2. Wireframes für zentrale Flows (Prompt, Spec, 3D-Preview).
3. Entscheidung für UI-Toolkit/Design-System.
4. Start der Implementierung (PWA-Basis + Projektliste + Prompt/Spec).
