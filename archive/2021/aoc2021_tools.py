import pathlib
import sys


def load_data(file_name: str, split_sep: str = None):

    ret_val = ""

    try:
        input_file_name = f"{pathlib.Path(__file__).parent.absolute()}/data/{file_name}"
        input_file = open(input_file_name)

        ret_val = input_file.read()
        if split_sep is not None:
            ret_val = ret_val.split(split_sep)
    except FileNotFoundError as e:
        sys.exit(e)
    return ret_val


def dprint(debug: bool = True, message: str = ""):
    if debug:
        print(message)
