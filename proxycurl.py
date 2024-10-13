import requests
import json

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

# Replace with your actual API key
headers = {"Authorization": "Bearer " + os.environ["PROXYCURL_API_KEY"]}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

params = {
    "linkedin_profile_url": "https://linkedin.com/in/muffafa/"  # Modify the LinkedIn profile URL if needed
}

# Make the API request
response = requests.get(api_endpoint, params=params, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    # Parse the response content as JSON
    data = response.json()

    # Save the data to a JSON file in the current working directory
    with open("data2.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Data has been successfully saved to data2.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
