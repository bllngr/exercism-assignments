#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Submission file for the python series exercise.
#
# v2: Cleared up error raising syntax
# v1: Using list indexing and list comprehensions


def slices(digits, count):
    """
    Return a list of ``count``-length slices from an integer iterable.
    """

    if not 0 < count <= len(digits):
        raise ValueError('{} is not a valid slice length for a series '
                         'of length {}.'.format(count, len(digits)))

    last = len(digits)-count+1

    series = []

    for start in range(last):
        substring = digits[start:start+count]
        series.append([int(x) for x in substring])

    return series
