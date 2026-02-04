import styles from "./StatusCard.module.css";

type StatusCardProps = {
  title: string;
  description: string;
  meta?: string;
  tone?: "info" | "success" | "warning";
};

const StatusCard = ({ title, description, meta, tone = "info" }: StatusCardProps) => {
  return (
    <article className={styles.card} data-tone={tone}>
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
      {meta ? <span className={styles.meta}>{meta}</span> : null}
    </article>
  );
};

export default StatusCard;
