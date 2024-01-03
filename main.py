import scripts.base64_coding as b64
import scripts.base32_coding as b32
import scripts.base16_coding as b16
import scripts.url_coding as url
import scripts.hex_coding as hexc
import scripts.rot13_coding as rot13
import scripts.md5_crypto as md5
import scripts.sha1_crypto as sha1
import scripts.sha256_crypto as sha256
import scripts.sha512_crypto as sha512
import contextlib
from colorama import Fore


def logo():
    """Функция отображает приветствие пользователя"""
    print(f'''{Fore.CYAN}
 ██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗     ██████╗  ██████╗ ██╗  ██╗
██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗╚██╗██╔╝
██║      ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║    ██████╔╝██║   ██║ ╚███╔╝ 
██║      ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║    ██╔══██╗██║   ██║ ██╔██╗ 
╚██████╗ ██║  ██║   ██║   ██║        ██║   ╚██████╔╝    ██████╔╝╚██████╔╝██╔╝ ██╗
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                                                     
        {Fore.RESET}''')


def menu():
    """Функция отображает меню"""
    print(f'\n\n{Fore.CYAN}Select the desired action:{Fore.RESET}')
    for crypt in algorithm:
        print(f'{Fore.CYAN}{crypt}. {algorithm[crypt][0]}{Fore.RESET}')


def choice_algorithm():
    """Функция обрабатывает ввод пользователя при выборе алгоритма"""
    try:
        if (select := int(input('\n\nSelect number: '))) in range(0, 13):
            return select
    except Exception as error:
        print(f'{Fore.RED}Error: {error}{Fore.RESET}')

    # Вывод ошибки и рестарт функции при выходе за пределы допустимых значений
    print(f'{Fore.RED}Error! Enter a number from 0 to 12{Fore.RESET}')
    return choice_algorithm()


def choice_action():
    """Функция обрабатывает выбор действия для алгоритмов кодирования"""

    # Отображение меню выбора действия
    print(f'{Fore.CYAN}1. Encode\n2. Decode{Fore.RESET}')

    # Обработка ввода пользователя
    if (select := int(input('Selected action: '))) == 1:
        return True
    elif select == 2:
        return False

    # Вывод ошибки и рестарт функции при выходе за пределы допустимых значений
    print(f'{Fore.RED}Error! Enter the number 1 or 2{Fore.RESET}')
    return choice_action()


def all_coding(data):
    """Функция кодирует по всем алгоритмам и записывает результат в файл"""
    with open('res_codings.txt', 'w') as file:
        with contextlib.redirect_stdout(file):
            for i in range(1, 7):
                print('-' * 35, f'{i}. {algorithm[i][0]}', '-' * 35,
                      algorithm[i][1](data, encode=True), sep='\n')
    print(f'{Fore.CYAN}Done!{Fore.RESET}')


def all_crypto(data):
    """Функция шифрует по всем алгоритмам и записывает результат в файл"""
    with open('res_ciphers.txt', 'w') as file:
        with contextlib.redirect_stdout(file):
            for i in range(7, 11):
                print('-' * 35, f'{i}. {algorithm[i][0]}', '-' * 35,
                      algorithm[i][1](data), sep='\n')
    print(f'{Fore.CYAN}Done!{Fore.RESET}')


def run_coding_crypto(n):
    """Функция запускает кодирование/шифрование"""
    text = input('Enter text: ')

    # Запуск кодирования по всем алгоритмам
    if n == 11:
        all_coding(text)

    # Запуск шифрования по всем алгоритмам
    elif n == 12:
        all_crypto(text)

    # Вывод при выборе алгоритмов кодирования
    elif n in range(1, 7):

        # Выбор действия (кодирование/декодирование) для алгоритмов кодирования
        action = choice_action()

        print(f'Encoded text: {Fore.GREEN}{algorithm[n][1](text, action)}{Fore.RESET}')

    # Вывод при выборе алгоритмов шифрования
    else:
        print(f'Encrypted text: {Fore.GREEN}{algorithm[n][1](text)}{Fore.RESET}')


def main():
    """Функция с основной логикой программы"""

    # Запуск функции, отображающей приветствие
    logo()
    while True:

        # Запуск функции, отображающей меню
        menu()

        # Завершение программы в случае выбора "0" в меню
        if (num := choice_algorithm()) == 0:
            print(f'{Fore.CYAN}The program is complete!{Fore.RESET}')
            exit(0)

        else:
            # Вывод заголовка выбранного алгоритма
            print('-'*35, f'{num}. {algorithm[num][0]}', '-'*35, sep='\n')

            # Запуск функции кодирования/шифрования
            try:
                run_coding_crypto(num)
            except Exception as error:
                print(f'{Fore.RED}Error: {error}{Fore.RESET}')


if __name__ == '__main__':
    algorithm = {0: ('Exit',),
                 1: ('BASE64', b64.coding),
                 2: ('BASE32', b32.coding),
                 3: ('BASE16', b16.coding),
                 4: ('HEX', hexc.coding),
                 5: ('URLENCODE', url.coding),
                 6: ('ROT13', rot13.coding),
                 7: ('MD5', md5.crypto),
                 8: ('SHA-1', sha1.crypto),
                 9: ('SHA-256', sha256.crypto),
                 10: ('SHA-512', sha512.crypto),
                 11: ('All coding',),
                 12: ('All crypto',)}

    # Запуск функции с основной логикой программы
    try:
        main()
    except KeyboardInterrupt:
        print(f'{Fore.RED}\nThe program is closed!{Fore.RESET}')
        exit(0)
