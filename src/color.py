import colorama as c

FULL_RESET = f'{c.Fore.RESET}{c.Back.RESET}'


class Fore:
    DEFAULT = c.Fore.RESET
    RED = c.Fore.RED
    BLUE = c.Fore.BLUE
    YELLOW = c.Fore.YELLOW
    GREEN = c.Fore.GREEN
    CYAN = c.Fore.CYAN
    MAGENTA = c.Fore.MAGENTA
    BLACK = c.Fore.BLACK
    WHITE = c.Fore.WHITE

    L_RED = c.Fore.LIGHTRED_EX
    L_BLUE = c.Fore.LIGHTBLUE_EX
    L_YELLOW = c.Fore.LIGHTYELLOW_EX
    L_GREEN = c.Fore.LIGHTGREEN_EX
    L_CYAN = c.Fore.LIGHTCYAN_EX
    L_MAGENTA = c.Fore.LIGHTMAGENTA_EX
    L_BLACK = c.Fore.LIGHTBLACK_EX
    L_WHITE = c.Fore.LIGHTWHITE_EX


class Back:
    DEFAULT = c.Back.RESET
    RED = c.Back.RED
    BLUE = c.Back.BLUE
    YELLOW = c.Back.YELLOW
    GREEN = c.Back.GREEN
    CYAN = c.Back.CYAN
    MAGENTA = c.Back.MAGENTA
    BLACK = c.Back.BLACK
    WHITE = c.Back.WHITE

    L_RED = c.Back.LIGHTRED_EX
    L_BLUE = c.Back.LIGHTBLUE_EX
    L_YELLOW = c.Back.LIGHTYELLOW_EX
    L_GREEN = c.Back.LIGHTGREEN_EX
    L_CYAN = c.Back.LIGHTCYAN_EX
    L_MAGENTA = c.Back.LIGHTMAGENTA_EX
    L_BLACK = c.Back.LIGHTBLACK_EX
    L_WHITE = c.Back.LIGHTWHITE_EX


class Style:
    BRIGHT = c.Style.BRIGHT
    DIM = c.Style.DIM
    NORMAL = c.Style.NORMAL
