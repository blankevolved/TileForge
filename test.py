from src.blocks import Block, Entity
from src.maps import Map
from src.color import Fore

new_map = Map(10, 5)

new_block = Block(f_color=Fore.RED)

new_entity = Entity()

new_map.draw_object(new_entity, 0, 0)

new_entity.move('x', '-')

new_map.redraw(add_inp=True)
