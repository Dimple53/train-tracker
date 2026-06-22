import styles from "./DeparturesTable.module.css";

export default function DeparturesTable({ data }) {
  if (!data || data.length === 0) {
    return <p className={styles.noResults}>No departures found</p>;
  }

  return (
    <div className={styles.grid}>
      {data.map((d, i) => {
        const delay = Number(d.delayMinutes || 0);

        const status = d.cancelled
          ? "Cancelled"
          : delay > 0
          ? `Delayed (${delay} min)`
          : "On time";

        const statusClass = d.cancelled
          ? styles.statusCancelled
          : delay > 0
          ? styles.statusDelayed
          : styles.statusOnTime;

        return (
          <div key={i} className={styles.card}>
            <div className={styles.top}>
              <strong>{d.station}</strong>

              <span className={styles.trainNumber}>
                {d.trainNumber}
              </span>
            </div>

            <div className={styles.row}>
              <span>➡️ {d.destination}</span>
              <span>
                {new Date(d.scheduledTime).toLocaleTimeString([], {
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </span>
            </div>

            <div className={styles.row}>
              <span>Delay: {delay} min</span>

              <span className={statusClass}>
                {status}
              </span>
            </div>
          </div>
        );
      })}
    </div>
  );
}