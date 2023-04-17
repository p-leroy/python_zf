import os

import matplotlib
import pandas as pd

import tools_zf as tools

matplotlib.use('Qt5Agg')

dir_ = r'C:\Scans\Laser scanning 6\Export'
targets = os.path.join(dir_, "Laser scanning 6.targets.txt")

scans = {'1.zfs': (0, '1', 'Initial general scan'),
         '1_Selection_1.zfs': (1, '1_1', 'Initial state [extremely]'),
         '1_Selection_2.zfs': (2, '1_2', 'Initial state [ultra]'),
         '1_Selection_3.zfs': (3, '1_3', 'Initial state [ultra]'),
         '1_Selection_4.zfs': (4, '1_4', 'Initial state [ultra]'),  # bicycle
         '1_Selection_5.zfs': (5, '1_5', 'Rotated + pivoted [extremely]'),
         '1_Selection_6.zfs': (6, '1_6', 'Rotated + pivoted [ultra]'),
         '1_Selection_7.zfs': (7, '1_7', 'Rotated + pivoted [ultra]'),
         '1_Selection_8.zfs': (8, '1_8', 'Initial state [extremely]'),  # car
         '1_Selection_9.zfs': (9, '1_9', 'Initial state [ultra]'),
         '1_Selection_10.zfs': (10, '1_10', 'Initial state [ultra]'),
         '1_Selection_11.zfs': (11, '1_11', 'Initial state [extremely]')}

colors = {1: 'b', 2: 'b', 3: 'b', 4: 'b',
          5: 'r', 6: 'r', 7: 'r',
          8: 'g', 9: 'g', 10: 'g', 11: 'g'}

target_labels = ['_10_1', '9_1', '_10_0']

targets_and_scans = [('sphere_1', '_10_1', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)),
                     ('ls_6', '9_1', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)),
                     ('sphere_2', '_10_0', (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))]

with open(targets) as csvfile:
    df = pd.read_table(targets, names=['target_name', 'x', 'y', 'z', 'scan'], delimiter=';')

#%%
tools.build_figures(targets_and_scans, df, scans, dir_, colors=colors)

#%%
target_name = df['target_name']
x = df['x']
y = df['y']
z = df['z']
scan = df['scan']
target_list = target_name.unique()

#%%
target = '9_1'
x_target = x.where(target_name == target)
y_target = y.where(target_name == target)
z_target = z.where(target_name == target)
tools.build_figures([targets_and_scans[1]], df, scans, dir_, colors=colors, lim=10)