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
    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # vindr-pediatric
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.90, 0.63, 0.65, 0.68, 0.71, 0.69, 0.74],
                         [0.75, 0.76, 0.62, 0.66, 0.66, 0.00, 0.67],
                         [0.83, 0.61, 0.77, 0.74, 0.77, 0.65, 0.81],
                         [0.87, 0.59, 0.77, 0.80, 0.75, 0.69, 0.84],
                         [0.88, 0.64, 0.76, 0.76, 0.81, 0.70, 0.85],
                         [0.88, 0.00, 0.69, 0.72, 0.76, 0.88, 0.82],
                         [0.86, 0.59, 0.73, 0.75, 0.77, 0.67, 0.87]])

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
    g.ax_marg_y.barh(1.5, width=9125, color="grey")
    g.ax_marg_y.barh(2.5, width=112120, color="grey")
    g.ax_marg_y.barh(3.5, width=157676, color="grey")
    g.ax_marg_y.barh(4.5, width=213921, color="grey")
    g.ax_marg_y.barh(5.5, width=193361, color="grey")
    g.ax_marg_y.barh(6.5, width=110525, color="grey")

    # remove ticks showing the heights of the histograms
    g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
    g.ax_marg_y.tick_params(axis='x', bottom=True, labelbottom=True, labelsize=5)
    g.ax_marg_y.grid(False)

    plt.show()


def main_vit():
    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # vindr-pediatric
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.90, 0.65, 0.64, 0.68, 0.72, 0.71, 0.75],
                         [0.79, 0.77, 0.65, 0.67, 0.69, 0.00, 0.71],
                         [0.86, 0.61, 0.77, 0.75, 0.77, 0.64, 0.81],
                         [0.87, 0.64, 0.76, 0.80, 0.76, 0.68, 0.83],
                         [0.90, 0.62, 0.76, 0.75, 0.81, 0.70, 0.85],
                         [0.90, 0.00, 0.70, 0.73, 0.77, 0.87, 0.83],
                         [0.87, 0.68, 0.72, 0.75, 0.77, 0.69, 0.88]])

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
    g.ax_marg_y.barh(1.5, width=9125, color="grey")
    g.ax_marg_y.barh(2.5, width=112120, color="grey")
    g.ax_marg_y.barh(3.5, width=157676, color="grey")
    g.ax_marg_y.barh(4.5, width=213921, color="grey")
    g.ax_marg_y.barh(5.5, width=193361, color="grey")
    g.ax_marg_y.barh(6.5, width=110525, color="grey")

    # remove ticks showing the heights of the histograms
    g.ax_marg_y.tick_params(axis='y', left=False, labelleft=False)
    g.ax_marg_y.tick_params(axis='x', bottom=True, labelbottom=True, labelsize=5)
    g.ax_marg_y.grid(False)

    plt.show()





