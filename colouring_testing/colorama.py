#
#THIS CODE DOES NOT WORK UNLESS INSTALL IN BASH "pip install colorama"
#


from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset after each print

print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.YELLOW + Style.BRIGHT + "This is bright yellow text")
