# Requests is used to get data from the compcon API and then amazon buckets
import requests
from bot.utils.constants import CONST

# The API key woot woot
compcon_headers = {
    "x-api-key": CONST.COMPCON_API_KEY
}

# Our method to get a character from the compcon API by its share code
def get_character_by_code(share_code):

    # Query the compcon API to get the bucket the character is stored in
    query_url = CONST.COMPCON_URL + "/share"
    response = requests.get(query_url, params = {"code": share_code}, headers=compcon_headers, timeout=2)
    if response.status_code == 200:
        return query_character_bucket(response.json()["presigned"])
    else:
        return {"error": f"response failed with code {response.status_code}: {response.text}"}

# Our method to query the amazon bucket when we get it
def query_character_bucket(url):

    # Query the bucket and return the character in the desired format
    response = requests.get(url, timeout=2)
    if response.status_code == 200: 
        return response.json()["name"]
    else:
        return {"error": f"response failed with code {response.status_code}: {response.text}"}
