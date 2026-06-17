

import logging
import requests
import time

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("/Users/kaviya/Desktop/w3schools.log"),
        logging.StreamHandler()
    ]
)

def fetch_from_url(url,max_attempt,delay):

    for i in range(1,max_attempt +1):

        try:
            logging.info(f"attemp:{i},api call started..")
            response=requests.get(url,timeout=10)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.Timeout as e:
            logging.error(f"timeout exception in attemp - {i}")

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error in attempt - {i}")

        except requests.exceptions.ConnectionError as e:
            logging.error(f"API connection Failed in attempt - {i}")

        if i < max_attempt:
            logging.warning(f"{i} st attempt of {max_attempt}, waiting {delay} seconds before retry..")
            time.sleep(delay)
        
    logging.error(f"all {max_attempt} attempt failed...")
    return []

data = fetch_from_url("https://jsonplaceholder.typicode.com/users", 3,2)

if data :
    print(data)
    logging.info("api call ended..successfully !")




    


