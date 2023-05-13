from color import Fore, Back


class Block:
    def __init__(self, f_color=Fore.DEFAULT, b_color=Back.DEFAULT, tile='='):
        self.f_color = f_color
        self.b_color = b_color
        self.tile = tile


class Entity(Block):
    def __init__(self, f_color=Fore.DEFAULT, b_color=Back.DEFAULT, tile='='):
        super().__init__(f_color=f_color, b_color=b_color, tile=tile)
        self.x = None
        self.y = None
        self.current_map = None

    def move(self, x_y: str, plus_minus: str):
        if plus_minus != '-' or plus_minus != '+':
            print('pick "+" or "-"')
        if x_y == 'x':
            self.current_map.draw_object(None, self.x, self.y)
            self.current_map.draw_object(self, eval(f'{self.x}{plus_minus}1'), self.y)
        elif x_y == 'y':
            self.current_map.draw_object(None, self.x, self.y)
            self.current_map.draw_object(self, self.x, eval(f'{self.y}{plus_minus}1'))
        else:
            print('pick "x" or "y"')

