import pandas as pd
from read import *
from guild_memebers import CharacterList
import numpy as np

pl = Player()
chl = CharacterList()
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)


class Frames:
    """Creating data frames from dictionary"""

    def read_data(self, guild):
        df = pd.DataFrame.from_dict(pl.player_presentation(guild), orient='index', columns=['Level', 'Vocation', 'Exp'])
        df[['b1', 'b2']] = pd.DataFrame(df['Exp'].tolist(), index=df.index)
        df[['b3', 'b4']] = pd.DataFrame(df['b1'].tolist(), index=df.index)
        df[['b5', 'b6']] = pd.DataFrame(df['b2'].tolist(), index=df.index)
        df = df.drop(columns=['Exp', 'b1', 'b2', 'b3', 'b5'])
        df = df.rename(columns={'b4': date[0], 'b6': date[1]})
        df['Total'] = df[date[0]] + df[date[1]]
        print(df)
        print(df.sort_values(by='Level'))


fr = Frames()
fr.read_data('Hill')
