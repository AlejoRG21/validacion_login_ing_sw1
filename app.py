from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal → index.html
@app.route('/')
def home():
    return render_template("index.html")

# Página de registro → registro.html
@app.route('/registro')
def registro():
    return render_template("registro.html")

# Página de login → login.html
@app.route('/login')
def login():
    return render_template("login.html")

# Ruta que procesa el formulario de registro
@app.route('/registrar', methods=["POST"])
def registrar():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    usuario = request.form.get("usuario")
    contrasena = request.form.get("contrasena")
    
    print(f"Nuevo registro: {nombre} {apellido}, usuario: {usuario}, contraseña: {contrasena}")

    # Redirige al login después de registrarse
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
