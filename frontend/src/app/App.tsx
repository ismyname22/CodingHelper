import { NavLink, Route, Routes } from "react-router-dom";
import ContextBar from "../components/ContextBar";
import AssemblyPage from "../features/assembly/AssemblyPage";
import EditorPage from "../features/editor/EditorPage";
import ExportPage from "../features/export/ExportPage";
import ProjectsPage from "../features/projects/ProjectsPage";
import SettingsPage from "../features/settings/SettingsPage";
import styles from "./App.module.css";

const App = () => {
  return (
    <div className={styles.appShell}>
      <aside className={styles.sidebar}>
        <div className={styles.brand}>CodingHelper</div>
        <nav className={styles.nav}>
          <NavLink to="/projects" className={({ isActive }) => (isActive ? styles.active : styles.link)}>
            Projekte
          </NavLink>
          <NavLink to="/editor" className={({ isActive }) => (isActive ? styles.active : styles.link)}>
            Editor
          </NavLink>
          <NavLink to="/assembly" className={({ isActive }) => (isActive ? styles.active : styles.link)}>
            Assembly
          </NavLink>
          <NavLink to="/export" className={({ isActive }) => (isActive ? styles.active : styles.link)}>
            Export
          </NavLink>
          <NavLink to="/settings" className={({ isActive }) => (isActive ? styles.active : styles.link)}>
            Einstellungen
          </NavLink>
        </nav>
        <div className={styles.sidebarFooter}>
          <span className={styles.statusDot} />
          Offline-fähig
        </div>
      </aside>
      <main className={styles.main}>
        <header className={styles.header}>
          <div>
            <h1>Frontend Workspace</h1>
            <p>Projektstatus, Validierung &amp; Sync-Infos auf einen Blick.</p>
          </div>
          <div className={styles.headerMeta}>
            <span className={styles.metaTag}>Pipeline: Idle</span>
            <span className={styles.metaTag}>Sync: Online</span>
          </div>
        </header>
        <ContextBar
          projectName="Laserhalterung"
          statusLabel="Status: In Bearbeitung"
          validationLabel="Validierung: OK"
          syncLabel="Offline-Queue: 2"
        />
        <Routes>
          <Route path="/" element={<ProjectsPage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/editor" element={<EditorPage />} />
          <Route path="/assembly" element={<AssemblyPage />} />
          <Route path="/export" element={<ExportPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </main>
    </div>
  );
};

export default App;
