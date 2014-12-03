import matplotlib.pyplot as plt
import pycelle
import numpy as np

from mpl_toolkits.axes_grid1 import ImageGrid


rules = [45, 90, 105, 110, 150]

f = plt.figure(1, (8,10))
grid = ImageGrid(f, 111, # similar to subplot(111)
                 nrows_ncols = (5, 3),
                 axes_pad=0.2, # pad between axes in inch.
                )
pattern = np.zeros(50)
pattern = '1001' * 50
pattern = np.array(map(int, pattern)[:50])

ics = ['single', pattern, 'random']
for i, rule in enumerate(rules):
    for j, ic in enumerate(ics):
        x = pycelle.ECA(rule, (38, 50), ic=ic)
        ax = grid[len(ics)*i + j]

        x.evolve(ax=ax)
        ax.set_ylabel('')
        ax.set_xlabel('')
        ax.set_title('')
        ax.set_xticks([])
        ax.set_yticks([])

        for spine in ax.spines.values():
            spine.set_color('red')

grid[0].set_title('Single Black Square')
grid[1].set_title('BWWB...')
grid[2].set_title('Random')
f.suptitle('Initial Row', fontsize=14)

for i, rule in enumerate(rules):
    grid[len(ics)*i].set_ylabel('Rule {0}'.format(rule),
                         rotation='horizontal', horizontalalignment='right')

plt.savefig('WorksheetAnswers.pdf')
