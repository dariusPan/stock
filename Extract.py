import matplotlib
import numpy as np

>>> info = {}
with open('scoring_info.txt') as input_file:
    for line in input_file:
        player, stats, outcome, date = (
            item.strip() for item in line.split('-', 3))
        stats = dict(zip(('kills', 'deaths', 'assists'),
                          map(int, stats.split('/'))))
        date = tuple(map(int, date.split('-')))
        info[player] = dict(zip(('stats', 'outcome', 'date'),
                                (stats, outcome, date)))

print('info:')
for player, record in info.items():
    print('  player %r:' % player)
    for field, value in record.items():
        print('    %s: %s' % (field, value))
