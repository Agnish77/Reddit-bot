# Reddit-bot

This project is a Reddit bot that automatically posts AI-generated content to a specified subreddit using PRAW (Python Reddit API Wrapper) and Groq AI.

## Features

- Fetches AI-generated content from Groq AI.
- Posts the content to a specified subreddit.
- Schedules posts to be made daily at a specific time.

## Prerequisites

- Python 3.7 or higher
- Reddit API credentials (client_id, client_secret, username, password)
- PRAW library
- Schedule library

## Installation

Clone this repository:
   
git clone https://github.com/Agnish77/Reddit-bot

Navigate to the project directory:

cd reddit-bot

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS and Linux:

source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

## Usage

Create a .env file in the project root directory with your Reddit API credentials:

CLIENT_ID=your_client_id

CLIENT_SECRET=your_client_secret

USERNAME=your_reddit_username

PASSWORD=your_reddit_password

Run the bot:

python app.py

## Configuration

Open app.py and update the following placeholders:

YOUR_SUBREDDIT: Replace this with the name of your subreddit where the bot will post.
Replace client_id, client_secret, username, password, and user_agent with your Reddit API credentials.
Replace GROQ_API_KEY with your Groq API key.

## Error Handling

The bot includes basic error handling and logging. Check the console output for any errors during execution. Common issues include invalid credentials, rate limits, and subreddit access restrictions.

## Contributing

Fork the repository.

Create a new branch: git checkout -b my-feature-branch.

Make your changes and commit them: git commit -m 'Add some feature'.

Push to the branch: git push origin my-feature-branch.

Submit a pull request.

## Acknowledgments

PRAW - The Python Reddit API Wrapper

Schedule - Python job scheduling for humans
