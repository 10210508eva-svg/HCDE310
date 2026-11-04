Name:Open Library API

What is this API?
This is an open library resource that contains book titles, authors, publication years, images, and more. This API allows people to get books' information in JSON format.

Why designer care? 
Designers might think this is a useful tool when they are creating a book search website or digital library. This API means designers don't need to enter book information manually and can focus more on design.

How to use it?
1. 
Open the terminal and install requests:
python3 -m pip install requests

Create a Python file called books.py

Find parameters: At this link, https://openlibrary.org/dev/docs/api/search, there is a Fields tab, and you can see a lot of data on GitHub. I think these are all the parameters you can use: https://github.com/internetarchive/openlibrary/blob/b4afa14b0981ae1785c26c71908af99b879fa975/openlibrary/plugins/worksearch/schemes/works.py#L38-L91

API end point is https://openlibrary.org/search.json

2. Decide which parameters you want to use as fields. We use title and author as our examples.

3. 
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

4. 
- Request.get sent request to Open Library.
- params tells the API what books to search for and what information to return.
- .json convert the response to python format
- data["docs"] contains the list of books that are matching
- .get() helps replacing missing information with "unknown __" without crashing the program.

5. Results (I create a example.py file to test this)
The Psychology of Everyday Things - Donald A. Norman
Patternmaking for fashion design - Helen Joseph Armstrong
Research Design - John W. Creswell, J. David Creswell

Gotchas
- It has a limit on the number of calls you can make per minute. You can't make more calls than that.
- Some books may not have an author, publication year, or cover image. We have to use .get() to prevent crashes. 
- There are a lot of different APIs in Open Library, and they all have different uses. I think it might be really confusing for people to use, especially beginners.This is a problem I actually encountered. I didn't know which API I should use because there are so many different APIs, and their documentation is really long. Overall, I found that once we choose the Search API, we don't really need to worry about using different endpoints for different searches. We can focus more on the parameters because the Search API endpoint allows us to retrieve different types of book information.

Design angle
- A personalized book exploration website where users can search for books by keyword, get book information, and decide whether they want to read them or not.

- I think the consideration I would have is that when information is missing, we still want to show users some useful information. While we are trying to give them useful information, we might get some parts wrong. It would be really bad if that happened. We don't want to provide misleading information. We need to be careful about balancing ethics and user experience.

AI use
I double check with ai how to use the code to call api.







