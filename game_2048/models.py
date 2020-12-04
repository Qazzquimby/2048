import collections
import typing as t

BOARD_WIDTH = 4
BOARD_HEIGHT = 4
Board = t.List[t.List[int]]

Point = collections.namedtuple('Point', ['x', 'y'])
