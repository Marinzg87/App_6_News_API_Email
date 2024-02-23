import requests

api_key = "91da104af6924548acd22a58ca6bea53"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "sortBy=publishedAt&apiKey=" \
       "91da104af6924548acd22a58ca6bea53"

request = requests.get(url)
content = request.text
print(content)
