import json
from flask import Flask
from flask_cors import CORS
import numpy as np
import random

numberOfSquares = 12000
arrayOfSquares = []

for x in range(numberOfSquares):
# Api goes here    
    colour = "%06x" % random.randint(0, 0xFFFFFF)
    newSquare = {"number":x,"colour":colour}
    arrayOfSquares.append(newSquare)
    pass

api = Flask(__name__)
CORS(api)

@api.route('/squares', methods=['GET'])
def get_squares():
  return json.dumps(arrayOfSquares)

if __name__ == '__main__':
    api.run()