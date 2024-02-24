import requests
from send_email import send_email

api_key = "91da104af6924548acd22a58ca6bea53"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "sortBy=publishedAt&apiKey=" \
       "91da104af6924548acd22a58ca6bea53"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

# Convert news to correct code
body = body.encode("utf-8")

# Preparing the message with news
message = f"""\
Subject: New email from App 6 News API

From: App 6 News API
Topic: news
{body}
"""

send_email(message=message)
