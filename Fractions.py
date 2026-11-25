import numpy as np
import math

class Fraction:
    '''The class represent a fraction'''

    def __init__(self, numerator: int = 1, denominator: int = 1):

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError('The numerator and denominator must be integers.')

        if denominator == 0:
            raise ZeroDivisionError('The denominator must not be zero')

        if denominator < 0:
            raise ValueError('The denominator must be posetive')

        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        pass

    def __str__(self):
        """A string represantaation for printing"""
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: Fraction) -> Fraction:
        ''' '''
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError

        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
        

    def __mul__(self, other: Fraction) -> Fraction:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError

        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    def __truediv__(self, other: Fraction) -> Fraction:
        ''' '''

        if isinstance(other, int):
                    other = Fraction(other, 1)

        if not isinstance(other, Fraction):
            return NotImplementedError

        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)


    def __eq__(self, other: Fraction) -> bool:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        else:
            return self.numerator*other.denominator == other.numerator*self.denominator
    
    def __ne__(self, other: Fraction) -> bool:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        return self.numerator*other.denominator != other.numerator*self.denominator
    
    def __lt__(self, other: Fraction) -> bool:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other: Fraction) -> bool:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        return self.numerator*other.denominator <= other.numerator*self.denominator

    def __gt__(self, other: Fraction) -> bool:
        ''' '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        return self.numerator*other.denominator > other.numerator*self.denominator

    def __ge__(self, other: Fraction) -> bool:
        ''' This '''

        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return NotImplementedError
        return self.numerator*other.denominator >= other.numerator*self.denominator

s=Fraction(1, 2)

t=Fraction(1, 3)

n=2
f=1.2

print(s)

print(t)

print(s+t)

print(s*t)

print(s/t)

print(s != t)
print(s == t)
print(s < t)
print(s >= t)
print(s > t)
print(s <= n)
print(s != n)
print(s == f)