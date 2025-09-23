import pytest

def test_math_works():
    assert 2 + 2 == 4

@pytest.mark.fast
def test_string_contains():
    assert "pokeapi".startswith("poke")
