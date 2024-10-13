import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()


def linkedin_profile_json():
    """Return the data of a LinkedIn profile from local data.json file."""

    # Get the data from the local data.json file
    with open("data2.json", "r") as f:
        data = json.load(f)

        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }

        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        # Return the data
        return data


if __name__ == "__main__":
    print(linkedin_profile_json())
