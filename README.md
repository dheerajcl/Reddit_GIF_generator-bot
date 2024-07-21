# Reddit GIF Bot

## Description

This Reddit bot automatically replies to comments in a specified subreddit with a gif you requested. The bot uses the Giphy API to fetch memes and responds to comments containing a specific trigger word.

## Features

- Monitors comments in a specified subreddit.
- Replies to comments containing a trigger word set by you.
- Fetches memes using the Giphy API.
- Configurable trigger word and subreddit.

## Setup

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Reddit Account**: You need a Reddit account to create an application and get API credentials.
3. **Giphy API Key**: Obtain an API key from Giphy.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/dheerajcl/Reddit_meme_generator-bot.git
   cd <repository-directory>

2. **Install the required packages**

    ```bash
    pip install praw requests

3. **Configure the bot**

   ***Create a `config.py` file in the root directory of the project with the following content:***

    ```python
    # Reddit API credentials
    client_id = 'YOUR_REDDIT_CLIENT_ID'
    client_secret = 'YOUR_REDDIT_CLIENT_SECRET'
    username = 'YOUR_REDDIT_USERNAME'
    password = 'YOUR_REDDIT_PASSWORD'
    user_agent = 'YOUR_USER_AGENT'
    
    # Giphy API key
    giphy_api_key = 'YOUR_GIPHY_API_KEY'

**Run the bot and set `SUBREDDIT` variable to the subreddit you want to monitor and `TRIGGER_WORD` to the word that will trigger the bot to reply with a meme.**

**If you set `TRIGGER_WORD` to `"gif"` followed by the word you want a gif on and the bot is running, it will reply to any comment in the specified subreddit containing the word "gif" with the gif you requested from Giphy.**


## API Credentials 

- Go to [Reddit/apps](https://www.reddit.com/prefs/apps)  and create a new app, `description` and `about url` are optional.

- `redirect uri`  can be set to `http://localhost:8000`

- Get your `client_id` (under your app name) and `client_secret`

- Visit [Giphy API](https://developers.giphy.com/dashboard) and create a new api key

   
