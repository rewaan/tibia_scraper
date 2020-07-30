import pandas as pd
from read import *

pl = Player()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)


class Frames:
    """Creating DataFrame from dictionary and saving it into csv file
        Clearing and saving new DataFrame"""

    # @staticmethod
    # def save_guild_df(guild):
    #     """Creating DataFrame from dictionary and save it as csv_raw file"""
    #     df = pd.DataFrame.from_dict(pl.player_presentation(guild), orient='index', columns=['Level', 'Vocation', 'Exp'])
    #     df.to_csv(r'D:/Exp Tibia/{0}/{0}_raw.csv'.format(guild))

    @staticmethod
    def save_df(guild):
        """Creating guild and players DataFrames. Save it into files"""
        df_guild = pd.DataFrame()
        for name in chl.name_list(guild):
            df = pd.Series(name, index=['Name'])
            df_voc = pd.Series(pl.get_vocation(name, guild), index=['Vocation'])
            df_lvl = pd.Series(pl.get_level(name, guild), index=['Level'])
            df_exp = pd.Series(pl.exp_by_day(name, guild))
            df = df.append([df_voc, df_lvl, df_exp])
            df_guild = df_guild.append(df, ignore_index=True)
            df.to_csv(r'D:/Exp Tibia/{}/{}_df.csv'.format(guild, name))
            print(df)
        df_guild = df_guild.set_index('Name')
        col_order = ['Level', 'Vocation']
        new_col_order = col_order + (df_guild.columns.drop(col_order).tolist())
        df_guild = df_guild[new_col_order]
        df_guild.to_csv(r'D:/Exp Tibia/{0}/{0}.csv'.format(guild))
        print(df_guild)

    # @staticmethod
    # def clear_df(guild):
    #     """Loading and clearing DataFrame"""
    #     df = pd.read_csv(r'D:/Exp Tibia/{0}/{0}_raw.csv'.format(guild))
    #     spec_chars = ["'", "(", ")", "[", "]"]
    #     for char in spec_chars:
    #         df['Exp'] = df['Exp'].str.replace(char, '')
    #     df[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']] = pd.DataFrame(df['Exp'].str.split(',').tolist())
    #     df = df.rename(columns={'Unnamed: 0': 'Name', '2': date[0], '4': date[1], '6': date[2], '8': date[3], '10': date[4]})
    #     df = df.drop(columns={'Exp', '1', '3', '5', '7', '9'})
    #     df = df.replace([None], [0])
    #     df[[date[0], date[1], date[2], date[3], date[4]]] = df[[date[0], date[1], date[2], date[3], date[4]]].apply(pd.to_numeric)
    #     # print(df)
    #     df['Total'] = df[date[0]] + df[date[1]] + df[date[2]] + df[date[3]] + df[date[4]]
    #     # df = df.set_index('Name')
    #     print(df)
    #     df.to_csv(r'D:/Exp Tibia/{0}/{0}.csv'.format(guild))


fr = Frames()
fr.save_df('Hill')
