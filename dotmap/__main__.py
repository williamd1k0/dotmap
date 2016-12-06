
import sys
from .render import Canvas
from .tilemap import TileMap


maps = TileMap.from_files(sys.argv[1], sys.argv[2])

cv = Canvas.from_tilemap(maps)

for row in range(len(maps.map)):
    for col in range(len(maps.map[row])):
        cv.render_matrix[row][col] = maps.tileset[maps.map[row][col]].sprite

print(cv)