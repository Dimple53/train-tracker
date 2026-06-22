from irail import fetch_stations, fetch_departures
from datetime import datetime, timedelta, timezone


_cached_stations = None
async def get_stations():
    global _cached_stations

    if _cached_stations is None:
        _cached_stations = await fetch_stations()

    return _cached_stations

async def search_stations(query: str):
    stations = await get_stations()

    q = query.lower()

    return [
        s
        for s in stations
        if q in s.get("standardname", "").lower()
        or q in s.get("name", "").lower()
    ]

def convert_departure(dep, station_name):
    return {
        "station": station_name,
        "trainNumber": dep.get("vehicle"),
        "destination": dep.get("station"),
        "scheduledTime": datetime.fromtimestamp(
    int(dep.get("time")),
    tz=timezone.utc
).isoformat(),
        "delayMinutes": int(dep.get("delay", 0)) // 60,
        "cancelled": dep.get("canceled") == 1
    }

def is_within_15_minutes(dep_time):
    now = datetime.now(timezone.utc)
    return now <= dep_time <= now + timedelta(minutes=15)
async def get_departures_for_station(station):
    raw = await fetch_departures(station["id"])

    departures = raw.get("departures", {}).get("departure", [])

    results = []

    # for dep in departures:
    #     scheduled = datetime.fromtimestamp(int(dep["time"]), tz=timezone.utc)
    #     if is_within_15_minutes(scheduled):
    #         results.append(convert_departure(dep, station["name"]))

    # for dep in departures:
    #   scheduled = datetime.fromtimestamp(
    #       int(dep["time"]),
    #       tz=timezone.utc
    #   )

    #   now = datetime.now(timezone.utc)
    #   diff_minutes = (scheduled - now).total_seconds() / 60

    #   print(
    #       f"Station={station['name']}, "
    #       f"Departure={scheduled.isoformat()}, "
    #       f"Now={now.isoformat()}, "
    #       f"Diff={diff_minutes:.2f} minutes"
    #   )

    #   if is_within_15_minutes(scheduled):
    #       print("KEEPING")
    #       results.append(convert_departure(dep, station["name"]))
    #   else:
    #       print("SKIPPING")

    for dep in departures:
      scheduled = datetime.fromtimestamp(int(dep["time"]), tz=timezone.utc)
      now = datetime.now(timezone.utc)

      diff = (scheduled - now).total_seconds() / 60

      if is_within_15_minutes(scheduled):
          results.append(convert_departure(dep, station["name"]))
      else:
          print("SKIP:", station["name"], diff)

    return results

   