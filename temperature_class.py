
class Temperature:
    """"""
    def __init__(self, value: float, unit: str) -> None:
        self._value = value
        self._unit = unit
        #at value og unit er read-only attributes betyr at du ikke kan endre dem utenfor klassen 
        # at unit er case-insensitive betyr at C, F og K er store bokstaver. 
        if unit not in ["C", "F", "K"] or self.to_kelvin < 0:
            raise ValueError
    
    @property
    def value(self):
        return self._value

    @property
    def unit(self):
            return self._unit

    def to_celsius(self) -> float:
        """"""
        if self._unit == "K":
            return self._value - 273.15
        if self._unit == "F":
            return (self._value - 32) * (5/9) 

    def to_fahrenheit(self) -> float:
        """"""
        if self.unit == "C":
            return (self.value * (9/5)) + 32
        if self.unit == "K":
            return ((self.value - 273.15) * (9/5)) + 32
        
    def to_kelvin(self) -> float:
        """"""
        if self.unit == "C":
            return self.value + 273.15
        if self.unit == "F":
            return ((self.value - 32) * (5/9)) + 273.15

    def convert_to(self, target_unit: str) -> Temperature:
        """"""
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
        if not isinstance(other, ):
            return NotImplemented
        return self.to_kelvin(self) == other.to_kelvin(self)

    def __lt__(self, other: object) -> bool: #isinstance sjekker du om begge objekter er temperaturobjekt. 
        """"""   
        if not isinstance(other, ):
            return NotImplemented
        return self.to_kelvin(self) < other.to_kelvin(self)

    

        