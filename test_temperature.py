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
    #Du bruker pytest.paramterize når du vil teste funksjonen med ulike typer input. 


def read_only_behaviours():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "K"

def invalid_unit():
    with pytest.raises(ValueError):
        t = Temperature(30, "b")
    with pytest.raises(ValueError):
        t = Temperature(100, "f")


def below_absolute_zero():
    with pytest.raises(ValueError):
        t = Temperature(-1, "unit")


@pytest.mark.parametrize("c, f, k", 
                         [[-273.15, −459.67, 0],
                          [],
                          [],
                          [],
                          [],
                          ])
                         ])

def conversion(c, f, k):
      assert 

#Du må teste par C = F, F = K .
