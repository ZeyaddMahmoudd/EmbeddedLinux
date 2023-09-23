import requests
from bs4 import BeautifulSoup

def extract_text_from_website(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()
    
    return text

website_url = "http://www.boredapi.com/api/activity"
text = extract_text_from_website(website_url).split(",")
for i in text:
    print(i)

