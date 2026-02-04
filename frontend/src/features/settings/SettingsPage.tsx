import StatusCard from "../../components/StatusCard";
import styles from "./SettingsPage.module.css";

const SettingsPage = () => {
  return (
    <section className={styles.layout}>
      <div className={styles.headerRow}>
        <div>
          <h2>Einstellungen</h2>
          <p>PWA-Status, Theme und Telemetrie steuern.</p>
        </div>
        <button className={styles.primaryButton}>Änderungen speichern</button>
      </div>
      <div className={styles.grid}>
        <div className={styles.card}>
          <h3>PWA &amp; Offline</h3>
          <p>Service Worker aktiv · Cache zuletzt vor 5 Minuten aktualisiert.</p>
          <div className={styles.toggleRow}>
            <span>Offline-Modus</span>
            <button className={styles.toggle}>Aktiv</button>
          </div>
        </div>
        <div className={styles.card}>
          <h3>Theme</h3>
          <p>Wähle zwischen hellem und dunklem Design.</p>
          <div className={styles.toggleRow}>
            <span>Dark Mode</span>
            <button className={styles.toggle}>Aus</button>
          </div>
        </div>
        <div className={styles.card}>
          <h3>Telemetry</h3>
          <p>Fehlerberichte und Performance-Metriken teilen.</p>
          <div className={styles.toggleRow}>
            <span>Opt-in</span>
            <button className={styles.toggleSecondary}>Optional</button>
          </div>
        </div>
      </div>
      <div className={styles.statusRow}>
        <StatusCard
          title="Sync-Queue"
          description="Keine ausstehenden Änderungen."
          meta="0 Items"
          tone="success"
        />
        <StatusCard
          title="Accessibility"
          description="Kontrastprüfung aktiv · Schriftgröße normal."
          meta="AA"
        />
      </div>
    </section>
  );
};

export default SettingsPage;
