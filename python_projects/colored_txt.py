#import libraries
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

print(Fore.BLUE+Back.YELLOW+'something obvious'+ Fore.YELLOW+ Back.BLUE+'  something more obvious'+ Back.CYAN+'  think something'+Fore.RED+Back.GREEN+'  got anything?')
