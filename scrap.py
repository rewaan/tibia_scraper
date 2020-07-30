from bs4 import BeautifulSoup
import requests
from guild_memebers import CharacterList
import os.path


chl = CharacterList()


class Scraper:
    """Visit website and scrap data. Save it into _raw file
    guild - name of guild
    name - character name"""
    def __init__(self, guild=''):
        self.guild = guild

    @staticmethod
    def make_dir(guild):
        try:
            os.makedirs(guild)
        except OSError:
            pass

    @staticmethod
    def _scrap(name, guild):
        """Scraping website and saving it into file"""
        url = 'https://guildstats.eu/character?nick={}'.format(name.replace(' ', '%20').replace("'", r'\%27'))
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        exp_raw = soup.get_text()
        with open(os.path.join(r'D:/Exp Tibia/{}/{}_raw'.format(guild, name)), 'w') as file:
            file.write(exp_raw)

    def scraper(self, guild):
        self.make_dir(guild)
        for name in chl.name_list(guild):
            self._scrap(name, guild)


scr = Scraper()
scr.scraper('Sleepers')
