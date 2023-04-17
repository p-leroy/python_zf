import os

import matplotlib
import pandas as pd

import tools_zf as tools

matplotlib.use('Qt5Agg')

dir_ = r"C:\Scans\Cibles Leica\Export"
targets = os.path.join(dir_, "Cibles Leica.targets.txt")

# serial numbers
# Leica-TG-RENNES-1
# Leica-TG-RENNES-2
# Leica-TG-RENNES-3
# Leica-TG-RENNES-4

scans = {'1.zfs': (0, '1', 'Initial general scan'),
         '1_Selection_1.zfs': (1, '1_1', 'Initial state [extremely high]'),
         '1_Selection_2.zfs': (2, '1_2', 'Initial state [ultra high]'),
         '1_Selection_3.zfs': (3, '1_3', 'Initial state [ultra high]'),
         '1_Selection_4.zfs': (4, '1_4', 'Rotated + pivoted [extremely high]'),
         '1_Selection_5.zfs': (5, '1_5', 'Rotated + pivoted [ultra high]'),
         '1_Selection_6.zfs': (6, '1_6', 'Rotated + pivoted [ultra high]'),
         '1_Selection_7.zfs': (7, '1_7', 'Initial state [extremely high]'),
         '1_Selection_8.zfs': (8, '1_8', 'Initial state [ultra high]'),
         '1_Selection_9.zfs': (9, '1_9', 'Initial state [ultra high]')}

colors = {0: 'b', 1: 'b', 2: 'b', 3: 'b',
          4: 'r', 5: 'r', 6: 'r',
          7: 'g', 8: 'g', 9: 'g'}

target_labels = ['0_0', '2_1', '2_2', '1_3', '2_4', '2_5', '1_4', '0_1']

targets_and_scans = [('sphere_1', '0_0', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_1', '2_1', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_2', '2_2', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_3', '1_3', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_4', '0_2', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_5', '0_3', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('leica_6', '1_4', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)),
                     ('sphere_2', '0_1', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))]

with open(targets) as csvfile:
    df = pd.read_table(targets, names=['target_name', 'x', 'y', 'z', 'scan'], delimiter=';')

#%% build figures
tools.build_figures(targets_and_scans, df, scans, dir_, colors=colors)
