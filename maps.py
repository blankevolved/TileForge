from color import Fore, FULL_RESET, Back
import time
from tools import clear
from blocks import Block, Entity


class Map:
    def __init__(self, x: int, y: int, base_tile='-', scale: int = 1):
        self.x = x
        self.y = y
        self.x_range = range(0, x)
        self.y_range = range(0, y)
        self.tile = base_tile
        self.f_color = Fore.DEFAULT
        self.b_color = Back.DEFAULT
        self.cords = {}
        self.scale = scale
        for yr in self.y_range:
            for xr in self.x_range:
                self.cords[xr, yr] = {'tile': self.tile, 'f_color': self.f_color, 'b_color': self.b_color}

    def draw(self):
        row = ''
        out = ''
        n = 0
        for current_key in self.cords.keys():
            cord_key = self.cords.get(current_key)
            if current_key[0] == self.x_range[-1]:
                row = row + f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}" * self.scale
                while n < self.scale:
                    out = out + row + '\n'
                    n += 1
                else:
                    n = 0
                row = ''
            else:
                row = row + f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}" * self.scale

        return out

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
            print(self.draw())
            if add_inp:
                input(inp_prompt)
            else:
                time.sleep(x_seconds)
