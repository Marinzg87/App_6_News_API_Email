import requests

api_key = "91da104af6924548acd22a58ca6bea53"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "sortBy=publishedAt&apiKey=" \
       "91da104af6924548acd22a58ca6bea53"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])
