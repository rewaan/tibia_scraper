from read import *

pl = Player()

# pd.set_option('display.max_colwidth', -1)


def save_df(guild):
    """Creating guild and players DataFrames. Save it into files"""
    df_guild = pd.DataFrame()
    for name in chl.name_list(guild):
        df = pd.Series(name, index=['Name'])
        df_voc = pl.get_vocation(name, guild)
        df_lvl = pl.get_level(name, guild)
        df_exp = pl.exp_by_day(name, guild)
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


save_df('Hill')
