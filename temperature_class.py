
import math

class Temperature:
    """"""
    def __init__(self, value: float, unit: str = "C") -> None:
        if not isinstance(unit, str):
            raise ValueError("The unit must be a string")
        normalized_unit = unit.upper()
        if normalized_unit not in ("C", "F", "K"):
            raise ValueError(f"The unit is invalid and the unit should be 'C', 'F' or 'K'.")
        self._value = float(value)
        self._unit = normalized_unit
        #at value og unit er read-only attributes betyr at du ikke kan endre dem utenfor klassen 
        # at unit er case-insensitive betyr at C, F og K er store bokstaver. 
        if self.to_kelvin() < 0:
            raise ValueError("Temperature cannot be lower than 0 K")
    
    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
            return self._unit

    def to_celsius(self) -> float:
        """"""
        if self._unit == "C":
            return self._value
        if self._unit == "K":
            return self._value - 273.15
        if self._unit == "F":
            return (self._value - 32) * (5/9) 

    def to_fahrenheit(self) -> float:
        """"""
        if self._unit == "F":
            return self._value
        if self.unit == "C":
            return (self.value * (9/5)) + 32
        if self.unit == "K":
            return ((self.value - 273.15) * (9/5)) + 32
        
    def to_kelvin(self) -> float:
        """"""
        if self._unit == "K":
            return self._value
        if self.unit == "C":
            return self.value + 273.15
        if self.unit == "F":
            return ((self.value - 32) * (5/9)) + 273.15

    def convert_to(self, target_unit: str) -> "Temperature":
        """"""
        if not isinstance(target_unit, str):
            raise ValueError("The target unit must be a string")

        target = target_unit.upper()
        if target == "C":
            return Temperature(self.to_celsius(), "C")
        #Instance er at du lager et nytt objekt av den klassen
        
        if target == "F":
            return Temperature(self.to_fahrenheit(), "F")
        
        if target == "K":
            return Temperature(self.to_kelvin(), "K")
        
        if target_unit not in ["C", "F", "K"]:
            raise ValueError
        #Sjekke hvilken unit du har. Target unit er enheten man konverterer til.
        #Bruk de andre funksjonene du har. 

    def __repr__(self) -> str:
        """"""
        return f"Temperature({self._value},{self._unit})"

    def __str__(self) -> str:
        """"""
        return f"{self._value}°{self._unit}"

    def __eq__(self, other: object) -> bool: #isinstance sjekker du om begge objekter er temperaturobjekt. 
        """"""
        #Hvis en eller begge ikke er temperaturobjekt retunerer du NotImplemented
        #Python forstår at other er på andre siden
        if not isinstance(other, Temperature): #Sjekker om other er en temperature
            return NotImplemented
        return math.isclose(self.to_kelvin(), other.to_kelvin(), rel_tol = 1e-09)
        #Math isclose trenger jeg kun for ==

    def __lt__(self, other: object) -> bool: 
        #isinstance sjekker du om begge objekter er temperaturobjekt. 
        """oioi iho"""   
        if not isinstance(other, Temperature):
            return NotImplemented
        return not(self == other) and self.to_kelvin() < other.to_kelvin()
        #Vi skriv not(self == other) slik at vi får brukt toleransen på 1e-09. 

    def __le__(self, other: object) -> bool: #isinstance sjekker du om begge objekter er temperaturobjekt. 
        """"""   
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self == other) or self.to_kelvin() <= other.to_kelvin()

    def __gt__(self, other: object) -> bool: 
        """"""   
        if not isinstance(other, Temperature):
            return NotImplemented
        return not(self == other) and self.to_kelvin() > other.to_kelvin()
    
    def __ge__(self, other: object) -> bool: 
        """"""   
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self == other) or self.to_kelvin() >= other.to_kelvin()

    
# https://www.w3schools.com/python/ref_math_isclose.asp#:~:text=The%20math.isclose%20%28%29%20method%20checks%20whether%20two%20values,tolerance%2C%20to%20see%20if%20the%20values%20are%20close.
        