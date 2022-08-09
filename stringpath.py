# MIT License
# Copyright (c) 2022 Pascal Vallaster
# -> see LICENSE for more information


import os
from pathlib import Path
from typing import Union


path = r"C:\Users\pasca\Desktop"
ch_path = r"../../../pascalV/../test/../../"


def normpath(_start_path: Union[str,Path], _end_path: Union[str, Path]):
    """
    Norms the paths to the correct os format.
    """
    return os.path.normpath(_start_path), os.path.normpath(_end_path)


def split_path(_start_path: Union[str,Path], _end_path: Union[str, Path]):
    """
    Splits every path into its single elements.
    """
    return [x.replace(os.sep, "") for x in list(Path(_start_path).parts)], \
           [x.replace(os.sep, "") for x in list(Path(_end_path).parts)]


def simulate_cd(_start_path: list, _end_path: list) -> (Path, bool):
    """
    Simulates a "cd" command on a string which contains a path-like object/str.

    Returns the new path-like object and a bool whether this path exists or not.
    """
    for end_element in _end_path:
        if end_element == "..":
            if len(_start_path) > 1:
                _start_path.pop(-1)
            else:
                pass
        else:
            _start_path.append(end_element)

    _start_path = Path(os.sep.join(_start_path))
    return _start_path, _start_path.exists()


def change_directory(_start_path: Union[str,Path], _end_path: Union[str, Path]) -> (Path, bool):
    """
    A shortcut for calling @simulate_cd with the path-like objects formatted correctly.

    Returns the output of @simulate_cd

    :param _start_path:
    :param _end_path:
    :return: (Path, bool)
    """
    return simulate_cd(*split_path(*normpath(_start_path, _end_path)))

