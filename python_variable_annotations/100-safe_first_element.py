#!/usr/bin/env python3
""" Duck typing - first element of a sequence """

from typing import Any, Union, Sequence

# The types of the elements of the input are not known


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safe first element """
    if lst:
        return lst[0]
    return None
