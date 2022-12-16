"""
Created on Dec 16, 2022.
utils.py

@author: Soroosh Tayebi Arasteh <soroosh.arasteh@rwth-aachen.de>
https://github.com/tayebiarasteh/
"""

import numpy as np
import seaborn as sns
import pdb
import matplotlib.pylab as plt
import pandas as pd



def main_resnet():

    auc_list = np.array([[0.90, 0.71, 0.68, 0.65, 0.68, 0.63, -1.00],
                         [0.88, 0.81, 0.76, 0.76, 0.71, 0.61, -1.00],
                         [0.87, 0.75, 0.80, 0.77, 0.69, 0.62, -1.00],
                         [0.83, 0.77, 0.74, 0.77, 0.63, 0.58, -1.00],
                         [0.88, 0.76, 0.72, 0.69, 0.88, 0.00, -1.00],
                         [0.75, 0.66, 0.66, 0.62, 0.00, 0.75, -1.00],
                         [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00]])

    ############ random placeholders below #############
    D = 28
    H = 24
    df = pd.DataFrame({'day': np.repeat(range(1, D + 1), H),
                       'hour': np.tile(range(H), D),
                       'Cost Dif.': np.random.uniform(10, 1000, D * H)})
    df.loc[df['hour'] == 10, 'Cost Dif.'] = 150
    df.loc[df['hour'] == 12, 'Cost Dif.'] = 250
    df.loc[df['day'] == 20, 'Cost Dif.'] = 800
    g = sns.jointplot(data=df, x='day', y='hour', kind='hist', bins=(D, H))
    ############ random placeholders above ############

    g.ax_marg_y.cla()
    sns.set(font_scale=1.5)

    sns.heatmap(auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    g.ax_marg_y.barh(0.5, width=18000, color="grey")
    g.ax_marg_y.barh(1.5, width=213921, color="grey")
    g.ax_marg_y.barh(2.5, width=157676, color="grey")
    g.ax_marg_y.barh(3.5, width=112120, color="grey")
    g.ax_marg_y.barh(4.5, width=193361, color="grey")
    g.ax_marg_y.barh(5.5, width=9125, color="grey")
    g.ax_marg_y.barh(6.5, width=105000, color="grey") #TODO

    # remove ticks showing the heights of the histograms
    g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
    g.ax_marg_y.tick_params(axis='x', bottom=True, labelbottom=True, labelsize=5)
    g.ax_marg_y.grid(False)

    plt.show()


def main_vit():

    auc_list = np.array([[0.90, 0.72, 0.68, 0.64, 0.71, 0.65, -1.00],
                         [0.90, 0.81, 0.75, 0.76, 0.70, 0.62, -1.00],
                         [0.87, 0.76, 0.80, 0.76, 0.68, 0.64, -1.00],
                         [0.86, 0.77, 0.75, 0.77, 0.64, 0.61, -1.00],
                         [0.90, 0.77, 0.73, 0.70, 0.87, 0.00, -1.00],
                         [0.79, 0.69, 0.67, 0.65, 0.00, 0.77, -1.00],
                         [-1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00]])

    ############ random placeholders below #############
    D = 28
    H = 24
    df = pd.DataFrame({'day': np.repeat(range(1, D + 1), H),
                       'hour': np.tile(range(H), D),
                       'Cost Dif.': np.random.uniform(10, 1000, D * H)})
    df.loc[df['hour'] == 10, 'Cost Dif.'] = 150
    df.loc[df['hour'] == 12, 'Cost Dif.'] = 250
    df.loc[df['day'] == 20, 'Cost Dif.'] = 800
    g = sns.jointplot(data=df, x='day', y='hour', kind='hist', bins=(D, H))
    ############ random placeholders above ############

    g.ax_marg_y.cla()
    sns.set(font_scale=1.5)

    sns.heatmap(auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    g.ax_marg_y.barh(0.5, width=18000, color="grey")
    g.ax_marg_y.barh(1.5, width=213921, color="grey")
    g.ax_marg_y.barh(2.5, width=157676, color="grey")
    g.ax_marg_y.barh(3.5, width=112120, color="grey")
    g.ax_marg_y.barh(4.5, width=193361, color="grey")
    g.ax_marg_y.barh(5.5, width=9125, color="grey")
    g.ax_marg_y.barh(6.5, width=105000, color="grey") #TODO

    # remove ticks showing the heights of the histograms
    g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
    g.ax_marg_y.tick_params(axis='x', bottom=True, labelbottom=True, labelsize=5)
    g.ax_marg_y.grid(False)

    plt.show()


if __name__ == '__main__':
    main_resnet()
    # main_vit()