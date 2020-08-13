import matplotlib.pyplot as plt
from read import *
import pandas as pd


class Plots:

    def __init__(self, guild=''):
        self.guild = guild

    @staticmethod
    def read_player_df(name, guild):
        df = pd.read_csv(r'{}/{}_df.csv'.format(guild, name))
        return df

    def day_exp_plot(self, name, guild):
        df = self.read_player_df(name, guild)
        df = df.rename(columns={'Unnamed: 0': 'Day', '0': 'Experience'})
        df = df.set_index('Day')
        df = df.drop(index=['Name', 'Level', 'Vocation'])
        df = df.astype(float)
        df = df['Experience']/1000000
        print(df)
        ax = df.plot(kind='line', marker='.')
        ax.set_ylabel('Experience/1,000,000')
        plt.title(name)
        plt.show()


plots = Plots()
plots.day_exp_plot('Goraca', 'Hill')
# plots.read_df('Hill')
