# Reddit-bot

A Python-based bot that automatically posts content to Reddit using the PRAW (Python Reddit API Wrapper) library.

## Features

- Automatically posts content to a specified subreddit.
- Scheduled posting using the `schedule` library.
- Customizable content generation.
- Error handling and logging for better debugging.

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

The bot's behavior can be customized by editing the app.py file. You can modify the content generation logic, subreddit target, posting frequency, etc.

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
