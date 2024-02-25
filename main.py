import requests
from send_email import send_email

api_key = "91da104af6924548acd22a58ca6bea53"
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt&" \
        "apiKey=91da104af6924548acd22a58ca6bea53&" \
        "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"

# Convert news to correct code
body = body.encode("utf-8")

send_email(message=body)
