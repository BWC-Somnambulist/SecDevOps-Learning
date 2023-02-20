import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://www.bbc.co.uk"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title of the page
title = soup.title.string

# Extract all the links on the page
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Extract all the paragraphs on the page
paragraphs = []
for p in soup.find_all("p"):
    paragraphs.append(p.get_text())

# Print the results
print("Title: " + title)
print("Links: " + str(links))
print("Paragraphs: " + str(paragraphs))