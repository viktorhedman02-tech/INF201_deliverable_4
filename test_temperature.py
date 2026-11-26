import pytest
from temperature_class import Temperature


#Se lecture 11 for å gjøre tester. Bruk def() og assert. Jeg tror du kan bruke 
# if :
# raise ValueError. 
#Du vet hvilke svar du skal få når koden funker.  
# I jupyter file bruker du utropstegn ! for å kjøre testene. Jupyter fila vil vise output.  
#Trenger vi å bruke pytest.approx() i koden?
#Ja, det er lurt å bruke pytest.approx() når du sammenligner float tall.

#Skal koden vi leverer inn fungere 100 prosent og være ferdig testet før vi leverer den inn?
#Skal testene vi legger inni jupyter fungere 100 prosent?
#Er default unit celsius eller en annen enhet?
#Du kan velge celsius som default unit. 

#Det er ikke noe krav om 100 prosent dekning på testene du leverer inn
#Helst skal alle testene fungere og være helt dekket når du leverer dem inni jupyter
#Du kan ikke levere inn en test som feiler. 
#Du skal rette opp feil i koden før du leverer inn.
# Det er mulig å få mindre enn 100 prosent dekning selv om koden er feilfri. 
# Dekning er hvor mye av det som er i koden som blir testet.  
#Jeg får ikke mer enn 0,5 poeng trekk når klassen bare godtar store bokstaver. 

#Skriv i notebooken din at koden din bare godtar store bokstaver. 

def test_default_unit():
    t = Temperature(25)
    assert t.value == 25
    assert t.unit == "C"

@pytest.mark.parametrize("unit", ["C", "F", "K"])
def test_case_insensitive_units(unit):
    value = 300 if unit == "K" else 25
    t = Temperature(value, unit)
    assert t.unit == unit
    assert t.value == value
    #Du bruker pytest.paramterize når du vil teste funksjonen med ulike typer input. 


def test_read_only_behaviours():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "K"

def test_invalid_unit():
    with pytest.raises(ValueError):
        t = Temperature(30, "b")
    with pytest.raises(ValueError):
        t = Temperature(100, "f")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        t = Temperature(-1, "K")
    with pytest.raises(ValueError):
        t = Temperature(-462, "F")
    with pytest.raises(ValueError):
        t = Temperature(-276, "C")


@pytest.mark.parametrize("c, f, k", 
                         [[-273.15, -459.67, 0],
                          [-40, -40, 233.15],
                          [0, 32, 273.15],
                          [37, 98.6, 310.15],
                          [100, 212, 373.15]
                          ])
def test_conversion(c, f, k):
    t_c = Temperature(c, "C")
    t_f = Temperature(f, "F")
    t_k = Temperature(k, "K")
    assert t_c == t_f
    assert t_f == t_k
    assert t_c == t_k
    
    assert t_c.convert_to("F").value == pytest.approx(f)
    assert t_c.convert_to("K").value == pytest.approx(k)
    assert t_f.convert_to("C").value == pytest.approx(c)
    assert t_f.convert_to("K").value == pytest.approx(k)
    assert t_k.convert_to("C").value == pytest.approx(c)
    assert t_k.convert_to("F").value == pytest.approx(f)
#Du må teste par C = F, F = K .

def test_roundtrip_conversion():
    original = Temperature(25, "C")
    conversion = original.convert_to("F").convert_to("C")

    assert conversion.unit == "C"
    assert conversion == original 

def test_cross_unit_comparisons():
    c_0 = Temperature(0, "C")
    f_32 = Temperature(32, "F")
    k_warm = Temperature(303.15, "K")  # 30 °C

    # Equal temperatures in different units
    assert c_0 == f_32
    assert c_0 <= f_32
    assert c_0 >= f_32
    assert not (c_0 < f_32)
    assert not (c_0 > f_32)

    # Ordered temperatures in different units
    assert c_0 < k_warm
    assert c_0 <= k_warm
    assert k_warm > c_0
    assert k_warm >= c_0
    assert c_0 != k_warm

def test_formatting():
    t = Temperature(30, "C")

    assert str(t) == "30.0°C"
    assert repr(t) == "Temperature(30.0,C)"


