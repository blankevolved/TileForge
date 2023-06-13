from color import Fore, FULL_RESET, Back
import time
from tools import clear
from blocks import Block, Entity
import json
from modules.JSave.jsave import load_from_file


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

        else:
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


def load_map(file_name: str = ''):
    if file_name == '':
        file_name = input('File name: ')
    try:
        loaded_map = load_from_file(f'map_files/{file_name}.json')
        cur_map = Map(loaded_map['x'], loaded_map['y'], loaded_map['tile'], loaded_map['scale'])
        cur_map.f_color = loaded_map['f_color']
        cur_map.b_color = loaded_map['b_color']
        for c in loaded_map['cords']:
            cur_map.cords[tuple(json.loads(c))] = {'tile': loaded_map['cords'][c]['tile'], 'f_color': loaded_map['cords'][c]['f_color'], 'b_color': loaded_map['cords'][c]['b_color']}
        return cur_map

    except TypeError:
        if '.json' in file_name:
            print(f'Cant load file, you dont need to add ".json" to "{file_name}"')
        else:
            print(f'Cant load file, check if the file is in the "map_files" folder or if a map with the name "{file_name}" exists')
