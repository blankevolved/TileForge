from src.maps import Map
from src.color import Fore, Back


class Block:
    def __init__(self, f_color=Fore.DEFAULT, b_color=Back.DEFAULT, tile='='):
        self.f_color = f_color
        self.b_color = b_color
        self.tile = tile

    def draw(self, drawing_map: Map, x: int, y: int):
        drawing_map.cords[x, y]['f_color'] = self.f_color
        drawing_map.cords[x, y]['b_color'] = self.b_color
        drawing_map.cords[x, y]['tile'] = self.tile




