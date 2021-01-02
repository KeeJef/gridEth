import json
import numpy as np

numberOfSquares = 12000
arrayOfSquares = []

for x in range(numberOfSquares):
# Api goes here    
    colour = list(np.random.choice(range(256), size=3).tolist())
    newSquare = {"number":x,"colour":colour}
    arrayOfSquares.append(newSquare)
    pass



print(json.dumps(arrayOfSquares))