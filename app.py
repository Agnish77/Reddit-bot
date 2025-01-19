import praw
import requests
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Reddit API credentials
reddit = praw.Reddit(
    client_id='r_g_sZTenqJ3kz6GapBBB',
    client_secret='	kOS5pqfdYCuDii4oV-zsFQ',
    username='u/Ok-Refuse5',
    password='agnisGHC',
    user_agent='Redditbot2 by /u/Ok-Refuse5'
)

# Groq API key
GROQ_API_KEY = 'sk_Av6L515neMURpVbDlehAWGdyb3FYsMOLdkna9TMfQPfJh0VzCV'

def generate_content():
    """Generate content using Groq AI."""
    response = requests.post(
        'https://api.groq.com/openai/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {GROQ_API_KEY}'
        },
        json={
            'model': 'llama-3.3-70b-versatile',
            'messages': [{
                'role': 'user',
                'content': 'Generate an interesting post about technology.'
            }]
        }
    )
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        logging.error(f"Error with Groq API: {response.status_code} {response.text}")
        return None


def post_to_reddit():
    """Post generated content to Reddit."""
    content = generate_content()
    if content:
        subreddit = reddit.subreddit('YOUR_SUBREDDIT')
        subreddit.submit(title='AI Generated Content', selftext=content)
        logging.info("Post submitted successfully.")
    else:
        logging.error("Failed to generate content.")

# Schedule the bot to post daily at a specified time
schedule.every().day.at("13:23").do(post_to_reddit)

# Run the scheduler
logging.info("Starting the Reddit bot.")
while True:
    schedule.run_pending()
    time.sleep(1)


