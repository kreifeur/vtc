from flask import Flask, jsonify , request
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def register():
    return jsonify({'msg':'hello'})

if __name__ == '__main__':
    app.run(debug=True)