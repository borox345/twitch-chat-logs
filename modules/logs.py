from datetime import datetime
from colorama import Fore
from colorama import Style

now = datetime.now()
time_log = now.strftime("[%d/%m/%Y %H:%M:%S]")


def log(type, message):

    switcher={
        'client': f'{Fore.MAGENTA}[CLIENT] {time_log} {message} {Style.RESET_ALL}',
        'info': f'{Fore.YELLOW}[INFO] {time_log} {message} {Style.RESET_ALL}',
        'error': f'{Fore.RED}[ERROR] {time_log} {message} {Style.RESET_ALL}',
        'warning': f'{Fore.YELLOW}[WARNING] {time_log} {message} {Style.RESET_ALL}',
    }

    print(switcher.get(type,"Invalid type"))
