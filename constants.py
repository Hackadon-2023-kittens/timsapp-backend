import os

project_root = os.path.join(os.path.dirname(os.path.realpath(__file__)))
mock_data_dir = os.path.join(project_root, "mock_data")
deviations_file = os.path.join(mock_data_dir, "deviations.json")
loads_file = os.path.join(mock_data_dir, "loads.json")
