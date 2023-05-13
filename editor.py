from maps import Map
from modules.JSave.jsave import save_to_file, load_from_file
import os
from color import FULL_RESET, Fore, Back
import json

VER_NUM = 2

cur_map = None

cur_cord = None

cur_map_name = None


def version():
    print(f'Tile Forge Editor: v{VER_NUM}')


def load_map(file_name: str = ''):
    if file_name == '':
        file_name = input('File name: ')
    global cur_map, cur_map_name
    try:
        loaded_map = load_from_file(f'map_files/{file_name}.json')
        cur_map = Map(loaded_map['x'], loaded_map['y'], loaded_map['tile'], loaded_map['scale'])
        cur_map.f_color = loaded_map['f_color']
        cur_map.b_color = loaded_map['b_color']
        cur_map_name = file_name
        for c in loaded_map['cords']:
            cur_map.cords[tuple(json.loads(c))] = {'tile': loaded_map['cords'][c]['tile'], 'f_color': loaded_map['cords'][c]['f_color'], 'b_color': loaded_map['cords'][c]['b_color']}

    except TypeError:
        if '.json' in file_name:
            print(f'Cant load file, you dont need to add ".json" to "{file_name}"')
        else:
            print(f'Cant load file, check if the file is in the "map_files" folder or if a map with the name "{file_name}" exists')


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
    new_cords = {}
    for c in cur_map.cords:
        new_cords[json.dumps(c)] = {'tile': cur_map.tile, 'f_color': cur_map.f_color, 'b_color': cur_map.b_color}
    json_save = {
        'x': cur_map.x,
        'y': cur_map.y,
        'scale': cur_map.scale,
        'cords': new_cords,
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


# noinspection PyUnresolvedReferences
def edit_property():
    global cur_map, cur_map_name

    if type(cur_map) == Map and cur_cord is not None:
        print('tile\nf_color\nb_color')
        inp = input('Option to change: ')

        if inp == 'tile':
            new = input(f'New value for {inp}: ')
            cur_map.cords[cur_cord]['tile'] = new

        if inp == 'f_color':
            new = input(f'New value for {inp}: ')
            cur_map.cords[cur_cord]['f_color'] = Fore.JSON[new]

        if inp == 'b_color':
            new = input(f'New value for {inp}: ')
            cur_map.cords[cur_cord]['b_color'] = Back.JSON[new]

        new_cords = {}
        for c in cur_map.cords:
            new_cords[json.dumps(c)] = {'tile': cur_map.cords[c]['tile'], 'f_color': cur_map.cords[c]['f_color'], 'b_color': cur_map.cords[c]['b_color']}

        new_cords[json.dumps(cur_cord)] = {'tile': cur_map.cords[cur_cord]['tile'], 'f_color': cur_map.cords[cur_cord]['f_color'], 'b_color': cur_map.cords[cur_cord]['b_color']}

        json_save = {
            'x': cur_map.x,
            'y': cur_map.y,
            'scale': cur_map.scale,
            'cords': new_cords,
            'f_color': cur_map.f_color,
            'b_color': cur_map.b_color,
            'tile': cur_map.tile
        }
        save_to_file(f'map_files/{cur_map_name}.json', json_save)

        load_map(str(cur_map_name))

    elif type(cur_map) == Map:
        print('x\ny\ntile\nrange\nf_color\nb_color')
        inp = input('Option to change: ')

        if inp == 'x':
            new = int(input(f'New value for {inp}: '))
            cur_map.x = new
            cur_map.x_range = range(0, new)

        if inp == 'y':
            new = int(input(f'New value for {inp}: '))
            cur_map.y = new
            cur_map.y_range = range(0, new)

        if inp == 'range':
            new = int(input(f'New value for {inp}: '))
            cur_map.range = new

        if inp == 'tile':
            new = input(f'New value for {inp}: ')
            cur_map.tile = new

        if inp == 'f_color':
            print('Warning, this will turn all colors on the map to this color!')
            new = input(f'New value for {inp}: ')
            cur_map.f_color = Fore.JSON[new]

        if inp == 'b_color':
            print('Warning, this will turn all colors on the map to this color!')
            new = input(f'New value for {inp}: ')
            cur_map.b_color = Back.JSON[new]

        new_cords = {}

        for c in cur_map.cords:
            new_cords[json.dumps(c)] = {'tile': cur_map.tile, 'f_color': cur_map.f_color, 'b_color': cur_map.b_color}

        json_save = {
            'x': cur_map.x,
            'y': cur_map.y,
            'scale': cur_map.scale,
            'cords': new_cords,
            'f_color': cur_map.f_color,
            'b_color': cur_map.b_color,
            'tile': cur_map.tile
        }
        save_to_file(f'map_files/{cur_map_name}.json', json_save)

        load_map(str(cur_map_name))

    else:
        print('please load or create a map')


# noinspection PyUnresolvedReferences
def select_cord():
    if type(cur_map) == Map:
        global cur_cord
        print(f'Max X: {cur_map.x_range[-1]}')
        print(f'Max Y: {cur_map.y_range[-1]}')
        print('Set both X and Y to -1 to select whole map')
        cord_x = input('X cord: ')
        cord_y = input('Y cord: ')
        try:
            int_x = int(cord_x)
            int_y = int(cord_y)

            if (int_x, int_y) in cur_map.cords:
                cur_cord = (int_x, int_y)
            elif int_x == -1 and int_y == -1:
                cur_cord = None
            else:
                print("that isn't a valid cord")
        except TypeError:
            print('x or y was not an int')
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
    },
    {
        'cmds': ['sc'],
        'exec': select_cord
    }
]

shortcuts = """v> show version\t\tc> create new map\t\tl> load map\t\tp> list properties of map
e> edit a property\t\tt> test what the map will look like\t\tsc> select a coordinate"""


def check_inp(input_object):
    for c in enumerate(COMMAND_LIST):  # check command list for avail commands
        for cc in COMMAND_LIST[c[0]]['cmds']:  # get act cmd names
            if input_object == cc:  # check if inp == cmd name
                COMMAND_LIST[c[0]]['exec']()  # execute function for cmd


def main():
    print()

    print(shortcuts)

    inp = input(f'{cur_map_name}/{cur_cord}> ')

    check_inp(inp)


if __name__ == '__main__':
    while True:
        main()
else:
    quit('RUN editor.py NORMALLY, NOT AS AN IMPORT')
