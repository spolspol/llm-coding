import argparse
import json
import logging
import time
from jsonschema import validate, ValidationError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Configure logging
logging.basicConfig(filename='reddit_clone_fetcher.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# JSON schema for configuration validation
JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "reddit": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "login": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "password": {"type": "string"}
                    },
                    "required": ["username", "password"]
                }
            },
            "required": ["url", "login"]
        },
        "mongodb": {
            "type": "object",
            "properties": {
                "uri": {"type": "string"},
                "database": {"type": "string"},
                "collection": {"type": "string"}
            },
            "required": ["uri", "database", "collection"]
        }
    },
    "required": ["reddit", "mongodb"]
}

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        validate(instance=config, schema=JSON_SCHEMA)
        return config
    except FileNotFoundError as e:
        logging.error(f"Configuration file not found: {e}")
        raise
    except ValidationError as e:
        logging.error(f"Configuration validation error: {e}")
        raise

def parse_arguments():
    parser = argparse.ArgumentParser(description='Reddit clone data fetcher')
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file')
    return parser.parse_args()

class WebScraper:
    def __init__(self, config):
        self.config = config
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(), options=self.chrome_options)
        self.mongo_client = MongoClient(self.config['mongodb']['uri'])
        self.db = self.mongo_client[self.config['mongodb']['database']]
        self.collection = self.db[self.config['mongodb']['collection']]

    def login(self):
        try:
            self.driver.get(self.config['reddit']['url'])
            time.sleep(2)
            username_field = self.driver.find_element(By.ID, 'loginUsername')
            password_field = self.driver.find_element(By.ID, 'loginPassword')
            login_button = self.driver.find_element(By.XPATH, '//button[text()="Log in"]')
            username_field.send_keys(self.config['reddit']['login']['username'])
            password_field.send_keys(self.config['reddit']['login']['password'])
            login_button.click()
            time.sleep(5)  # Wait for login to complete
        except Exception as e:
            logging.error(f"Login failed: {e}")
            self.driver.quit()
            raise

    def fetch_data(self):
        try:
            self.driver.get(self.config['reddit']['url'])
            time.sleep(5)  # Wait for page to load
            posts = self.driver.find_elements(By.CLASS_NAME, 'Post')
            data = []
            for post in posts:
                title = post.find_element(By.CLASS_NAME, 'title').text
                comments = post.find_element(By.CLASS_NAME, 'comments').text
                data.append({'title': title, 'comments': comments})
            return data
        except Exception as e:
            logging.error(f"Data fetching failed: {e}")
            return []

    def store_data(self, data):
        try:
            if data:
                self.collection.insert_many(data)
                logging.info(f"Stored {len(data)} documents in MongoDB")
        except PyMongoError as e:
            logging.error(f"Data storage failed: {e}")

    def run(self):
        self.login()
        data = self.fetch_data()
        self.store_data(data)
        self.driver.quit()
        self.mongo_client.close()

def main():
    args = parse_arguments()
    config = load_config(args.config)
    scraper = WebScraper(config)
    scraper.run()

if __name__ == '__main__':
    main()
