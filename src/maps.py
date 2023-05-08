from src.color import F_DEFAULT, FULL_RESET, B_DEFAULT


class Map:
    def __init__(self, x: int, y: int, base_tile='-'):
        self.x_range = range(1, x+1)
        self.y_range = range(1, y+1)
        self.base_tile = base_tile
        self.f_base_color = F_DEFAULT
        self.b_base_color = B_DEFAULT
        self.cords = {}
        for yr in self.y_range:
            for xr in self.x_range:
                self.cords[xr, yr] = {'tile': self.base_tile, 'f_color': self.f_base_color, 'b_color': self.b_base_color}

    def print(self):
        for current_key in self.cords.keys():
            cord_key = self.cords.get(current_key)
            if current_key[0] == self.x_range[-1]:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='\n')
            else:
                print(f"{cord_key['f_color']}{cord_key['b_color']}{cord_key['tile']}{FULL_RESET}", end='')



