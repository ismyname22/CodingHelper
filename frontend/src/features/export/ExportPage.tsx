import StatusCard from "../../components/StatusCard";
import styles from "./ExportPage.module.css";

const ExportPage = () => {
  return (
    <section className={styles.layout}>
      <div className={styles.headerRow}>
        <div>
          <h2>Export-Center</h2>
          <p>Wähle Format, Version und starte den Export.</p>
        </div>
        <button className={styles.primaryButton}>Export erstellen</button>
      </div>
      <div className={styles.grid}>
        <div className={styles.card}>
          <h3>Format</h3>
          <div className={styles.optionRow}>
            <span>STEP</span>
            <span className={styles.badge}>Bevorzugt</span>
          </div>
          <div className={styles.optionRow}>
            <span>STL</span>
            <span className={styles.badgeSecondary}>Mesh</span>
          </div>
        </div>
        <div className={styles.card}>
          <h3>Revisionen</h3>
          <ul>
            <li>v1.2 · Kantenradien angepasst</li>
            <li>v1.1 · Anchors ergänzt</li>
            <li>v1.0 · Erste Geometrie</li>
          </ul>
        </div>
        <div className={styles.card}>
          <h3>Download</h3>
          <p>Export bereitstellen oder Link teilen.</p>
          <div className={styles.actions}>
            <button className={styles.secondaryButton}>Datei laden</button>
            <button className={styles.secondaryButton}>Link teilen</button>
          </div>
        </div>
      </div>
      <div className={styles.statusRow}>
        <StatusCard
          title="Export-Queue"
          description="1 Export in Arbeit · ETA 3 Minuten"
          meta="In Bearbeitung"
          tone="warning"
        />
        <StatusCard
          title="Versionsvergleich"
          description="Differenzen werden automatisch hervorgehoben."
          meta="Aktiv"
        />
      </div>
    </section>
  );
};

export default ExportPage;
