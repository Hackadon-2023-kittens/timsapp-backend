import os
import random
import json


def seed(mock_data_dir, deviations_file, loads_file):
    if os.path.exists(mock_data_dir):
        return

    os.mkdir(mock_data_dir)

    stations = []
    center_point = [48.766666, 11.433333]
    for i in range(20):
        stations.append(
            {
                "lat": center_point[0] + random.randint(-100, 100) / 10000,
                "lon": center_point[1] + random.randint(-100, 100) / 10000,
            }
        )

    stations_deviations = []
    for station in stations:
        stations_deviations.append(
            {**station, "deviation": random.randint(-100, 100) / 100}
        )

    with open(deviations_file, "w", encoding="utf-8") as f:
        json.dump(stations_deviations, f, ensure_ascii=False, indent=4)

    stations_loads = []
    for station in stations:
        stations_loads.append({**station, "load": random.randint(0, 100)})

    with open(loads_file, "w", encoding="utf-8") as f:
        json.dump(stations_loads, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    import sys

    seed(sys.argv[1], sys.argv[2], sys.argv[3])
