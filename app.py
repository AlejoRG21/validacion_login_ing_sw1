from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = []  # Lista para guardar registros temporalmente

# Página principal → index.html
@app.route('/')
def home():
    return render_template("index.html")

# Página de registro
@app.route('/registro')
def registro():
    return render_template("registro.html")

# Página de login
@app.route('/login')
def login():
    return render_template("login.html")

# Procesar registro
@app.route('/registrar', methods=["POST"])
def registrar():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    usuario = request.form.get("usuario")
    contrasena = request.form.get("contrasena")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")

    # Guardar datos en la lista
    usuarios.append({
        "nombre": nombre,
        "apellido": apellido,
        "usuario": usuario,
        "contrasena": contrasena,
        "correo": correo,
        "telefono": telefono
    })

    print(f"Nuevo registro: {nombre} {apellido}, usuario: {usuario}, correo: {correo}")

    # 🔥 Redirige al login después de registrarse
    return redirect(url_for("login"))

# Página con tabla de usuarios
@app.route('/usuarios')
def lista_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
