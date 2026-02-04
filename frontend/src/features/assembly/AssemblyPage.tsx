import StatusCard from "../../components/StatusCard";
import styles from "./AssemblyPage.module.css";

const AssemblyPage = () => {
  return (
    <section className={styles.layout}>
      <div className={styles.headerRow}>
        <div>
          <h2>Assembly-Editor</h2>
          <p>Platziere Komponenten an Anchors und prüfe die Alignment-Historie.</p>
        </div>
        <div className={styles.actions}>
          <button className={styles.secondaryButton}>Undo</button>
          <button className={styles.secondaryButton}>Redo</button>
          <button className={styles.primaryButton}>Anker ausrichten</button>
        </div>
      </div>
      <div className={styles.grid}>
        <div className={styles.column}>
          <StatusCard
            title="Komponenten"
            description="4 Bauteile aktiv · 2 warten auf Import"
            meta="Liste"
          />
          <div className={styles.listCard}>
            <h3>Anchors</h3>
            <ul>
              <li>base · center</li>
              <li>base · face_zmax</li>
              <li>bracket · face_zmin</li>
              <li>bracket · face_xmin</li>
            </ul>
          </div>
        </div>
        <div className={styles.column}>
          <div className={styles.previewCard}>
            <h3>Placement Preview</h3>
            <p>Komponenten werden auf der Vorschau ausgerichtet.</p>
            <div className={styles.previewPlaceholder}>
              3D-Assembly Vorschau
            </div>
          </div>
          <StatusCard
            title="Alignment-Historie"
            description="5 Schritte · Letzte Änderung vor 10 Min"
            meta="Timeline"
            tone="info"
          />
        </div>
      </div>
    </section>
  );
};

export default AssemblyPage;
