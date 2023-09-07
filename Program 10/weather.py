import requests
from bs4 import BeautifulSoup
city = input("Enter the city name: ")
url ="https://www.google.com/search?q=weather+in+"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split('\n')
time = data[0]
sky = data[1]
print("Temperature in "+city+" is: "+temp)
print("Time: "+time)
print("Sky: "+sky)