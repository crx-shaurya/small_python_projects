import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.text)

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]
    
    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {tags}")
    print("-" * 50)

import csv

with open("quotes.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author", "Tags"])

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))
        
        writer.writerow([text, author, tags])


url = "http://quotes.toscrape.com/"
all_data = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))
        all_data.append([text, author, tags])

    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page = next_btn.a['href']
        url = "http://quotes.toscrape.com" + next_page
    else:
        url = None

# Save after all pages are done
with open("all_quotes.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(all_data)
