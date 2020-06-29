from tqdm import trange
from colorama import Fore

for i in trange(int(7e7),
    bar_format="{l_bar}%s{bar}%s{r_bar}"%(Fore.BLUE,Fore.RESET)):
    pass