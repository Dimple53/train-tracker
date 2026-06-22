import httpx

IRAIL_BASE = "https://api.irail.be"

async def fetch_stations():
    url = f"{IRAIL_BASE}/stations/?format=json&lang=en"

    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    stations = data.get("station")

    if isinstance(stations, dict):
        stations = [stations]

    return stations

async def fetch_departures(station_id: str):
    url = f"{IRAIL_BASE}/liveboard/"

    params = {
        "id": station_id,
        "format": "json",
        "lang": "en"
    }

    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()