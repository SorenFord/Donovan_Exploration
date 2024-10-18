"""Module to easily access and explore the donovan api endpoints"""

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import pprint
import os
from constants import URL_ENDPOINTS
from pathlib import Path

load_dotenv()

DON_KEY = os.environ.get("DONOVAN_KEY")
basic = HTTPBasicAuth(DON_KEY, "")


def retrieve_data_from_donovan_api(dimension: str):
    """View available api endpoints depending on input.

    Args:
        dimension (str): accepts workspaces, datasets, models
    Output:
        class 'requests.models.Response' object
    """
    api_endpoint = get_api_endpoint(dimension)
    url = f"https://api.donovan.scale.com/v1/{api_endpoint}"

    headers = {"accept": "application/json"}
    if dimension == "models":
        headers["content-type"] = "application/json"

    return requests.get(url, headers=headers, auth=basic)


def get_workspace_from_user():
    return input("Input Workspace: ")


def get_api_endpoint(selected_endpoint_abbv):
    try:
        if selected_endpoint_abbv == "datasets":
            workspace_names = [
                d["name"] for d in retrieve_data_from_donovan_api("workspaces").json()
            ]
            workspace_selection = get_workspace_from_user()
            if workspace_selection not in workspace_names:
                print("Try one of these workspaces: ")
                _name = [print(n) for n in workspace_names]
                workspace_selection = get_workspace_from_user()
            URL_ENDPOINTS["datasets"] = f"workspaces/{workspace_selection}/datasets"
    except KeyError as e:
        print("Sorry. Invalid dimension input. Error {e}")
    return URL_ENDPOINTS[selected_endpoint_abbv]


def create_donovan_workspace():
    url = "https://api.donovan.scale.com/v1/workspaces"

    payload = {"name": "sanderson_demo", "isReadonly": False, "isGlobal": True}
    headers = {"accept": "application/json", "content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, auth=basic)

    print(response.text)


def create_dc_service_request_dataset():
    url = "https://api.donovan.scale.com/v1/datasets"

    payload = {
        "name": "opendata_dc_service_requests",
        "workspace": "sanderson_demo",
        "description": "311 Service Calls in DC Metro area",
        "samplePrompts": [
            "What is the most common 311 service request in the DC Metro Area"
        ],
        "isMultilingual": False,
    }
    headers = {"accept": "application/json", "content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, auth=basic)

    print(response.text)


def add_asset_to_dataset(path_to_local_asset: str, dataset_id: str):
    url = "https://api.donovan.scale.com/v1/upload/local"
    headers = {"accept": "application/json", "content-type": "application/json"} 
    with open(path_to_local_asset, "rb") as file:
        file_data = file.read()

        data = {
            "dataset_id": dataset_id,
            "name": path_to_local_asset.split('/')[-1],
            "file": file_data.decode('utf-8')
            "mimeType": "application/json"
        }
        response = requests.post(
            url, headers=headers, json=data, auth=basic
        )
    return response.json()
