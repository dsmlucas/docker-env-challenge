import datetime as __date


__PURPLE = '\033[95m'
__CYAN = '\033[96m'
__BLUE = '\033[94m'
__GREEN = '\033[92m'
__YELLOW = '\033[93m'
__RED = '\033[91m'

__BOLD = '\033[1m'
__UNDERLINE = '\033[4m'
__END = '\033[0m'


def __get_time():
    return str(__date.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


def info(text: str):
    dt = __get_time()
    print(f'{dt} - {__BOLD}{__GREEN}[info]{__END}: {text}')


def error(text: str):
    dt = __get_time()
    print(f'{dt} - {__BOLD}{__RED}[error]{__END}: {text}')


def warn(text: str):
    dt = __get_time()
    print(f'{dt} - {__BOLD}{__YELLOW}[warn]{__END}: {text}')


def debug(text: str):
    dt = __get_time()
    print(f'{dt} - {__BOLD}[debug]{__END}: {text}')


def topic(topic, text: str):
    dt = __get_time()
    print(f'{dt} - {__BOLD}{__BLUE}[{topic}]{__END}: {text}')
