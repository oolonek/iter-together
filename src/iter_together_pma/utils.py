# -*- coding: utf-8 -*-

"""Utilities for``iter-together``."""


def iter_together(path_left: str, path_right: str):
    """Open two files, iterate over them, and zip the together.

    :param path_left: The path to the left CSV file.
    :param path_right: The path to the right CSV file.
    """
    with open(path_left) as left_file, open(path_right) as right_file:
        for left_line, right_line in zip(left_file, right_file):
            left_idx, left_value = left_line.strip().split(',')
            right_idx, right_value = right_line.strip().split(',')
            yield left_idx, left_value, right_value
