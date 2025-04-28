from flask import Flask, render_template

app = Flask(__name__)

# Datos Dinámicos
libros = [
    {"id": 1, "nombre": "All Tomorrows", "precio": 30.00},
    {"id": 2, "nombre": "Final Fantasy VII", "precio": 10.00}
]

usuarios = [
    {"id": 1, "nombre": "Peter", "rol": "Usuario"},
    {"id": 2, "nombre": "Michael", "rol": "Usuario"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/libros")
def mostrar_productos():
    return render_template("libros.html", libros=libros)

@app.route("/usuarios")
def mostrar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)