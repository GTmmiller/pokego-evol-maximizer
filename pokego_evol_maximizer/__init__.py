__version__ = "0.1.0"

from scipy import optimize
import numpy as np
import json

class EvolutionMaximizationResults:
    def __init__(self, evolvable_pokemon, total_candies, evolution_cost):
        self._evolvable_pokemon = evolvable_pokemon
        self._total_candies = total_candies
        self._evolution_cost = evolution_cost

        minimization_results_tuple = optimize.fminbound(self._min_evolution_function, 0, self._evolvable_pokemon, full_output=True)

        # [pokemon_to_transfer, negative pokemon_to_evolve, n/a, n/a]
        # The results array is more of a halfway point
        minimization_results_tuple = self._floor_results_tuple(minimization_results_tuple)
        self.pokemon_to_transfer = int(minimization_results_tuple[0]) 
        self.pokemon_to_evolve = int(minimization_results_tuple[1])
    
    def to_json_dict(self):
        """Only return fields not prepended with an underscore as a dict for json conversion"""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def _min_evolution_function(self, x):
        return -1 * np.minimum(self._evolvable_pokemon-x, self._total_candies/self._evolution_cost + x/self._evolution_cost) 
        #return np.maximum(-1 * self._evolvable_pokemon + x, -1 * self._total_candies/self._evolution_cost +  -1 * x/self._evolution_cost)

    # This method takes in the results of the optimization
    # and converts them into minimized integer values
    # turns out getting a min of a floor function is tough
    def _floor_results_tuple(self, results_tuple):
        pokemon_to_transfer = int(round(results_tuple[0], 4))

        candies_after_transfer = pokemon_to_transfer + self._total_candies  
        candies_after_transfer -= candies_after_transfer % self._evolution_cost 

        pokemon_to_transfer = max(candies_after_transfer - self._total_candies, 0)
        pokemon_to_evolve = min(self._evolvable_pokemon, candies_after_transfer / self._evolution_cost) 
        return (pokemon_to_transfer, pokemon_to_evolve)