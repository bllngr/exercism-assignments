#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Submission file for the python allergies exercise.
#
# v1:


class Allergies(object):
    """
    Store and calculate allergies depending on a person's allergy score.

    Possible allergen values are powers of two, which allows easy
    calculations using bitwise-operators.

    Example:

    Tom is allergic to peanuts and chocolate. (That poor guy!). Peanuts
    have a value of 2, while chocolate has a value of 32. This give Tom
    an allergy score of 34.

    Now, we want to tell whether Tom is allergic to strawberries.
    Given his score of 34, and the strawberries' value of 8, we are able
    to calculate 32 & 8 == 0, or in binary:

      100010
    & 001000
    --------
      000000

    Calculating whether he's allergic to chocolate works the same way:

      100010
    & 100000
    --------
      100000

    If the result is zero, we now Tom's not allergic to the given item.
    If the result is unequal to zero, Tom unfortunately has an allergy.
    """

    _allergens = list(zip('eggs peanuts shellfish strawberries '
                          'tomatoes chocolate pollen cats'.split(),
                          [2**x for x in range(8)]))

    def is_allergic_to(self, allergen):
        """
        Tell if a person if allergic to the given allergen.
        """
        return allergen in self.list

    def __init__(self, score):
        """
        Initialise an allergy storage with the given allergy score.
        """
        self.score = score

        # Given the nature of allergen values
        self.list = [candidate[0] for candidate in self._allergens
                     if candidate[1] & self.score]
