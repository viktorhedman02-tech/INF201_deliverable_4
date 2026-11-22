
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

    def __repr__(self) -> str:
        """"""

    def __str__(self) -> str:
        """"""
        