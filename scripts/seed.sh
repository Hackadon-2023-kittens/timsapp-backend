SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
MOCK_DATA=$SCRIPT_DIR/../mock_data 
python ./utils/seed.py $MOCK_DATA $MOCK_DATA/deviations.json $MOCK_DATA/loads.json
