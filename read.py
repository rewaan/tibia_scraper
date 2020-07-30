import re
from guild_memebers import CharacterList

date = ['2020-07-10', '2020-07-11','2020-07-14', '2020-07-15', '2020-07-16', '2020-07-17']
chl = CharacterList()


class Player:
    """Scrap website name by name from guild and saving data into file"""

    def __init__(self, guild=''):
        self.guild = guild

    @staticmethod
    def exp_by_day(name, guild):
        """Obtaining experience value and saving it into dictionary:
        keys - day
        value - experience value"""
        daily_exp = {}
        with open(r'D:/Exp Tibia/{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                for i in date:
                    if line.startswith(i):
                        exp = next(file_raw, '')
                        exp = re.sub('[,+]', '', exp)
                        exp = int(exp)
                        daily_exp[i] = int(exp)
        return daily_exp

    @staticmethod
    def get_level(name, guild):
        """Obtaining player level"""
        with open(r'D:/Exp Tibia/{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Level:'):
                    level = next(file_raw, '')
                    return int(level.split(' ')[0])

    @staticmethod
    def get_vocation(name, guild):
        """Obtaining player vocation"""
        with open(r'D:/Exp Tibia/{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Vocation'):
                    voc = next(file_raw, '')
                    return voc.split('\n')[0]

    # def player_presentation(self, guild):
    #     player = {}
    #     for name in chl.name_list(guild):
    #         player[name] = [self._get_level(name, guild), self._get_vocation(name, guild), sorted(self._exp_by_day(name, guild).items())]
    #     return player


pl = Player()
# pl.player_presentation('Hill')
