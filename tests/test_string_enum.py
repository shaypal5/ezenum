"""Testing the StringEnum class."""

import ezenum as eze


def test_basic():
    """Just check it out."""
    rgb = eze.StringEnum(['Red', 'Green', 'Blue'])
    assert rgb.Red == 'Red'
    assert rgb.Green == 'Green'
    assert rgb.Blue == 'Blue'
    assert rgb[0] == 'Red'
    assert rgb[1] == 'Green'
    assert rgb[2] == 'Blue'
    assert len(rgb) == 3
    assert repr(rgb) == "['Red', 'Green', 'Blue']"
