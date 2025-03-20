from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def obtener_personas():
    personas = ["Esteban", "Alejandro", "María", "Carlos"]
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)