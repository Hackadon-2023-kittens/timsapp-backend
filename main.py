from flask import Flask
from utils.seed import seed
from constants import mock_data_dir, deviations_file, loads_file
import json
from flask_cors import CORS

seed(mock_data_dir, deviations_file, loads_file)

app = Flask(__name__)
CORS(app)


@app.route("/deviations")
def deviations():
    with open(deviations_file) as f:
        deviations = json.load(f)
    return deviations


@app.route("/loads")
def loads():
    with open(loads_file) as f:
        loads = json.load(f)
    return loads


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
