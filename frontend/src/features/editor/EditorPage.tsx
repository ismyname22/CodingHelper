import StatusCard from "../../components/StatusCard";
import styles from "./EditorPage.module.css";

const EditorPage = () => {
  return (
    <section className={styles.layout}>
      <div className={styles.split}>
        <div className={styles.panel}>
          <header>
            <h2>Prompt &amp; Spezifikation</h2>
            <p>Formuliere die Geometrie-Anfrage und überprüfe die Spec-Details.</p>
          </header>
          <div className={styles.promptCard}>
            <label htmlFor="prompt">Prompt</label>
            <textarea
              id="prompt"
              rows={6}
              defaultValue="Erstelle eine Box 40x20x10mm mit abgerundeten Kanten."
            />
            <div className={styles.actions}>
              <button className={styles.secondaryButton}>Validieren</button>
              <button className={styles.primaryButton}>Geometrie erzeugen</button>
            </div>
          </div>
          <StatusCard
            title="Spec-Validierung"
            description="Keine Fehler gefunden. Einheiten: mm · Shape: box"
            meta="Letzter Lauf vor 2 Min"
            tone="success"
          />
        </div>
        <div className={styles.previewPanel}>
          <header>
            <h2>3D-Vorschau</h2>
            <p>Bounding-Box, Anchors und Messwerkzeuge auf einen Blick.</p>
          </header>
          <div className={styles.previewBox}>
            <div>
              <h3>WebGL Preview</h3>
              <p>3D-Ansicht wird nach der Geometrie-Generierung aktualisiert.</p>
            </div>
            <ul>
              <li>Grid: Aktiv</li>
              <li>Anchors: 6 sichtbar</li>
              <li>Bounding Box: 40×20×10 mm</li>
            </ul>
          </div>
          <div className={styles.metrics}>
            <StatusCard
              title="Messwerte"
              description="X: 40mm · Y: 20mm · Z: 10mm"
              meta="Workplane"
            />
            <StatusCard
              title="Letzte Aktion"
              description="Geometrie erzeugt · 12s"
              meta="Timeline"
              tone="info"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default EditorPage;
