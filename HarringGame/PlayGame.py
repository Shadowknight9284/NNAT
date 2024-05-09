from HarringGame import CreateGame
from HarringGame.CreateGame import Game
import itertools
# Assuming you have a function called `rate_strategy` that rates a strategy

def rate_strategy(strategy):
    # Your rating logic here
    pass

# Assuming you have a list of strategies
strategies = [...]

# Generate all possible combinations of two strategies
combinations = list(itertools.combinations(strategies, 2))

# Rate each combination
for combination in combinations:
    strategy1, strategy2 = combination
    rating1 = rate_strategy(strategy1)
    rating2 = rate_strategy(strategy2)
    # Do something with the ratings

