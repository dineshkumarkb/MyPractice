from bs4 import BeautifulSoup
import requests

URL = 'https://www.twitch.tv'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())

offline = soup.find('a', {'class':'side-nav-card__link'})
spans = soup.find_all('a')

for span in spans:
    print(span)

print(offline)