def cardiomegaly_resnet():

    # order: vindr, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.95, 0.73, 0.77, 0.73, 0.68, 0.83],
                         [0.84, 0.88, 0.78, 0.72, 0.75, 0.89],
                         [0.83, 0.85, 0.87, 0.73, 0.69, 0.90],
                         [0.80, 0.80, 0.82, 0.81, 0.79, 0.87],
                         [0.96, 0.82, 0.84, 0.79, 0.86, 0.87],
                         [0.89, 0.85, 0.81, 0.70, 0.75, 0.92]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def pneumonia_resnet():

    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # vindr-pediatric
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.90, 0.66, 0.63, 0.56, 0.61, 0.79, 0.72],
                         [0.75, 0.78, 0.60, 0.57, 0.58, 0.56, 0.64],
                         [0.84, 0.64, 0.67, 0.57, 0.64, 0.81, 0.71],
                         [0.73, 0.63, 0.65, 0.74, 0.60, 0.76, 0.62],
                         [0.82, 0.62, 0.70, 0.71, 0.72, 0.81, 0.81],
                         [0.75, 0.66, 0.68, 0.63, 0.67, 0.92, 0.78],
                         [0.85, 0.61, 0.67, 0.66, 0.70, 0.82, 0.84]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def nofinding_resnet():

    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, padchest

    # order:

    # vindr,
    # vindr-pediatric,
    # cxr14,
    # chexpert,
    # mimic,
    # padchest

    auc_list = np.array([[0.91, 0.57, 0.68, 0.82, 0.78, 0.80],
                         [0.75, 0.72, 0.65, 0.75, 0.74, 0.75],
                         [0.84, 0.58, 0.71, 0.83, 0.81, 0.80],
                         [0.87, 0.59, 0.71, 0.88, 0.82, 0.82],
                         [0.82, 0.62, 0.72, 0.86, 0.85, 0.81],
                         [0.92, 0.61, 0.71, 0.85, 0.82, 0.86]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def effusion_resnet():

    # order: vindr, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.97, 0.72, 0.78, 0.81, 0.72, 0.89],
                         [0.96, 0.81, 0.84, 0.87, 0.75, 0.94],
                         [0.97, 0.81, 0.87, 0.89, 0.84, 0.95],
                         [0.98, 0.81, 0.87, 0.91, 0.83, 0.96],
                         [0.87, 0.74, 0.80, 0.83, 0.91, 0.90],
                         [0.95, 0.78, 0.85, 0.89, 0.77, 0.96]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()






def cardiomegaly_vit():

    # order: vindr, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.96, 0.77, 0.75, 0.70, 0.73, 0.84],
                         [0.92, 0.88, 0.81, 0.73, 0.72, 0.90],
                         [0.92, 0.87, 0.88, 0.75, 0.79, 0.89],
                         [0.94, 0.81, 0.82, 0.81, 0.80, 0.87],
                         [0.96, 0.83, 0.84, 0.79, 0.85, 0.88],
                         [0.93, 0.83, 0.83, 0.71, 0.76, 0.93]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def pneumonia_vit():

    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # vindr-pediatric
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.91, 0.72, 0.63, 0.55, 0.63, 0.76, 0.75],
                         [0.80, 0.80, 0.61, 0.56, 0.60, 0.69, 0.65],
                         [0.70, 0.59, 0.60, 0.48, 0.56, 0.64, 0.69],
                         [0.70, 0.55, 0.60, 0.72, 0.58, 0.74, 0.62],
                         [0.77, 0.56, 0.70, 0.72, 0.72, 0.76, 0.78],
                         [0.79, 0.67, 0.67, 0.63, 0.66, 0.91, 0.77],
                         [0.84, 0.64, 0.66, 0.65, 0.68, 0.78, 0.84]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def nofinding_vit():

    # order: vindr, vindr-pediatric, cxr14, chexpert, mimic, padchest

    # order:

    # vindr,
    # vindr-pediatric,
    # cxr14,
    # chexpert,
    # mimic,
    # padchest

    auc_list = np.array([[0.90, 0.60, 0.67, 0.82, 0.76, 0.79],
                         [0.75, 0.73, 0.67, 0.74, 0.76, 0.75],
                         [0.87, 0.59, 0.71, 0.84, 0.82, 0.81],
                         [0.89, 0.62, 0.71, 0.88, 0.83, 0.82],
                         [0.88, 0.61, 0.71, 0.86, 0.85, 0.82],
                         [0.91, 0.64, 0.71, 0.84, 0.82, 0.86]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()


def effusion_vit():

    # order: vindr, cxr14, chexpert, mimic, UKA, padchest

    # order:

    # vindr,
    # cxr14,
    # chexpert,
    # mimic,
    # UKA,
    # padchest

    auc_list = np.array([[0.97, 0.70, 0.78, 0.81, 0.72, 0.89],
                         [0.96, 0.81, 0.84, 0.87, 0.78, 0.94],
                         [0.97, 0.80, 0.88, 0.89, 0.84, 0.95],
                         [0.98, 0.81, 0.87, 0.90, 0.82, 0.95],
                         [0.91, 0.73, 0.81, 0.84, 0.91, 0.91],
                         [0.97, 0.79, 0.85, 0.88, 0.80, 0.96]])

    sns.set(font_scale=1.5)

    ax = sns.heatmap(data=auc_list, vmin=0.55, vmax=1, annot=True, fmt=".2f", cmap='Blues')
    ax.tick_params(axis='y', left=False, labelleft=False)
    ax.tick_params(axis='x', bottom=False, labelbottom=False, labelsize=5)

    plt.show()





if __name__ == '__main__':
    main_resnet()
    # main_vit()
    ###########################################################
    # cardiomegaly_resnet()
    # pneumonia_resnet()
    # nofinding_resnet()
    # effusion_resnet()
    ###########################################################
    # cardiomegaly_vit()
    # pneumonia_vit()
    # nofinding_vit()
    # effusion_vit()

