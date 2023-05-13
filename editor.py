from maps import Map
from modules.JSave.jsave import save_to_file, load_from_file
import os
from color import FULL_RESET, Fore, Back

VER_NUM = 1

cur_map = None

cur_map_name = None


def version():
    print(f'Editor Version: v{VER_NUM}')


def load_map():
    file_name = input('File name: ')
    global cur_map, cur_map_name
    try:
        loaded_map = load_from_file(f'map_files/{file_name}.json')
        cur_map_name = file_name
        cur_map = Map(loaded_map['x'], loaded_map['y'], loaded_map['tile'], loaded_map['scale'])
        cur_map.f_color = loaded_map['f_color']
        cur_map.b_color = loaded_map['b_color']
        # noinspection PyUnresolvedReferences
        for yr in cur_map.y_range:
            # noinspection PyUnresolvedReferences
            for xr in cur_map.x_range:
                # noinspection PyUnresolvedReferences
                cur_map.cords[xr, yr] = {'tile': cur_map.tile, 'f_color': cur_map.f_color, 'b_color': cur_map.b_color}

    except TypeError:
        print('cant load file')


def test_map():
    if type(cur_map) == Map:
        # noinspection PyUnresolvedReferences
        print(cur_map.draw())
    else:
        print('please load or create a map')


def create_map():
    global cur_map, cur_map_name

    file_name = input('File name: ')
    x_val = int(input('Width: '))
    y_val = int(input('Height: '))
    scale_val = int(input('Scale: '))
    cur_map = Map(x_val, y_val, scale=scale_val)
    cur_map_name = file_name
    json_save = {
        'x': cur_map.x,
        'y': cur_map.y,
        'scale': cur_map.scale,
        'f_color': cur_map.f_color,
        'b_color': cur_map.b_color,
        'tile': cur_map.tile
    }
    try:
        save_to_file(f'map_files/{file_name}.json', json_save)
    except FileNotFoundError:
        os.mkdir('map_files')
        save_to_file(f'map_files/{file_name}.json', json_save)


def list_props():
    if type(cur_map) == Map:
        # noinspection PyUnresolvedReferences
        print(f"""Properties:
X: {cur_map.x}
Y: {cur_map.y}
Base Tile: {cur_map.tile}
Base Fore Color: {cur_map.f_color} COLOR {FULL_RESET}
Base Back Color: {cur_map.b_color} COLOR {FULL_RESET}
Scale: {cur_map.scale}""")
    else:
        print('please load or create a map')


def edit_property():
    if type(cur_map) == Map:
        print('x\ny\ntile\nf_color\nb_color\nrange')
        inp = input('Option to change: ')

        if inp == 'x':
            new = int(input(f'New value for {inp}: '))
            cur_map.x = new
            cur_map.x_range = range(0, new)

        if inp == 'y':
            new = int(input(f'New value for {inp}: '))
            cur_map.y = new
            cur_map.y_range = range(0, new)

        if inp == 'tile':
            new = input(f'New value for {inp}: ')
            cur_map.tile = new

        if inp == 'f_color':
            new = input(f'New value for {inp}: ')
            cur_map.f_color = Fore.JSON[new]

        if inp == 'b_color':
            new = input(f'New value for {inp}: ')
            cur_map.b_color = Back.JSON[new]

        if inp == 'range':
            new = int(input(f'New value for {inp}: '))
            cur_map.range = new

        # noinspection PyUnresolvedReferences
        for yr in cur_map.y_range:
            # noinspection PyUnresolvedReferences
            for xr in cur_map.x_range:
                # noinspection PyUnresolvedReferences
                cur_map.cords[xr, yr] = {'tile': cur_map.tile, 'f_color': cur_map.f_color, 'b_color': cur_map.b_color}

        # noinspection PyUnresolvedReferences
        json_save = {
            'x': cur_map.x,
            'y': cur_map.y,
            'scale': cur_map.scale,
            'f_color': cur_map.f_color,
            'b_color': cur_map.b_color,
            'tile': cur_map.tile
        }

        save_to_file(f'map_files/{cur_map_name}.json', json_save)

    else:
        print('please load or create a map')


COMMAND_LIST = [
    {
        'cmds': ['v'],
        'exec': version
    },
    {
        'cmds': ['c'],
        'exec': create_map
    },
    {
        'cmds': ['l'],
        'exec': load_map
    },
    {
        'cmds': ['debug'],
        'exec': lambda: exec(input())
    },
    {
        'cmds': ['p'],
        'exec': list_props
    },
    {
        'cmds': ['e'],
        'exec': edit_property
    },
    {
        'cmds': ['t'],
        'exec': test_map
    }
]

shortcuts = """v> show version\t\tc> create new map\t\tl> load map\t\tp> list properties of map\t\te> edit a property\t\tt> test what the map will look like"""


def check_inp(input_object):
    for c in enumerate(COMMAND_LIST):  # check command list for avail commands
        for cc in COMMAND_LIST[c[0]]['cmds']:  # get act cmd names
            if input_object == cc:  # check if inp == cmd name
                COMMAND_LIST[c[0]]['exec']()  # execute function for cmd


def main():
    print()

    print(shortcuts)

    inp = input(f'{cur_map_name}> ')

    check_inp(inp)


if __name__ == '__main__':
    while True:
        main()
else:
    quit('RUN editor.py NORMALLY, NOT AS AN IMPORT')
