# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tools_zf as tools

matplotlib.use('Qt5Agg')

dir_ = r"C:\Scans\Test retournement cibles\Export"
targets = os.path.join(dir_, "Test retournement cibles.targets.txt")

scans = {'1_Selection_1.zfs': (0, '1_1', 'Leica 1 2 3 4 LaserScanning 1 2'),
         '1_Selection2_1.zfs': (1, '1_2', 'Leica 1 2 3 4 LaserScanning 1 2 rotated and pivoted'),
         '1_Selection3_1.zfs': (2, '1_3', 'Leica 1 2 3 4 LaserScanning 1 2 rotated and pivoted (initial state)'),
         '1_Selection_4.zfs': (3, '1_4', 'Leica 1 2 5 6 LaserScanning 3 4'),
         '1_Selection5_1.zfs': (4, '1_5', 'Leica 1 2 5 6 LaserScanning 3 4 [ultra high]'),
         '1_Selection6_1.zfs': (5, '1_6', 'Leica 1 2 5 6 LaserScanning 3 4 [ultra high] rotated and pivoted'),
         '1_Selection7_1.zfs': (6, '1_7', 'Leica 1 2 5 6 LaserScanning 3 4 [ultra high] rotated and pivoted (initial state)')}

colors = {0: 'b', 1: 'r', 2: 'b', 3: 'g',
          4: 'g', 5: 'k', 6: 'g'}

target_labels = ['4_0', '2_4', '2_5', '2_6', '2_1', '4_2', '2_3', '4_1']

targets_and_scans = [('sphere_1', '4_0', (0, 1, 2, 3, 4, 5, 6)),  # 0
                     ('sphere_2', '4_1', (0, 1, 2, 3, 4, 5, 6)),  # 1
                     ('leica_1', '2_4', (0, 1, 2, 3, 4, 5, 6)),  # 2
                     ('leica_2', '2_5', (0, 1, 2, 3, 4, 5, 6)),  # 3
                     ('leica_3', '2_6', (0, 1, 2)),  # 4
                     ('leica_4', '2_1', (0, 1, 2)),  # 5
                     ('leica_5', '2_6', (3, 4, 5, 6)),  # 6
                     ('leica_6', '2_1', (3, 4, 5, 6)),  # 7
                     ('laserscanning_1', '4_2', (0, 1, 2)),  # 8
                     ('laserscanning_2', '2_3', (0, 1, 2)),  # 9
                     ('laserscanning_3', '4_2', (3, 4, 5, 6)),  # 10
                     ('laserscanning_4', '2_3', (3, 4, 5, 6))]  # 11

with open(targets) as csvfile:
    df = pd.read_table(targets, names=['target_name', 'x', 'y', 'z', 'scan'], delimiter=';')

#%%
target_name = df['target_name']
x = df['x']
y = df['y']
z = df['z']
scan = df['scan']
target_list = target_name.unique()

#%% build figures
tools.build_figures(targets_and_scans, df, scans, dir_, colors=colors)
