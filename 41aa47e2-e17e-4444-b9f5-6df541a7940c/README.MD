## Overview

This application automates the process of fetching posts and comments from a Reddit user's profile using Selenium for web automation and storing the data in a MongoDB database. The project structure includes several modules to manage configuration, MongoDB operations, Selenium automation, and utility functions.

## Modules

1. **config.py:** Contains configuration settings such as MongoDB URI, database name, login credentials, and browser headers.

2. **mongodb_manager.py:** Handles MongoDB operations such as connecting to the database, and inserting posts and comments.

3. **selenium_manager.py:** Manages the Selenium driver, performs login actions, and fetches user posts and comments.

4. **utils.py:** Provides auxiliary functions such as creating random delays during script execution.

5. **reddit_fetcher.py:** Integrates Selenium and MongoDB managers to automate the fetching and storing of Reddit data.

6. **main.py:** Initializes the application, sets up logging, and triggers the fetching process for a specified Reddit username.

## Installation and Configuration

### Prerequisites

- Python 3.x installed on your system
- MongoDB installed and running locally or accessible via the network
- Google Chrome browser installed
- ChromeDriver compatible with your Google Chrome version

### Steps to Install and Run

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Packages:**

   Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   .\venv\Scripts\activate  # On Windows
   ```

   Install the necessary packages using `pip`:

   ```bash
   pip install pymongo selenium
   ```

3. **Download ChromeDriver:**

   Download the ChromeDriver executable matching your version of Google Chrome from the [ChromeDriver site](https://sites.google.com/a/chromium.org/chromedriver/).

4. **Set Up Configuration:**

   Edit `config.py` to set up your MongoDB URI, database name, and Reddit login credentials:

   ```python
   MONGO_URI = "mongodb://localhost:27017/"
   DB_NAME = "reddit_clone"
   LOGIN_CREDENTIALS = {"username": "your_username", "password": "your_password"}
   BROWSER_HEADERS = {"User-Agent": "Mozilla/5.0 (Your custom user agent)"}
   ```

   Ensure that `MONGO_URI` is pointing to your MongoDB instance, and `LOGIN_CREDENTIALS` are replaced with your actual Reddit username and password.

5. **Run the Application:**

   After setting up the configuration, run the application using:

   ```bash
   python main.py
   ```

   Edit the `main.py` to specify the target Reddit username in the `reddit_fetcher.start_fetching("example_user")` line.

## Notes

- Ensure that the MongoDB server is running and accessible when executing the script.
- Make sure to replace `"example_user"` with the actual Reddit username you want to fetch data for.
- The functionality depends on the page structure of Reddit, which may change over time; thus updating CSS selectors and XPath expressions in `selenium_manager.py` may be required.