# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Bienvenido Mauricio  a la API de Ejemplo!"

@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'mundo')
    return jsonify({'mensaje': f'¡Hola, {nombre}!'}), 200

@app.route('/suma', methods=['POST'])
def suma():
    data = request.get_json()
    numero1 = data.get('numero1')
    numero2 = data.get('numero2')

    if numero1 is None or numero2 is None:
        return jsonify({'error': 'Por favor proporciona dos números.'}), 400

    try:
        resultado = numero1 + numero2
        return jsonify({'resultado': resultado}), 200
    except TypeError:
        return jsonify({'error': 'Ambos valores deben ser números.'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
