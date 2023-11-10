from flask import Flask
from utils.seed import seed_stations, seed_deviations, seed_loads
from flask_cors import CORS

stations = seed_stations()

app = Flask(__name__)
CORS(app)


@app.route("/deviations")
def deviations():
    return seed_deviations(stations)


@app.route("/loads")
def loads():
    return seed_loads(stations)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
