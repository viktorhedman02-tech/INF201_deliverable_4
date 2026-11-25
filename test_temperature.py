import pytest
from temperature_class import Temperature


#Se lecture 11 for å gjøre tester. Bruk def() og assert. Jeg tror du kan bruke 
# if :
# raise ValueError. 
#Du vet hvilke svar du skal få når koden funker.  
# I jupyter file bruker du utropstegn ! for å kjøre testene. Jupyter fila vil vise output.  

def default_unit():
    t = Temperature(25)
    assert t.value == 25
    assert t.unit == "C"

@pytest.mark.parametrize("unit", ["C", "F", "K"])
def test_case_insensitive_units(unit):
    value = 300 if unit == "K" else 25
    t = Temperature(value, unit)
    assert t.unit == unit
    assert t.value == value

def read_only_behaviours():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.uniy = "K"
