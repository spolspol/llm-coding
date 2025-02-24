# config.py
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "reddit_clone"
LOGIN_CREDENTIALS = {"username": "your_username", "password": "your_password"}
BROWSER_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# mongodb_manager.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import logging

class MongoDBManager:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.posts_collection = None
        self.comments_collection = None
        self._setup_connection()

    def _setup_connection(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.posts_collection = self.db['posts']
            self.comments_collection = self.db['comments']
            logging.info("Connected to MongoDB")
        except ConnectionFailure as e:
            logging.error(f"Could not connect to MongoDB: {e}")
            raise

    def insert_post(self, post_data):
        try:
            self.posts_collection.insert_one(post_data)
            logging.info("Post inserted successfully")
        except OperationFailure as e:
            logging.error(f"Failed to insert post: {e}")
            raise

    def insert_comment(self, comment_data):
        try:
            self.comments_collection.insert_one(comment_data)
            logging.info("Comment inserted successfully")
        except OperationFailure as e:
            logging.error(f"Failed to insert comment: {e}")
            raise

# selenium_manager.py
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import random
import logging

class SeleniumManager:
    def __init__(self, login_credentials, headers):
        self.login_credentials = login_credentials
        self.headers = headers
        self.driver = None
        self._setup_driver()

    def _setup_driver(self):
        try:
            self.driver = webdriver.Chrome()
            logging.info("Selenium driver started")
        except WebDriverException as e:
            logging.error(f"Failed to start driver: {e}")
            raise

    def login(self):
        try:
            self.driver.get("https://www.reddit.com/login")
            time.sleep(random.randint(2, 4))
            username_field = self.driver.find_element_by_id("loginUsername")
            password_field = self.driver.find_element_by_id("loginPassword")
            login_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
            username_field.send_keys(self.login_credentials["username"])
            password_field.send_keys(self.login_credentials["password"])
            login_button.click()
            time.sleep(random.randint(5, 7))
            logging.info("Logged in to Reddit")
        except Exception as e:
            logging.error(f"Failed to login: {e}")
            raise

    def fetch_user_posts(self, username):
        try:
            self.driver.get(f"https://www.reddit.com/user/{username}/submitted/")
            time.sleep(random.randint(3, 5))
            posts = self.driver.find_elements_by_css_selector('div.Post')
            return [post.text for post in posts]
        except Exception as e:
            logging.error(f"Failed to fetch user posts: {e}")
            raise

    def fetch_user_comments(self, username):
        try:
            self.driver.get(f"https://www.reddit.com/user/{username}/comments/")
            time.sleep(random.randint(3, 5))
            comments = self.driver.find_elements_by_css_selector('div.Comment')
            return [comment.text for comment in comments]
        except Exception as e:
            logging.error(f"Failed to fetch user comments: {e}")
            raise

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            logging.info("Driver closed")

# utils.py
import random
import time

def random_delay(min_sec=2, max_sec=5):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

# reddit_fetcher.py
import logging
from selenium_manager import SeleniumManager
from mongodb_manager import MongoDBManager
from utils import random_delay

class RedditFetcher:
    def __init__(self, selenium_manager, mongodb_manager):
        self.selenium_manager = selenium_manager
        self.mongodb_manager = mongodb_manager

    def start_fetching(self, username):
        self.selenium_manager.login()
        posts = self.selenium_manager.fetch_user_posts(username)
        comments = self.selenium_manager.fetch_user_comments(username)
        self.selenium_manager.close_driver()
        self.store_data(posts, comments)

    def store_data(self, posts, comments):
        for post in posts:
            self.mongodb_manager.insert_post({"content": post})
            random_delay()
        for comment in comments:
            self.mongodb_manager.insert_comment({"content": comment})
            random_delay()

    def cleanup(self):
        pass

# main.py
import logging
from selenium_manager import SeleniumManager
from mongodb_manager import MongoDBManager
from reddit_fetcher import RedditFetcher
from config import MONGO_URI, DB_NAME, LOGIN_CREDENTIALS, BROWSER_HEADERS

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    mongodb_manager = MongoDBManager(MONGO_URI, DB_NAME)
    selenium_manager = SeleniumManager(LOGIN_CREDENTIALS, BROWSER_HEADERS)
    reddit_fetcher = RedditFetcher(selenium_manager, mongodb_manager)
    reddit_fetcher.start_fetching("example_user")
