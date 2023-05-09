from src.blocks import Block
from src.maps import Map
from src.color import Fore

new_map = Map(10, 5)

new_block = Block(f_color=Fore.RED)

new_block.draw(new_map, 0, 0)

new_map.redraw()
