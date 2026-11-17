import numpy as np
import math

class Fraction:
    '''The class represent a fraction'''

    def __init__(self, numerator: int = 1, denominator: int = 1):

        if not isinstance(numerator, int) or isinstance(denominator, int):
            raise ValueError('The numerator and denominator must be integers.')

        if denominator == 0:
            raise ZeroDivisionError('The denominator must not be zero')

        if denominator < 0:
            raise ValueError('The denominator must be posetive')

        self.numerator = numerator
        self.denominator = denominator

    
        