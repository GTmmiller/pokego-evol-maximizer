import pokego_evol_maximizer
import unittest
import json

# OK, so I want to do one test that returns zero
# One that returns the over amount and one that returns the lower amount
# I also want to make sure the constructor work s properly 

class EvolutionMaximizationResultsTestCase(unittest.TestCase):
    evolvable_pokemon = 0
    total_candies = 0
    evolution_cost = 1

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 0
    
    def setUp(self):
        self.maximization_results = pokego_evol_maximizer.EvolutionMaximizationResults(
            type(self).evolvable_pokemon, 
            type(self).total_candies, 
            type(self).evolution_cost) 

    def test_results_return_as_expected(self):
        self.assertEqual(type(self).expected_pokemon_to_transfer, 
                         self.maximization_results.pokemon_to_transfer)
        self.assertEqual(type(self).expected_pokemon_to_evolve,
                         self.maximization_results.pokemon_to_evolve)
    
    def test_results_serialize_as_expected(self):
        json_dict = self.maximization_results.to_json_dict()
        self.assertEqual(2, len(json_dict))
        self.assertEqual(type(self).expected_pokemon_to_transfer, 
                         json_dict['pokemon_to_transfer'])
        self.assertEqual(type(self).expected_pokemon_to_evolve,
                         json_dict['pokemon_to_evolve'])


class MultipleEvolutions(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 100
    total_candies = 50
    evolution_cost = 12

    expected_pokemon_to_transfer = 82
    expected_pokemon_to_evolve = 11


class AlmostOneEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 11
    total_candies = 38
    evolution_cost = 50

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 0


class AlmostOneCandyEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 1
    total_candies = 49
    evolution_cost = 50

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 0

class NotCloseEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 24
    total_candies = 50
    evolution_cost = 5000

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 0

class JustOneEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 1
    total_candies = 50
    evolution_cost = 50

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 1

class JustOneTransferEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 2
    total_candies = 49
    evolution_cost = 50

    expected_pokemon_to_transfer = 1
    expected_pokemon_to_evolve = 1

class JustOneTransferCheapEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 2
    total_candies = 0
    evolution_cost = 1

    expected_pokemon_to_transfer = 1
    expected_pokemon_to_evolve = 1

class JustOneExpensiveEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 2
    total_candies = 999
    evolution_cost = 1000

    expected_pokemon_to_transfer = 1
    expected_pokemon_to_evolve = 1

class MaxPlusEvolution(EvolutionMaximizationResultsTestCase):
    evolvable_pokemon = 12
    total_candies = 100
    evolution_cost = 4

    expected_pokemon_to_transfer = 0
    expected_pokemon_to_evolve = 12

def test_main():
    assert pokego_evol_maximizer  # use your library here
