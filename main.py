import requests
import pandas as pd
import plotly.express as px
from demo3 import *
from io import StringIO
import json

STATE_DATA_URL = "https://rawcdn.githack.com/TabassumNova/graph_generate_ex2py/4ee8202a0ceb5a6fa46744217b4ae4b06c8d0375/"
STATE_DATA_URL0 = "https://raw.githubusercontent.com/CITF-Malaysia/citf-public/main/vaccination/vax_state.csv"


# https://rawcdn.githack.com/TabassumNova/graph_generate_ex2py/4ee8202a0ceb5a6fa46744217b4ae4b06c8d0375/dataset/003_005_010_037_061/trajectory/000000.json
# https://rawcdn.githack.com/TabassumNova/graph_generate_ex2py/4ee8202a0ceb5a6fa46744217b4ae4b06c8d0375/dataset/003_004_024_025_061/trajectory/000000.json
def fetch_csv(data_url: str) -> pd.DataFrame:
    t = requests.get(data_url).text
    return pd.read_csv(StringIO(requests.get(data_url).text))

def fetch_json(data_url: str):
    response = requests.get(data_url)
    json_response = json.loads(response.text)
    return json_response

# if __name__ == "__main__":
#     state_data = fetch_json(STATE_DATA_URL)
#     state_data0 = fetch_csv(STATE_DATA_URL0)
#     pass



#
if __name__ == "__main__":
    layout = plot_scenewise(file_location=STATE_DATA_URL ,plotly_viz=True)
    layout.write_html('demo3.html', include_plotlyjs='cdn')
