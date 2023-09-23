import requests
from bs4 import BeautifulSoup

def extract_ip(ip_url):
    response = requests.get(ip_url)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    ip = soup.get_text()
    
    return ip

def extract_location(location_url):
    response = requests.get(location_url)
    
    soup = BeautifulSoup(response.content, 'html.parser')

    location = soup.get_text()
    
    return location

ip_url = "http://api.ipify.org/?format=json"
ip = extract_ip(ip_url)[7:-2]

location_url = "http://ipinfo.io/" + ip + "/geo"
information = extract_location(location_url).split(",")
location = information[2] + information[4]

print("ip : ", ip)
print("location : ", location)