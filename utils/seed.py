import random

letters = "abcdefghijklmnopqrs"


def seed_deviations(stations):
    stations_deviations = []
    for station in stations:
        stations_deviations.append(
            {**station, "deviation": random.randint(-100, 100) / 100}
        )

    return stations_deviations


def seed_loads(stations):
    stations_loads = []
    for station in stations:
        stations_loads.append({**station, "load": random.randint(0, 100)})

    return stations_loads


def seed_stations():
    stations = []
    center_point = [48.766666, 11.433333]
    for i in range(100):
        name = (
            random.choice(letters).upper()
            + random.choice(letters)
            + random.choice(letters) * 2
            + random.choice(letters)
        )
        stations.append(
            {
                "name": name,
                "id": i,
                "lat": center_point[0] + random.randint(-100, 100) / 4000,
                "lon": center_point[1] + random.randint(-100, 100) / 4000,
            }
        )

    return stations
