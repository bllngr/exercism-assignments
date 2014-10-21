#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

# Submission file for the python word_count_test exercise.
#
# v4: Reduce unnecessary variables, and directly return the Counter.
# v3: Remove unnecessary __main__(), since it's usually called from the
#     word_count_test.py file.
# v2: Remove unnecessary comments, and use command line arguments
#     instead of pre-defined string in __main__() 
# v1: Use collections.Counter() for counting word frequencies.

def word_count(str):
	words = str.split()
	return Counter(words)
