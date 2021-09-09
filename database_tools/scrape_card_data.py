from bs4 import BeautifulSoup
import requests
import re

def scrape_data():

    url = "https://www.pokellector.com/sets/SWSH7-Evolving-Skies"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    hrefs = soup.find_all("a", {"href":re.compile(r'^/card')})
    print(hrefs)
    
    for i in range(len(hrefs)):
        pokemon_name = hrefs[i]["title"].split("-")[0].strip()
        pokemon_num = hrefs[i]["title"].split("#")[1].strip()
        series = hrefs[i]["title"].split("-")[1].split("#")[0].strip()
        print(series)
        
if __name__ == "__main__":
    scrape_data()
