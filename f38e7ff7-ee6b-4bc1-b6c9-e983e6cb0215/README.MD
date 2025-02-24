## Reddit Clone Fetcher Documentation

### Overview

This script is a web scraper designed to log in to a Reddit-like website, collect data from posts, and store this data in a MongoDB database. It utilizes Selenium for web automation and interaction, and PyMongo for database operations.

### Prerequisites

Before running this script, ensure you have the following components installed:

- Python 3.x
- Google Chrome Browser
- ChromeDriver compatible with your Chrome version
- MongoDB instance (local or remote)
  
### Installation and Configuration

1. **Google Chrome and ChromeDriver:**
   - Install Google Chrome from the [official site](https://www.google.com/chrome/).
   - Install ChromeDriver. Ensure you download the version that matches your installed Chrome browser version. You can get ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).

2. **Python Packages:**

   Install the required Python packages using pip:
   ```bash
   pip install selenium pymongo jsonschema
   ```

3. **Setup MongoDB:**

   Ensure you have a running instance of MongoDB. You can download and install MongoDB from [MongoDB's official site](https://www.mongodb.com/).

4. **Configuration File:**

   Create a JSON configuration file (for example, `config.json`) consistent with the following structure:

   ```json
   {
       "reddit": {
           "url": "https://example-reddit-clone.com",
           "login": {
               "username": "your-username",
               "password": "your-password"
           }
       },
       "mongodb": {
           "uri": "mongodb://localhost:27017/",
           "database": "reddit_clone_db",
           "collection": "posts"
       }
   }
   ```

   - Replace `https://example-reddit-clone.com` with the actual URL of the Reddit clone.
   - Use your username and password for the "login" section.
   - Update MongoDB URI, database, and collection details as necessary.

### Command-Line Usage

Run the script using the command line, specifying the path to your configuration file:

```bash
python script_name.py --config path/to/config.json
```

### Script Functionality

- **Load Configuration**: Validates and loads the configuration file.
- **Login**: Uses Selenium to log in to the specified Reddit clone using provided credentials.
- **Fetch Data**: Gathers posts' data, specifically the title and comments count, from the loaded page.
- **Store Data**: Saves the fetched data into the specified MongoDB database and collection.
- **Logging**: Logs activities and errors in `reddit_clone_fetcher.log`.

### Important Considerations

- **ChromeDriver Compatibility**: Ensure your ChromeDriver is compatible with your version of Chrome.
- **Security**: Do not expose sensitive data (such as usernames and passwords) in unsecured locations or repositories.
- **Execution Timing**: Consider using delays appropriately in the Selenium scripts to handle dynamic content loading.