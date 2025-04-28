from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route("/")
def main():
    return "<h1>Mensaje de ejemplo: segundo ejercicio.<h1>"

usuarios = []


# Ruta GET para obtener información del servidor
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        'ejercicio': "2",
        'usuario': 'Francis X. Rivera Torres'
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.json

    nombre = data.get('nombre')
    correo = data.get('correo')
    
    if not nombre or not correo:
        return jsonify({
            'Error': 'Se necesita el nombre y el correo'}), 400

    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': nombre,
        'correo': correo,
    }

    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)