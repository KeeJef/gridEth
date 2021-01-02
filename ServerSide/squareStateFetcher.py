import json
from flask import Flask, json
import numpy as np

numberOfSquares = 12000
arrayOfSquares = []

for x in range(numberOfSquares):
# Api goes here    
    colour = list(np.random.choice(range(256), size=3).tolist())
    newSquare = {"number":x,"colour":colour}
    arrayOfSquares.append(newSquare)
    pass

api = Flask(__name__)

@api.route('/squares', methods=['GET'])
def get_squares():
  return json.dumps(arrayOfSquares)

if __name__ == '__main__':
    api.run()