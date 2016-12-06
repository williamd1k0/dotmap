
from colorama import init
from colorama import Fore, Back, Style
#init()


BACK = {
    'black': Back.BLACK,
    'red': Back.RED,
    'green': Back.GREEN,
    'yellow': Back.YELLOW,
    'blue': Back.BLUE,
    'magenta': Back.MAGENTA,
    'cyan': Back.CYAN,
    'white': Back.WHITE,
}

FORE = {
    'black': Fore.BLACK,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
}


class Sprite(object):


    def __init__(self, texture, background, modulate):
        self.texture = texture
        self.bg = background
        self.fg = modulate


    def __repr__(self):
        return '{0}{1}{2}{3}'.format(BACK[self.bg], FORE[self.fg], self.texture, Style.RESET_ALL)


class Canvas(object):


    def __init__(self, size=(25,10), clear=Sprite('*', 'white', 'red')):
        self.size = size
        self.clear = clear
        self.render_matrix = [ [clear for col in range(size[0])] for row in range(size[1]) ]

    @staticmethod
    def from_tilemap(tilemap):
        return Canvas((len(tilemap.map[0]), len(tilemap.map)), tilemap.tileset[0].sprite)

    
    def __repr__(self):
        matrix = '<Canvas({0})>'.format(self.size)
        for row in self.render_matrix:
            matrix += '\n'
            for col in row:
                matrix += repr(col)
        return matrix.strip()



if __name__ == '__main__':

    cv = Canvas()
    print(cv)
