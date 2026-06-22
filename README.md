# Lagovia Train Tracker

A simple train departure tracker built for the DPS Technical Challenge.

## Tech Stack

### Backend
- Python 3.14.6
- FastAPI
- httpx

### Frontend
- React
- Vite

## Features

- Search stations by partial name
- Minimum 3-character validation
- Retrieves departures from iRail API
- Shows departures within the next 15 minutes
- Displays:
  - Station
  - Train Number
  - Destination
  - Scheduled Departure Time
  - Delay Minutes
  - Cancelled Status

## Screenshots

### Search Screen

![Search Screen](screenshots/search_page.png)

### Results Screen

![Results Screen](screenshots/results_page1.png)
![Results Screen](screenshots/results_page2.png)

## Project Structure

train-tracker/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── irail.py
│   │   └── services.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── components/
│   │       └── DeparturesTable.jsx
│   └── package.json
│
├── README.md
└── AI_USAGE.md

## Running Locally

### Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

fastapi dev app/main.py
```

Backend runs on:

http://localhost:8000

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

http://localhost:5173

---

## API

### Endpoint

```http
GET /departures?q=Bru
```

### Query Parameters

| Parameter | Type | Required | Description |
|------------|--------|----------|-------------|
| q | string | Yes | Station name substring to search for |

### Validation

Queries shorter than 3 characters return an error response.

Example:

```http
GET /departures?q=Br
```

Response:

```json
{
  "detail": "Query must be at least 3 characters long"
}
```

### Example Response

```json
{
  "query": "Bru",
  "stations_found": 16,
  "departures_count": 10,
  "departures": [
    {
      "station": "Brugge",
      "trainNumber": "BE.NMBS.IC1818",
      "destination": "Antwerp-Central",
      "scheduledTime": "2025-06-21T16:25:00+00:00",
      "delayMinutes": 0,
      "cancelled": false
    }
  ]
}
```

---

## Design Decisions

### FastAPI Backend

I chose FastAPI because it is lightweight, easy to develop with, and provides automatic API documentation through Swagger UI.

### React Frontend

React was selected because it is widely used, simple to integrate with REST APIs, and aligns with the preferred technology stack mentioned in the challenge.

### Station Caching

The station list is loaded once from the iRail API and cached in memory. This reduces unnecessary network requests and improves response times.

### Departure Filtering

The iRail API may return many departures. To satisfy the challenge requirements, departures are filtered to only include trains departing within the next 15 minutes.

### Error Handling

The API validates user input and returns a clear error message when the search query is shorter than three characters.

---

## Assumptions

- Station matching is performed using case-insensitive substring search.
- Time calculations are performed using UTC timestamps returned by the iRail API.
- Only upcoming departures within the next 15 minutes are included in results.

---

## Known Limitations

- No fuzzy matching is implemented.
- Station data is stored in memory and is refreshed only when the backend restarts.
- No pagination is implemented for large result sets.
- UI is intentionally simple and focused on functionality.

---

## Future Improvements

- Add fuzzy search support (e.g. "Antverpen" → "Antwerpen-Centraal").
- Add loading skeletons and improved user feedback.
- Group departures by station in the UI.
- Add automated tests.
- Deploy backend and frontend to cloud platforms.

---

## Data Source

This project uses the public iRail API:

https://docs.irail.be/

---

## Author

Created as part of the DPS Technical Challenge.