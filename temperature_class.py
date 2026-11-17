
class Temperature:
    """"""
    def __init__(self, value: float, unit: str) -> None:
        self._value = value
        self._unit = unit
        #value og unit er betyr at du ikke kan endre dem utenfor klassen 
        #
    @property
    def value(self):
        return self._value

    @property
    def unit(self):
            return self._unit

    def to_celsius(self) -> float:
        """"""
        C.self.unit = K.self.unit - 273.15



        def to_fahrenheit(self) -> float:
        
        """"""
        def to_kelvin(self) -> float:
        """"""

        def convert_to(self, target_unit: str) -> Temperature:
        """"""

        def __repr__(self) -> str:
        """"""

        def __str__(self) -> str:
        """"""
        