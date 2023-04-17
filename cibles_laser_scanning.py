import os

import matplotlib
import pandas as pd

import tools_zf as tools

matplotlib.use('Qt5Agg')

dir_ = r"C:\Scans\Cibles laser scanning\Export"
targets = os.path.join(dir_, "Cibles laser scanning.targets.txt")

scans = {'1.zfs': (0, '1', 'Initial general scan'),
         '1_Selection_2.zfs': (1, '1_2', 'Initial state [ultra]'),
         '1_Selection_3.zfs': (2, '1_3', 'Initial state [extremely]'),
         '1_Selection_4.zfs': (3, '1_4', 'Initial state [ultra]'),
         '1_Selection_5.zfs': (4, '1_5', 'Rotated + pivoted [extremely]'),  # top of the targed missed :1 5 6
         '1_Selection_6.zfs': (5, '1_6', 'Rotated + pivoted [ultra]'),  # OK
         '1_Selection_7.zfs': (6, '1_7', 'Rotated + pivoted [extremely]'),  # OK
         '1_Selection_8.zfs': (7, '1_8', 'Rotated + pivoted [extremely]'),
         '1_Selection_9.zfs': (8, '1_9', 'Rotated + pivoted [extremely]'),
         '1_Selection_10.zfs': (9, '1_10', 'Rotated + pivoted [ultra]'),  # OK
         '1_Selection_11.zfs': (10, '1_11', 'Initial state [extremely]'),
         '1_Selection_12.zfs': (11, '1_12', 'Initial state [extremely]'),
         '1_Selection_13.zfs': (12, '1_13', 'Initial state [ultra]'),  # fire mens cross
         '1_Selection_14.zfs': (13, '1_14', 'Initial state [ultra]')}

colors = {1: 'b', 2: 'b', 3: 'b',
          4: 'r', 5: 'r', 6: 'r', 7: 'r', 8: 'r', 9: 'r',
          10: 'g', 11: 'g', 12: 'g', 13: 'g'}

target_labels = ['2_0', '7_1', '3_4', '3_3', '3_5', '1_1', '7_3', '1_2', '2_1']

targets_and_scans = [('sphere_1', '2_0', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_1', '7_1', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_2', '3_4', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_3', '3_3', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_4', '3_5', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_5', '1_1', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_6', '7_3', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('ls_7', '1_2', (1, 2, 3, 5, 6, 9, 10, 11, 13)),
                     ('sphere_2', '2_1', (1, 2, 3, 5, 6, 9, 10, 11, 13))]

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
target = '1_2'
x_target = x.where(target_name == target)
y_target = y.where(target_name == target)
z_target = z.where(target_name == target)
tools.build_figures([targets_and_scans[6]], df, scans, dir_, colors=colors, lim=10)