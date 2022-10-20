from bs4 import BeautifulSoup
import requests

with open('example.html')as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# Match = soup.title.text
# Print(match)

print(soup.prettify())

