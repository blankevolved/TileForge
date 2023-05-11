from src.color import Fore, FULL_RESET, Back
import time
from src.tools import clear
from src.blocks import Block, Entity


class Map:
    def __init__(self, x: int, y: int, base_tile='-'):
        self.x_range = range(0, x)
        self.y_range = range(0, y)
        self.tile = base_tile
        self.f_color = Fore.DEFAULT
        self.b_color = Back.DEFAULT
        self.cords = {}
        for yr in self.y_range:
            for xr in self.x_range:
                self.cords[xr, yr] = {'tile': self.tile, 'f_color': self.f_color, 'b_color': self.b_color}

    def draw(self):
        for current_key in self.cords.keys():
            cord_key = self.cords.get(current_key)
            if current_key[0] == self.x_range[-1]:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='\n')
            else:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='')

    def draw_object(self, obj: Block | Entity | None, x: int, y: int):
        if obj is None:
            obj = self
        self.cords[x, y]['f_color'] = obj.f_color
        self.cords[x, y]['b_color'] = obj.b_color
        self.cords[x, y]['tile'] = obj.tile

        if obj is not None:
            obj.current_map = self
            obj.x = x
            obj.y = y

    def redraw(self, x_seconds: int = 1, add_inp: bool = False, inp_prompt: str = '>>> '):
        while True:
            clear()
            self.draw()
            if add_inp:
                input(inp_prompt)
            else:
                time.sleep(x_seconds)
