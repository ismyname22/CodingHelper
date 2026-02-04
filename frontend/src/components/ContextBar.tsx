import styles from "./ContextBar.module.css";

type ContextBarProps = {
  projectName: string;
  statusLabel: string;
  validationLabel: string;
  syncLabel: string;
};

const ContextBar = ({ projectName, statusLabel, validationLabel, syncLabel }: ContextBarProps) => {
  return (
    <section className={styles.contextBar}>
      <div>
        <span className={styles.eyebrow}>Aktives Projekt</span>
        <h2>{projectName}</h2>
      </div>
      <div className={styles.statusGroup}>
        <span className={styles.badge}>{statusLabel}</span>
        <span className={styles.badge}>{validationLabel}</span>
        <span className={styles.badgeMuted}>{syncLabel}</span>
      </div>
    </section>
  );
};

export default ContextBar;
