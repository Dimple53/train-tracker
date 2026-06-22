export async function fetchDepartures(query) {
  const res = await fetch(
    `http://127.0.0.1:8000/departures?q=${query}`
  );

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Request failed");
  }

  return res.json();
}