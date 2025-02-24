import os
import json
import time
import argparse
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from requests.structures import CaseInsensitiveDict

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def setup_chrome_driver(options):
    service = Service(executable_path='/path/to/chromedriver')  # Update this path
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver, config):
    driver.get('https://www.reddit.com/login')
    time.sleep(2)
    driver.find_element(By.ID, 'loginUsername').send_keys(config['reddit']['username'])
    driver.find_element(By.ID, 'loginPassword').send_keys(config['reddit']['password'])
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

def fetch_posts(config, headers, delay):
    url = f"https://oauth.reddit.com/r/{config['subreddit']}/new"
    response = requests.get(url, headers=headers)
    data = response.json()
    posts = []
    for post in data['data']['children']:
        posts.append(post['data'])
        time.sleep(delay)
    return posts

def fetch_comments(config, headers, posts, delay):
    comments = []
    for post in posts:
        post_id = post['id']
        comment_url = f"https://oauth.reddit.com/r/{config['subreddit']}/comments/{post_id}.json"
        response = requests.get(comment_url, headers=headers)
        comment_data = response.json()
        for comment in comment_data[1]['data']['children']:
            comments.append(comment['data'])
            time.sleep(delay)
    return comments

def store_data_in_mongo(client, posts, comments):
    db = client[config['mongoDB']['db_name']]
    posts_collection = db['posts']
    comments_collection = db['comments']
    posts_collection.insert_many(posts)
    comments_collection.insert_many(comments)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type=str, help="path to the JSON configuration file.")
    args = parser.parse_args()

    config = load_config(args.config_path)

    mongo_uri = config['mongoDB']['uri']
    client = MongoClient(mongo_uri)

    options = Options()
    options.add_argument("--headless")
    driver = setup_chrome_driver(options)
    login(driver, config)

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = config['fetch_headers']['User-Agent']
    headers["Authorization"] = f"bearer {config['fetch_headers']['Authorization']}"

    delays = config['delays']

    posts = fetch_posts(config, headers, delays['post'])
    comments = fetch_comments(config, headers, posts, delays['comment'])

    store_data_in_mongo(client, posts, comments)

    driver.quit()

if __name__ == "__main__":
    main()
