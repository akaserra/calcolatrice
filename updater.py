# Import modules

import os
import shutil
import time
import urllib.error
import urllib.request

try:
    from colorama import *
except ImportError:
    raise SystemExit('Please run › pip install pynput')

FILE_Version = \
    urllib.request.urlopen('https://raw.githubusercontent.com/akaserra/updater/main/Version/Version.txt').read().decode(
        'utf8').splitlines()[0]  # Raw of Version.txt repository file
FILE_Changelogs = urllib.request.urlopen(
    'https://raw.githubusercontent.com/akaserra/updater/main/Version/Changelogs.txt').read().decode(
    'utf8')  # raw of changelog.txt repository file
FILE_Link = 'https://codeload.github.com/akaserra/updater/zip/refs/heads/main'  # file download link
FILE_Path = 'updater-main.zip'  # Name of the .zip file


# Checking version of file


def version():
    os.system("cls")
    print(f'\r{Fore.RESET}I\'m looking for new updates...')
    time.sleep(2)
    if FILE_Version == '1': # Version
        print(f'{Fore.GREEN + Style.BRIGHT}No available updates.')
        input(f'{Fore.WHITE}Press enter to continue...')
    else:
        sc = input(f'{Fore.BLUE}Update {Fore.GREEN + Style.BRIGHT}available{Fore.BLUE}. Update now? {Fore.CYAN}y/n: {Fore.YELLOW}')
        if sc == 'y'.lower():
            print('\nDownloading update...')
            urllib.request.urlretrieve(FILE_Link, FILE_Path)
            print('Unpacking archive...')
            shutil.unpack_archive(FILE_Path, 'Updated Version ' + FILE_Version)
            os.remove(FILE_Path)
            time.sleep(3)
            print(f'{Fore.GREEN + Style.BRIGHT}Update installed.')
            input(f'{Fore.CYAN}Press enter for see the changelogs...')
            print(f'{Fore.YELLOW}\nChangelogs:{Fore.WHITE}\n' + FILE_Changelogs + '\n')
            time.sleep(3)
            input(f'{Fore.WHITE}Press enter to continue...')
        elif sc == 'n'.lower():
            print(f'{Fore.WHITE}Ok.')
            input(f'{Fore.WHITE}Press enter to continue...')
        else:
            print(f'{Fore.RED}You can write only y or n.')
            input(f'{Fore.WHITE}Press enter to continue...')
            version()


version()
