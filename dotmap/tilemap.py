
import yaml

try:
    from render import Sprite
except ImportError as ie:
    from .render import Sprite


class Tile(object):


    def __init__(self, index, name, sprite, data={}):
        self.index = index
        self.name = name
        if isinstance(sprite, Sprite):
            self.sprite = sprite
        else:
            self.sprite = Sprite(sprite['char'], sprite['background'], sprite['foreground'])
        self.data = data


    def __repr__(self):
        return '<Tile: {0} {1}>'.format(self.name, self.sprite)
    
    def __str__(self):
        return repr(self)
    

class TileMap(object):


    def __init__(self, map_, tileset):
        self.map = map_
        self.tileset = tileset
    

    @staticmethod
    def from_files(map_path, tileset_path):
        tiles = []
        for tile in load_tileset(tileset_path):
            tiles.append( Tile(**tile) )

        return TileMap(load_map(map_path), { tile.index: tile for tile in tiles })


    def __repr__(self):
        maps = '<TileMap>'
        for row in self.map:
            maps+='\n'
            for item in row:
                maps += self.tileset[item].sprite.texture
        return maps.strip()



def load_map(path):
    map_ = []
    mapcsv = None
    with open(path, 'r') as mapfile:
        for row in mapfile.read().split('\n'):
            map_.append([ int(x) for x in row.split(',') ])
    return map_


def load_tileset(path):
    tileset = None
    with open(path, 'r', encoding='utf-8') as tilefile:
        tileset = yaml.load(tilefile.read())
    return tileset


if __name__ == '__main__':
    import sys

    if sys.argv[1] in ('tileset', 'map', 'tilemap'):
       
        if sys.argv[1] == 'map':
            print(load_map(sys.argv[2]))
        
        elif sys.argv[1] == 'tileset':
            tiles = []
            tileset = load_tileset(sys.argv[2])
            print(tileset)

            for tile in tileset:
                tiles.append( Tile(**tile) )
            
            tileset = { tile.index: tile for tile in tiles }
            print(tileset)
        
        else:
            maps = TileMap.from_files(sys.argv[2], sys.argv[3])
            print(maps)