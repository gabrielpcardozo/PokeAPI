import pytest
from django.test import TestCase
from pokemon.models import Pokemon


class PokemonModelTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1

    def test_first(self):
        pokemon = "lucario"
        assert type(pokemon) == str