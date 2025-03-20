from flask import Flask, jsonify  # Importa Flask y jsonify para manejar respuestas JSON

app = Flask(__name__)  # Crea la instancia de la aplicación Flask

# Define la ruta '/personas' que responderá con una lista de nombres
@app.route('/personas', methods=['GET'])
def obtener_personas():
    """
    Función que devuelve una lista de nombres en formato JSON.
    Se accede mediante una solicitud GET a /personas.
    """
    personas = ["Esteban", "Dylan", "Ana", "Carlos", "María"]  # Lista de nombres
    return jsonify(personas)  # Retorna la lista como respuesta JSON

# Ejecuta la aplicación si el script se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)  
