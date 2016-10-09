from flask import Flask, session, g, render_template, jsonify, request
from pokego_evol_maximizer import EvolutionMaximizationResults

app = Flask(__name__)

@app.route('/')
def index():
    """Display the pokemon go evolution maximizer homepage
    The homepage will use JQuery and other javascript goodness
    to call the other json endpoints in the application
    """
    return render_template('index.html')

@app.route('/maximize/')
def maximize():
    """Call the maximizer library to determine how many pokemon should be evolved.
    This endpoint requires the params: evolvable_pokemon, total_candies, and evolution_cost
    failure to set all paramaters """
    evolvable_pokemon = request.args.get("evolvable_pokemon", type=int)
    total_candies = request.args.get("total_candies", type=int)
    evolution_cost = request.args.get("evolution_cost", type=int)
    return jsonify(EvolutionMaximizationResults(evolvable_pokemon, total_candies, evolution_cost).to_json_dict())