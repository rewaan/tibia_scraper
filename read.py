import re
from guild_memebers import CharacterList
import pandas as pd

date = ['2020-07-10', '2020-07-11', '2020-07-14', '2020-07-15', '2020-07-16', '2020-07-17']
chl = CharacterList()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Player:
    """Scrap website name by name from guild and saving data into file"""

    def __init__(self, guild=''):
        self.guild = guild
        print(self.save_df(guild))

    @staticmethod
    def exp_by_day(name, guild):
        """Obtaining experience value and saving it into dictionary:
        keys - day
        value - experience value"""
        daily_exp = {}
        with open(r'{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                for i in date:
                    if line.startswith(i):
                        exp = next(file_raw, '')
                        exp = re.sub('[,+]', '', exp)
                        exp = int(exp)
                        daily_exp[i] = int(exp)
        df_exp = pd.Series(daily_exp)
        return df_exp

    @staticmethod
    def get_level(name, guild):
        """Obtaining player level"""
        with open(r'{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Level:'):
                    level = next(file_raw, '')
                    level = int(level.split(' ')[0])
                    df_lvl = pd.Series(level, index=['Level'])
                    return df_lvl

    @staticmethod
    def get_vocation(name, guild):
        """Obtaining player vocation"""
        with open(r'{}/{}_raw'.format(guild, name), 'r') as file_raw:
            for line in file_raw:
                if line.startswith('Vocation'):
                    voc = next(file_raw, '')
                    voc = voc.split('\n')[0]
                    df_voc = pd.Series(voc, index=['Vocation'])
                    return df_voc

    def save_df(self, guild):
        """Creating guild and players DataFrames. Save it into files"""
        df_guild = pd.DataFrame()
        for name in chl.name_list(guild):
            df = pd.Series(name, index=['Name'])
            df_voc = self.get_vocation(name, guild)
            df_lvl = self.get_level(name, guild)
            df_exp = self.exp_by_day(name, guild)
            df = df.append([df_voc, df_lvl, df_exp])
            df_guild = df_guild.append(df, ignore_index=True)
            df.to_csv(r'{}/{}_df.csv'.format(guild, name))
            print(df)
        df_guild = df_guild.set_index('Name')
        col_order = ['Level', 'Vocation']
        new_col_order = col_order + (df_guild.columns.drop(col_order).tolist())
        df_guild = df_guild[new_col_order]
        df_guild.to_csv(r'{0}/{0}.csv'.format(guild))
        print(df_guild)


if __name__ == '__main__':
    Player('Hill')

# pl.player_presentation('Hill')
