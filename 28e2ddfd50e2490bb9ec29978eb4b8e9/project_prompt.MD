# Instructions for Building "Reddit Clone Data Fetcher and MongoDB Storage" Application

## Overview
This document outlines the steps to implement a Python script that fetches posts and comments from a clone of Reddit, storing them in MongoDB. The application will use Selenium for web scraping and will follow the specified design and architecture throughout the stages of development.

## Architecture Pattern
The application will utilize the Model-View-Controller (MVC) architecture, where:
- **Model**: Represents data structure and MongoDB interactions.
- **View**: Provides a simple command-line interface (CLI) for input and configuration.
- **Controller**: Handles the application logic, including fetching data and orchestrating the interaction between the Model and the View.

## Functional Components Breakdown

### 1. Setup Project Structure
- Create a project directory named `reddit_clone_fetcher`.
- Inside the directory, create the following subdirectories and files:
  - `src/` - for source code
  - `config/` - for configuration files
  - `data/` - for storing fetched data
  - `reddit_clone_fetcher.py` - main application script
  - `config/schema.json` - JSON schema file defining data structure

### 2. Dependency Management
- Create a `requirements.txt` file with the following dependencies:
  ```
  Selenium
  pymongo
  requests
  jsonschema
  argparse
  ```

### 3. Import Required Libraries
- In `reddit_clone_fetcher.py`, import the following libraries:
  - `selenium.webdriver`
  - `pymongo`
  - `requests`
  - `json`
  - `argparse`
  - `random`
  - `time`
  - `jsonschema`

### 4. Command-Line Argument Parsing
- Implement command-line parsing using `argparse` to accept a `--config` parameter that points to the JSON configuration file.
  
### 5. Load JSON Configuration
- Define a function to load the JSON configuration file, validate it against the defined schema using `jsonschema`.

### 6. Initialize Selenium WebDriver
- Create a function to initialize the Selenium WebDriver with the appropriate Chrome options to simulate Chromebook or any specific user-agent.

### 7. Login Automation
- Implement a function to:
  - Navigate to the Reddit clone login page.
  - Input username and password from the configuration.
  - Submit the form and wait for successful login confirmation.

### 8. MongoDB Setup
- Establish a connection with MongoDB using `pymongo`. Create `my_posts` and `my_comments` collections as needed.

### 9. Browser Header Simulation
- Define a list of headers (simulating different devices) to be used for making requests to the Reddit clone.

### 10. Data Fetching Logic
- Implement functions to:
  - Fetch posts and comments, cycling through the list of headers.
  - Respect defined delays between requests as specified in the configuration.

### 11. Data Storage Mechanism
- Create a function that takes the fetched data and stores it in the respective MongoDB collections, ensuring proper structure and metadata is applied.

### 12. Error Handling
- Implement error handling around network requests, login attempts, and MongoDB operations using try-except blocks to manage exceptions gracefully.

### 13. Cleanup Resources
- Ensure the WebDriver and MongoDB connections are properly closed at the end of the script's execution, regardless of success or failure.

## Implementation Steps
1. Set up the project structure and create the necessary files.
2. Write the schema in the `config/schema.json` to define the data structure.
3. Implement the import statements in `reddit_clone_fetcher.py`.
4. Write the argument parsing logic and JSON configuration loading.
5. Code the WebDriver initialization for Selenium automation.
6. Implement the login automation functionality.
7. Set up the MongoDB connection and collections.
8. Develop the logic to simulate browser headers and fetch data.
9. Create the functions for storing data in MongoDB and handling errors effectively.
10. Write the cleanup logic for closing resources.
11. Test the script thoroughly for various scenarios including error cases.

## Testing & Validation
- Validate the complete flow by running the script with sample configuration files, and ensure that all components properly interact and that data is correctly stored in MongoDB.
- Use various Reddit clone URLs as configurations to ensure adaptability.

By following these structured instructions, you will be able to build the "Reddit Clone Data Fetcher and MongoDB Storage" application according to the defined specifications.