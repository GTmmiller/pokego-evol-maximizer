**[Pidgey Spam](https://pokeassistant.com/main/pidgeyspam) is a much more complete and useful tool that does a lot more than pokego-evol-maximizer. This was mostly created for fun, so please keep that in mind if you use it.**

pokego-evol-maximizer is a utility for Pokemon Go that tells you how many Pokemon you should transfer to maximize the number of Pokemon you can evolve at that moment. 

## Motivation

I created this project to fill a personal need I had to make the most out of my Lucky Eggs. The goal of this project was to discover how to maximize the number of Pokemon I could evolve with the fewest amount of transfers. I also wanted to try my hand at maximizing calculus equations with [SciPy](https://www.scipy.org/).

## Installation

In order to get started developing or running pokego-evol-maximizer, you need to:
 
1. [install anaconda](https://www.continuum.io/downloads) **Be sure to get the Python 3 version**. That should get you all the SciPy packages and tooling needed to run the site.

2. Run `conda env create -f environment.yml`. It insures that all the packages you need to run the site are installed.

## Running

1. Set the FLASK_APP environment variable to run.py
    - Windows: `set FLASK_APP=run.py`
    - Unix-like: `export FLASK_APP=run.py`
2. Run `python -m flask run`

Congratulations! The server should be running now! 

## Tests

Run `python -m unittest` to run all the unit tests.

## Contributors

Feel free to do pretty much whatever you want with this code! If you take the time to make a merge request for a new feature or something cool I'll try my best to review it.

## License

This software is covered by the BSD 2 clause license

## Disclaimer

This project has no affiliation with The Pokemon Company or Niantic, Inc. All rights to the names "Pokemon" and "Pokemon Go" are reserved by the aforementioned parties.
