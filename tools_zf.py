import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Qt5Agg')


def set_axis(ax, lim=2.5):
    ax.grid()
    ax.set_aspect('equal')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])


def build_figures(targets_and_scans, df, scans, odir, shift=0.1, colors=None):

    args = {'ha': "left",
            'va': "center",
            'fontweight': 'bold'}
    color = 'green'  # default color for points and labels

    target_name = df['target_name']
    x = df['x']
    y = df['y']
    z = df['z']

    for target, name, scans_containing_target in targets_and_scans:
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
        remaining_scans = [scans[lines.loc[idx]['scan']][0] for idx in indexes]

        title = target + f' - scans {scans_containing_target}'
        f.suptitle(title)
        for xx, yy, idx in zip(x_target, y_target, indexes):
            i = scans[lines.loc[idx]['scan']][0]
            if colors is not None:
                color = colors[i]
            args['color'] = color
            ax1.plot(xx, yy, 'o', c=color)
            ax1.text(xx + shift, yy, i, **args)
        ax1.set_xlabel('[x]', loc='right')
        ax1.set_ylabel('[y]', loc='top')
        set_axis(ax1, lim=lim)

        for zz, idx in zip(z_target, indexes):
            i = scans[lines.loc[idx]['scan']][0]
            if colors is not None:
                color = colors[i]
            args['color'] = color
            ax2.plot(0, zz, 'o', c=color)
            ax2.text(0 + shift, zz + shift, i, **args)
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
        filename = os.path.join(odir, title)
        f.savefig(filename)