# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

#%%


def set_axis(ax, lim=2.5):
    ax.grid()
    ax.set_aspect('equal')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])


args = {'ha': "left",
        'va': "center",
        'color': 'green',
        'fontweight': 'bold'}

shift = 0.1

#%% alternate figure
for target, name, scans_containing_target in [targets_and_scans[1]]:
    print(target, name, scans_containing_target)
    # get the target under test, its name as a target in the scans, and the list of scans that contain it
    # for instance: physical target leica_3 is named target 2_6 in scans 0, 1 and 2
    # get the rows in the target list which contain the name
    lines = df[target_name == name]
    # keep only the lines related to scans which contain the physical target
    indexes = [idx for idx in lines.index if scans[lines.loc[idx]['scan']][0] in scans_containing_target]

    if 'sphere_' in target:
        lim = 0.5
    else:
        lim = 2

    f, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [5, 1]}, figsize=(10, 7))
    x_target, y_target, z_target = ((x[indexes] - np.mean(x[indexes])) * 1000,
                                    (y[indexes] - np.mean(y[indexes])) * 1000,
                                    (z[indexes] - np.mean(z[indexes])) * 1000)

    title = target + f' - scans {scans_containing_target}'
    f.suptitle(title)
    ax1.plot(x_target, y_target, 'o')
    for (xx, yy, idx) in zip(x_target, y_target, indexes):
        i = scans[lines.loc[idx]['scan']][0]
        ax1.text(xx + shift, yy, i, **args)
    ax1.set_xlabel('[x]', loc='right')
    ax1.set_ylabel('[y]', loc='top')
    set_axis(ax1, lim=lim)

    ax2.plot(np.zeros(z_target.shape), z_target, 'o')
    for (zz, idx)  in zip(z_target, indexes):
        i = scans[lines.loc[idx]['scan']][0]
        ax2.text(0, zz + shift, i, **args)
    ax2.set_ylabel('[z]', loc='top')
    ax2.grid()
    ax2.spines['bottom'].set_position('center')
    ax2.tick_params(bottom=False)
    ax2.tick_params(labelbottom=False)
    ax2.spines['top'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax2.spines['right'].set_color('none')
    ax2.set_aspect('equal')
    ax2.set_ylim([-lim, lim])

    # f.show()
    f.tight_layout()
    filename = os.path.join(dir_, title)
    f.savefig(filename)
