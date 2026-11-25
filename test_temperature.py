import pytest
from temperature_class import Temperature

def default_unit():
    t = Temperature(20)
    assert t.value == 20
    assert t.unit == "C"

@pytest.mark.parametrize("raw_unit, expected_unit", [
    ("c", "C"),
    
])