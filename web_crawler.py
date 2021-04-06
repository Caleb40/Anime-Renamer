import requests
# import requests_cache
from bs4 import BeautifulSoup


def scrape_wiki(url):
    # requests_cache.install_cache()
    # url = 'http://www.instaghttps://en.wikipedia.org/wiki/List_of_Angel_Beats!_episodes
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all("td", {"class": "summary"})
    name_list = []
    for i in titles:
        title = i.get_text().split('"')
        name_list.append(title[1])
    return name_list

