from bs4 import BeautifulSoup
import requests

with open('example.html')as html_file:
    soup = BeautifulSoup(html_file,'lxml')

#match = soup.title.text
#print(match)

print(soup.prettify())

