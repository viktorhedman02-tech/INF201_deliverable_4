import pytest
from temperature_class import Temperature
 

def test_default_unit() -> None:
    """Check that if you create Temperature(25) without a unit, 
    that it defaults to 'C'. And use assert to test this."""
    t: Temperature = Temperature(25)
    assert t.value == 25
    assert t.unit == "C"

#Use @pytest.mark.parametrize to do the same tests for "C", "F", "K", "c", "f" and "k"
@pytest.mark.parametrize("unit", ["C", "F", "K", "c", "f", "k"])
def test_case_insensitive_units(unit: str) -> None:
    """Tests that unit and value matches with what was passed in.
    Use assert to test this."""
    value = 300 if unit == "K" else 25
    t = Temperature(value, unit)
    assert t.unit == unit
    assert t.value == value 

@pytest.mark.parametrize("target", ["c", "f", "k"])
def test_convert_to_lowercase(target: str) -> None:
    """Tests that the unit can be converted to a lowercase because
    the units should work for both uppercase and lowercase."""
    t: Temperature = Temperature(25, "C")
    converted = t.convert_to(target)
    assert converted.unit == target 

def test_read_only_behaviours() -> None:
    """In this test t.value and t.unit are reassigned and .pytest.raises(AttributeError) is used to confirm
    that both properties are read only attributes"""
    t: Temperature = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "K"

def test_invalid_unit() -> None:
    """Test that invalid units for example 'b' and 'd' raises a ValueError. """
    with pytest.raises(ValueError):
        t = Temperature(30, "b")
    with pytest.raises(ValueError):
        t = Temperature(100, "d")


def test_below_absolute_zero() -> None:
    """Test that temperatures below 0 k (absolute zero) raises a ValueError"""
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
def test_conversion(c: float, f: float, k: float) -> None:
    """In this test we use 5 reference temperatures
    (such as absolute zero, body temperature, booling temperature)
    across the units C, F and K to test conversion accuracy
    and that temperatures from different units equal to the same physical temperature"""
    t_c: Temperature = Temperature(c, "C")
    t_f: Temperature = Temperature(f, "F")
    t_k: Temperature = Temperature(k, "K")
    assert t_c == t_f
    assert t_f == t_k
    assert t_c == t_k
    
    assert t_c.convert_to("F").value == pytest.approx(f)
    assert t_c.convert_to("K").value == pytest.approx(k)
    assert t_f.convert_to("C").value == pytest.approx(c)
    assert t_f.convert_to("K").value == pytest.approx(k)
    assert t_k.convert_to("C").value == pytest.approx(c)
    assert t_k.convert_to("F").value == pytest.approx(f)


def test_roundtrip_conversion() -> None:
    """In this test a temperature of 25 Celsius is converted to "F" and than back to "C"
    to test if we still have the original temperature 25 Celsius."""
    original = Temperature(25, "C")
    conversion = original.convert_to("F").convert_to("C")

    assert conversion.unit == "C"
    assert conversion == original 

def test_cross_unit_comparisons() -> None:
    """This test compares temperatures across the units
     C, F and K to test both equal temperatures (==, <= and >=) and stricly different temperatures
     (<, <=, >, >= and !=). """
    c_0 = Temperature(0, "C")
    f_32 = Temperature(32, "F")
    k_warm = Temperature(303.15, "K")  # 30 °C

    # Equal temperatures in different units
    assert c_0 == f_32
    assert c_0 <= f_32
    assert c_0 >= f_32
    assert not (c_0 < f_32)
    assert not (c_0 > f_32)

    # Strictly different temperatures in different units
    assert c_0 < k_warm
    assert c_0 <= k_warm
    assert k_warm > c_0
    assert k_warm >= c_0
    assert c_0 != k_warm

def test_formatting() -> None:
    """Test that str(t) returns "30.0°C" 
    and that repr(t) returns "Temperature(30.0,C)"."""
    t = Temperature(30, "C")

    assert str(t) == "30.0°C"
    assert repr(t) == "Temperature(30.0,C)"

def test_identity_conversion() -> None:
    """ Test direct same-unit conversion for to_celsius when already "C"
    and for o_fahrenheit when already "F"."""
    t_c = Temperature(25, "C")
    t_f = Temperature(77, "F")
    # Hits (to_celsius when already "C") and (to_fahrenheit when already "F")
    assert t_c.to_celsius() == pytest.approx(25.0)
    assert t_f.to_fahrenheit() == pytest.approx(77.0) 

def test_convert_target_unit() -> None:
    """Test that error is handeld when the target unit in convert_to() is invalid"""
    t = Temperature(20, "C")

    # Hits ValueError on invalid target_unit)
    with pytest.raises(ValueError):
        t.convert_to("invalid")
    with pytest.raises(ValueError):
        t.convert_to("d")


def test_comparisons() -> None:
    """This test compare a Temperature instance with a integer to verify
    that == returns False, != returns True, and that 
    <, <=, >, and >= raise TypeError when __lt__, __le__, __gt__, and __ge__ 
    return NotImplemented"""
    t = Temperature(20, "C")

    # Hits (__eq__ returning NotImplemented -> evaluates to False / != is True)
    assert (t == 20) is False
    assert (t != 20) is True

    # Hits (__lt__, __le__, __gt__, __ge__ -> Python raises TypeError)
    with pytest.raises(TypeError):
        _ = t < 20
    with pytest.raises(TypeError):
        _ = t <= 20
    with pytest.raises(TypeError):
        _ = t > 20
    with pytest.raises(TypeError):
        _ = t >= 20

