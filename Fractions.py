import numpy as np
import math

class Fraction:
    '''The class represent a fraction'''

    def __init__(self, numerator: int = 1, denominator: int = 1):
        ''' The iniseliser function 
        
        Args:
            numerator (int): The numerator of the fraction
            denomenator (int): The denominator of the fraction that must be positive and not zero
        '''

        #Cheks if the numerator and denominator are not integers and rasses Valuerorss
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError('The numerator and denominator must be integers.')

        #Cheks if the denominator is Zerro and raises a Zirodivideerror
        if denominator == 0:
            raise ZeroDivisionError('The denominator must not be zero')

        #Cheks if the denominator is negativ and raises a valueerror
        if denominator < 0:
            raise ValueError('The denominator must be posetive')

        #Devisor to surten the fractions
        devi=math.gcd(abs(numerator), denominator)

        #Define the denominator and numenator for the class
        self.numerator = numerator // devi
        self.denominator = denominator // devi

    def __repr__(self):
        """A reepresantation of the Fraction"""
        return f'Fraction({self.numerator}, {self.denominator})'

    def __str__(self):
        """A string represantaation for printing"""
        #Returns the apropriate string
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: Fraction) -> Fraction:
        ''' The add metode defining the sumation of the fraction'''
        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError

        #Chek if the denominators are the same and returns the apropriat new fraction
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
            ''' The add metode defining the sumation of the fraction'''
            #Cheks if the other value are and integer and give it a class
            if isinstance(other, int):
                other = Fraction(other, 1)
            #Cheks if the other value is a class and return a NotImplementedError
            if not isinstance(other, Fraction):
                return NotImplementedError
    
            #Chek if the denominators are the same and returns the apropriat new fraction
            if self.denominator == other.denominator:
                return Fraction(self.numerator - other.numerator, self.denominator)
            else:
                return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)
        

    def __mul__(self, other: Fraction) -> Fraction:
        '''The metode defining the multiplicatoin of the fraction'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError

        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    def __truediv__(self, other: Fraction) -> Fraction:
        '''The metode defining the divition of the fraction'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
                    other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError

        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)


    def __eq__(self, other: Fraction) -> bool:
        '''The Metode defining the equal to'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        else:
            #Returns the right boolean expration
            return self.numerator*other.denominator == other.numerator*self.denominator
    
    def __ne__(self, other: Fraction) -> bool:
        '''The Metode defining the not equla to'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        #Returns the right boolean expration
        return self.numerator*other.denominator != other.numerator*self.denominator
    
    def __lt__(self, other: Fraction) -> bool:
        '''The Metode defining the lass than'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        #Returns the right boolean expration
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other: Fraction) -> bool:
        '''The Metode defining the lass than or eqal to'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        #Returns the right boolean expration
        return self.numerator*other.denominator <= other.numerator*self.denominator

    def __gt__(self, other: Fraction) -> bool:
        '''The Metode defining the grater than'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        #Returns the right boolean expration
        return self.numerator*other.denominator > other.numerator*self.denominator

    def __ge__(self, other: Fraction) -> bool:
        ''' The Metode defining the grater then or equl to'''

        #Cheks if the other value are and integer and give it a class
        if isinstance(other, int):
            other = Fraction(other, 1)
        #Cheks if the other value is a class and return a NotImplementedError
        if not isinstance(other, Fraction):
            return NotImplementedError
        #Returns the right boolean expration
        return self.numerator*other.denominator >= other.numerator*self.denominator

