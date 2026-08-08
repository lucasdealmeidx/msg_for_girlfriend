import colorama
import time
from colorama import init, Fore, Style

init(autoreset=True)

TITLE = Fore.LIGHTMAGENTA_EX+ Style.BRIGHT
INFO = Fore.YELLOW + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
INPUT = Fore.WHITE + Style.BRIGHT
MSG = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
HEART = Fore.RED + Style.BRIGHT


def carregamento(mensagem, cor):
    print(mensagem, end='')

    for _ in range(5):
        print(cor + '.', end='', flush=True)
        time.sleep(0.5)
    print()

carregamento(TITLE + '\nInicializando sistema', TITLE)
time.sleep(1.0)

print(SUCCESS + '✔ Sistema iniciado!')
time.sleep(1.0)
print()

print(TITLE + '╔════════════════════════════════════════════════════════════════════╗')
print(TITLE + '║                                                                    ║')
print(TITLE + '║                      MSG PARA SEU LOVEZINHO <3                     ║')
print(TITLE + '║                                                                    ║')
print(TITLE + '╚════════════════════════════════════════════════════════════════════╝')
time.sleep(1.0)

carregamento(TITLE +'\nAnalisando usuários', TITLE)
time.sleep(1.0)

print(SUCCESS + '✔ Dados processados!')
time.sleep(1.0)

print()

nome = input(INPUT + 'Digite o seu nome: ').strip().title()

carregamento(INFO + '\nValidando informações', INFO)
time.sleep(1.0)

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