from fastapi import FastAPI, HTTPException
from services import search_stations, get_departures_for_station

app = FastAPI(title="Lagovia Train Tracker")

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/departures")
async def get_departures(q: str):

    if len(q) < 3:
        raise HTTPException(
            status_code=400,
            detail="Query must be at least 3 characters"
        )

    stations = await search_stations(q)

    all_departures = []

    for station in stations:
        deps = await get_departures_for_station(station)
        all_departures.extend(deps)

    return {
        "query": q,
        "stations_found": len(stations),
        "departures_count": len(all_departures),
        "departures": all_departures
    }