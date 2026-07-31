import colorama
import time

from colorama import init, Fore, Style

init(autoreset=True)

TITLE = Fore.CYAN + Style.BRIGHT
INFO = Fore.YELLOW + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
INPUT = Fore.WHITE + Style.BRIGHT
MSG = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
HEART = Fore.RED + Style.BRIGHT

print(TITLE + '=' * 50)
print(TITLE + '               Sistema iniciado')
print(TITLE + '=' * 50)
time.sleep(1.0)

print(INFO + '\nAnalisando usuários', end='')

for i in range(10):
    print(INFO + '.', end='', flush=True)
    time.sleep(0.5)

print('\n')

nome = input(INPUT + 'Digite o seu nome: ').strip().title()

print(INFO +'\nValidando informações', end='')

for _ in range(10):
    print(INFO + '.', end='', flush=True)
    time.sleep(0.5)

print('\n')

time.sleep(1.5)

print(SUCCESS + 'Resultado encontrado!')
time.sleep(1.0)

print(MSG + f'\nOlá {nome}')
time.sleep(1.5)

print(MSG + f'\nApós uma análise completa...')
time.sleep(1.5)

print(MSG + f'\nFoi identificado que...')
time.sleep(1.5)

print(MSG + f'\nVocê é o amor da minha vida nessa vida e em todas as outras vidas existentes 🪐❤️')
time.sleep(1.5)

print(MSG + f'\nTe amo muito minha vida ❤️')
time.sleep(1.5)

print(HEART + r"""
           *****     *****
         ********* *********
        *********************
         *******************
           ***************
             ***********
               *******
                 ***
                  *
""")

input(SUCCESS + '\nAperte Enter...para finalizar o programa!')
