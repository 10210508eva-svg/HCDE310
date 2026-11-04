import requests

url = "https://openlibrary.org/search.json"

params = {
    "q": "design",
    "fields": "title,author_name",
    "limit": 3
}

response = requests.get(url, params=params)
data = response.json()

for book in data["docs"]:
    title = book.get("title", "Unknown title")
    authors = book.get("author_name", ["Unknown author"])
    print(title, "-", ", ".join(authors))
