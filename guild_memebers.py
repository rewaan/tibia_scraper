from bs4 import BeautifulSoup
import requests


class CharacterList:
    """Scraping website for guild members and saving into set"""
    def __init__(self, guild=''):
        self.guild = guild

    def name_list(self, guild):
        url = 'https://guildstats.eu/guild={}&op=2'.format(guild)
        r = requests.get(url, verify=False)
        data = r.text
        soup = BeautifulSoup(data, features="lxml")
        char_set = set()
        for link in soup.find_all('a'):
            if 'nick' in link.get('href'):
                name = link.get_text()
                char_set.add(name)
        return char_set


chl = CharacterList()
chl.name_list('Hill')
# print(chl.name_list('Hill'))

