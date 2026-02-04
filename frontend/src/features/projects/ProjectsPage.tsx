import StatusCard from "../../components/StatusCard";
import styles from "./ProjectsPage.module.css";

const projects = [
  {
    name: "Laserhalterung",
    description: "Letztes Update vor 3 Stunden · Ziel: STEP",
    status: "Validierung läuft",
  },
  {
    name: "Halterung V2",
    description: "Neu angelegt · Ziel: STL",
    status: "Bereit für Prompt",
  },
  {
    name: "Montageplatte",
    description: "Synchronisiert · Ziel: STEP",
    status: "Pipeline erfolgreich",
  },
];

const ProjectsPage = () => {
  return (
    <section className={styles.layout}>
      <div className={styles.hero}>
        <div>
          <h2>Projekte</h2>
          <p>Verwalte deine CAD-Projekte, Tags und Export-Formate.</p>
        </div>
        <button className={styles.primaryButton}>Projekt erstellen</button>
      </div>
      <div className={styles.grid}>
        {projects.map((project) => (
          <StatusCard
            key={project.name}
            title={project.name}
            description={project.description}
            meta={project.status}
            tone={project.status === "Pipeline erfolgreich" ? "success" : "info"}
          />
        ))}
      </div>
      <div className={styles.secondaryGrid}>
        <StatusCard
          title="Offline Queue"
          description="2 Aktionen warten auf Synchronisierung, sobald du wieder online bist."
          meta="2 Items"
          tone="warning"
        />
        <StatusCard
          title="Validierungsrichtlinien"
          description="Spezifikationen werden automatisch auf Maßeinheiten geprüft."
          meta="Aktiv"
        />
      </div>
    </section>
  );
};

export default ProjectsPage;
