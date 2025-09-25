from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # O la URI de tu base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mi_secreto'  # Necesario para usar `flash`
db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombre} {self.apellido}>"

# Ruta para la página de registro (index.html)
@app.route('/')
def index():
    return render_template('./templates/index.html')

# Ruta para registrar un nuevo usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        usuario = request.form['usuario']
        correo = request.form['correo']
        telefono = request.form['telefono']
        contrasena = request.form['contrasena']
        
        # Verificar si el usuario ya existe
        usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
        if usuario_existente:
            flash('El nombre de usuario ya está registrado', 'error')
            return redirect(url_for('index'))
        
        # Crear un nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre, apellido=apellido, usuario=usuario,
            correo=correo, telefono=telefono, contrasena=contrasena
        )
        
        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))

# Ruta para la página de inicio de sesión (login.html)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos del formulario de login
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        # Buscar el usuario en la base de datos
        usuario_db = Usuario.query.filter_by(usuario=usuario).first()
        
        if usuario_db and usuario_db.contrasena == contrasena:
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('usuarios'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('./templates/login.html')

# Ruta para mostrar los usuarios registrados
@app.route('/usuarios')
def mostrar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('./templates/usuarios.html', usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
