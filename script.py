from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from utils import current_timestamp, transform_values

load_dotenv()

url = os.environ.get('SOLAR_DATA_URL')

try:
    response = requests.get(url)

except requests.exceptions.RequestException as e:
    print("Error: ", e)


if response.status_code == 200:
    # process success
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Find all divs with class "inverter_data"
    inverter_data_divs = soup.find_all('div', class_='inverter_data')

  # Construct dictionary
    data_dict = {}
    for div in inverter_data_divs:
        field = div.find('div', class_='data_field').text.strip()
        value = div.find('div', class_='data_value').text.strip()
        data_dict[field] = value

    keys_to_remove = ['', 'Theme', 'AC Volt', 'AC Frequency', 'Grid Load (W)', 'Grid Load (A)']
    [data_dict.pop(key) for key in keys_to_remove if key in data_dict]

    # cleaning the dict keys
    cleaned_dict = {key.replace(' ', '_').lower(): value for key, value in data_dict.items()}
    # string to numeric conversion
    cleaned_dict = transform_values(cleaned_dict)
    
    # insert current time
    cleaned_dict['local_time'] = current_timestamp()

    client = MongoClient(os.environ.get('DATABASE_URL'))
    db = client.get_database(os.environ.get('DB'))
    collection = db.get_collection(os.environ.get('COLLECTION'))

    # Insert the data dictionary into the MongoDB `collection`
    result = collection.insert_one(cleaned_dict)
    client.close()

    if result.acknowledged:
        print(f"Writing to db successful: {current_timestamp()}")
    else:
        print(f"Failed to push the record {current_timestamp()}")    
else:
    print(f"Couldn't fetch the data successfully, HTTP status: {requests.status_code}, Time: {current_timestamp()}")