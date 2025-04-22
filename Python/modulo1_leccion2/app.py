from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista simula base de datos de mensajes
mensajes = ["Mensaje ejemplo"]

# Ruta GET que devuelve información básica del servidor
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "versión de prueba: ": "1.0",
        "usuario: ": "Francis X. Rivera Torres"
    })

# Ruta GET y POST que maneja los mensajes
@app.route("/mensaje", methods=["GET", "POST"])
def mensaje():
    if request.method == "GET":
        return jsonify({"mensajes": mensajes})
    
    if request.method == "POST":
        data = request.json
        if not data or "mensaje" not in data:
            return jsonify({"error: ", "Falta campo 'mensaje'"}), 400
        
        mensajes.append(data["mensaje"])
        return jsonify({"respuesta: ": f"Mensaje recibido: {data['mensaje']}"}), 201
    
if __name__ == "__main__":
    app.run(debug=True)