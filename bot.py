import praw
import requests
import config
import time

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    password=config.password,
    username=config.username,
    user_agent=config.user_agent
)

GIPHY_API_KEY = config.giphy_api_key
GIPHY_API_URL = 'https://api.giphy.com/v1/gifs/search'

SUBREDDIT = 'test'  # Change to the subreddit you want to monitor

# Define the trigger word
TRIGGER_WORD = 'gif'

def fetch_meme(keyword):
    """Fetch a meme from Giphy based on the keyword."""
    params = {
        'api_key': GIPHY_API_KEY,
        'q': keyword,
        'limit': 1
    }
    response = requests.get(GIPHY_API_URL, params=params)
    data = response.json()
    
    if data['data']:
        meme_url = data['data'][0]['url']
        return meme_url
    else:
        return "No memes found for your search."

def contains_trigger_word(text, trigger_word):
    """Check if the trigger word is in the text."""
    return text.lower().startswith(trigger_word.lower())

def main():
    subreddit = reddit.subreddit(SUBREDDIT)
    print("Bot is running...")
    
    for comment in subreddit.stream.comments(skip_existing=True):
        # Avoid replying to own comments              you can remove this if you want to reply to your own comments
        if comment.author == reddit.user.me():
            continue
        if contains_trigger_word(comment.body, TRIGGER_WORD):
            parts = comment.body.split(' ', 1)
            if len(parts) > 1:
                keyword = parts[1]
                meme_url = fetch_meme(keyword)
                try:
                    comment.reply(f"Here's a meme for '{keyword}': {meme_url}")
                    print(f"Replied to comment {comment.id} with meme: {meme_url}")
                except Exception as e:
                    print(f"Error replying to comment {comment.id}: {e}")
        time.sleep(10)

if __name__ == '__main__':
    main()
