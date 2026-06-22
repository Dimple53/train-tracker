import { useState } from "react";
import { fetchDepartures } from "./api";
import DeparturesTable from "./components/DeparturesTable";
import styles from "./App.module.css";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const search = async () => {
    if (query.trim().length < 3) {
      setError("Enter at least 3 characters");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const data = await fetchDepartures(query);
      setResult(data);
    } catch (e) {
      setError(e.message);
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") search();
  };

  return (
    <div className={styles.page}>
      <div className={styles.container}>

        {/* TITLE */}
        <h1 className={styles.title}>🚆 Lagovia Train Tracker</h1>
        <p className={styles.subtitle}>
          Search real-time train departures
        </p>

        {/* SEARCH */}
        <div className={styles.searchBox}>
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search station (e.g. Bru)"
            className={styles.input}
          />

          <button onClick={search} className={styles.button}>
            Search
          </button>
        </div>

        {/* STATES */}
        {error && <div className={styles.error}>{error}</div>}
        {loading && <div className={styles.loading}>Loading...</div>}

        {/* META */}
        {result && (
          <div className={styles.meta}>
            <span>Stations: {result.stations_found}</span>
            <span>Departures: {result.departures_count}</span>
          </div>
        )}

        {/* RESULTS */}
        <DeparturesTable data={result?.departures || []} />

      </div>
    </div>
  );
}

export default App;

