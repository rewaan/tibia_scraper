import requests
from bs4 import BeautifulSoup
import re
from guild_memebers import CharacterList

date = ['2020-07-03', '2020-07-04']
chl = CharacterList()


class Player:
    """Scrap website name by name from guild and saving data into file"""

    def __init__(self, guild=''):
        self.guild = guild

    @staticmethod
    def _scrap(name):
        """Scraping website and saving it into file"""
        url = 'https://guildstats.eu/character?nick={}'.format(name.replace(' ', '%20').replace("'", r'\%27'))
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        exp_raw = soup.get_text()
        with open('{}_raw'.format(name), 'w') as file:
            file.write(exp_raw)

    @staticmethod
    def _get_experience(name):
        """Obtaining experience value and saving it into dictionary:
        keys - day
        value - experience value"""
        daily_exp = dict()
        with open('{}_raw'.format(name), 'r') as file_raw:
            for line in file_raw:
                for i in date:
                    if line.startswith(i):
                        exp = next(file_raw, '')
                        exp = re.sub('[,+]', '', exp)
                        daily_exp[i] = int(exp)
        return daily_exp

    @staticmethod
    def _get_level(name):
        """Obtaining player level"""
        with open('{}_raw'.format(name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Level:'):
                    level = next(file_raw, '')
                    return level.split(' ')[0]

    @staticmethod
    def _get_vocation(name):
        """Obtaining player vocation"""
        with open('{}_raw'.format(name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Vocation'):
                    voc = next(file_raw, '')
                    return voc.split('\n')[0]

    # @staticmethod
    # def _calculate(guild):
    #     """Calculate total experience"""
    #     result_list = []
    #     total = 0
    #     for name in chl.name_list(guild):
    #         with open(name, 'r') as file:
    #             for line in file:
    #                 for i in date:
    #                     if line.startswith(i):
    #                         result = next(file, '')
    #                         result_list.append(result)
    #         for value in result_list:
    #             value = int(value)
    #             total += value
    #         return total

    def player_presentation(self, guild):
        player = dict()
        for name in chl.name_list(guild):
            # self._scrap(name)
            player[name] = [self._get_level(name), self._get_vocation(name), sorted(self._get_experience(name).items())]
        for keys, values in sorted(player.items()):
            print(keys, values)


pl = Player()
pl.player_presentation('Hill')
