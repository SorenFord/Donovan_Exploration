"""Functions for chatting with LLM models"""
import requests
from donovan_interaction import basic
from constants import *
import openai
import geopandas as gpd
import os
from dotenv import load_dotenv

def chat_with_dc_data(prompt: str, dataset_id: str):
    url = "https://api.donova.scale.com/v1/chat"
    payload = {
        "modelType": "SCALE_LLAMA_2_13B_CHAT",
        "text": "Describe the ",
        "workspace": workspace_name,
        "datasets": [dataset_id],
    }
    headers = {"accept": "application/json", "content-type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, auth=basic)


def analyze_data(prompt: str, data: pd.DataFrame):
    results = []
    for index, row in data.iterrows():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"{prompt}: {data}"}],
        )
        results.append(response["choices"][0]["message"]["content"])

    # Now results contain the analysis for each description in your GeoJSON
    print(results)


def run_analysis_on_services_by_ward(prompt:str):
    openai.api_key = os.environ.get("OPENAI_KEY")
    gdf = gpd.read_file("./311_City_Service_Requests_in_2024.geojson")
    service_by_ward = gdf[["SERVICECODEDESCRIPTION", "WARD"]]
    output = analyze_data(prompt, service_by_ward)
    return output


if __name__ == "__main__":
    load_dotenv()
    print(run_analysis_on_services_by_ward())
