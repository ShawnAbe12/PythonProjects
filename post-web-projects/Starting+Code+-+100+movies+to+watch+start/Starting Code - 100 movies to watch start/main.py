import requests
from bs4 import BeautifulSoup
import requests


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

requests = requests.get(URL)
# Write your code below this line 👇

soup = BeautifulSoup(requests.text, "html.parser")
titles = soup.find_all("h3", class_="title")

for i in range(0,100):
    print(titles[abs(i-99)].text)


