import pathlib


def load_data(file_name: str, split_sep: str = None):

    ret_val = ''

    with open(f"{pathlib.Path(__file__).parent.absolute()}/data/{file_name}"
              ) as input_file:

        ret_val = input_file.read()
        if split_sep is not None:
            ret_val = ret_val.split(split_sep)

    return ret_val
