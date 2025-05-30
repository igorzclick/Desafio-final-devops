from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return jsonify({'message': 'Aplicação com Swagger está no ar!'})

@app.route('/api/soma/<int:a>/<int:b>')
def soma(a, b):
    """
    Soma dois números
    ---
    parameters:
      - name: a
        in: path
        type: integer
        required: true
      - name: b
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Retorna a soma dos dois números
    """
    return jsonify({'resultado': a + b})

if __name__ == '__main__':
    app.run(debug=True)
