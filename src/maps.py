from src.color import Fore, FULL_RESET, Back
import time
from src.tools import clear


class Map:
    def __init__(self, x: int, y: int, base_tile='-'):
        self.x_range = range(0, x)
        self.y_range = range(0, y)
        self.base_tile = base_tile
        self.f_base_color = Fore.DEFAULT
        self.b_base_color = Back.DEFAULT
        self.cords = {}
        for yr in self.y_range:
            for xr in self.x_range:
                self.cords[xr, yr] = {'tile': self.base_tile, 'f_color': self.f_base_color, 'b_color': self.b_base_color}

    def draw(self):
        for current_key in self.cords.keys():
            cord_key = self.cords.get(current_key)
            if current_key[0] == self.x_range[-1]:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='\n')
            else:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='')

    def redraw(self, x_seconds: int, add_inp: bool = False, inp_prompt: str = '>>> '):
        while True:
            clear()
            time.sleep(x_seconds)
            self.draw()
            if add_inp:
                input(inp_prompt)
