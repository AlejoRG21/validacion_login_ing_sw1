from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    tipo_documento = db.Column(db.String(50), nullable=False)
    numero_documento = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=True)
    usuario = db.Column(db.String(120), nullable=False, unique=True)
    contrasena = db.Column(db.String(120), nullable=False, unique=True)



    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'tipo_documento': self.tipo_documento,
            'numero_documento': self.numero_documento,
            'email': self.email,
            'telefono': self.telefono
            'usuario': self.usuario
            'contrasena': self.usuario
        }

# Crear la base de datos antes del primer request
@app.before_first_request
def crear_bd():
    db.create_all()

# Ruta para obtener todos los usuarios
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

# Ruta para agregar un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()

    # Validación básica (puedes mejorarla con marshmallow o WTForms)
    campos_requeridos = ['nombre', 'apellido', 'tipo_documento', 'numero_documento', 'email']
    if not all(campo in datos for campo in campos_requeridos):
        return jsonify({'error': 'Faltan datos requeridos'}), 400

    # Verificar si el email o número de documento ya existen
    if Usuario.query.filter_by(email=datos['email']).first():
        return jsonify({'error': 'El email ya está registrado'}), 409
    if Usuario.query.filter_by(numero_documento=datos['numero_documento']).first():
        return jsonify({'error': 'El número de documento ya está registrado'}), 409

    nuevo_usuario = Usuario(
        nombre=datos['nombre'],
        apellido=datos['apellido'],
        tipo_documento=datos['tipo_documento'],
        numero_documento=datos['numero_documento'],
        email=datos['email'],
        telefono=datos.get('telefono')  # Puede ser opcional
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario agregado correctamente'}), 201
from flask import request, jsonify
from werkzeug.security import check_password_hash  # si usas hash

@app.route('/api/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({'error': 'Faltan datos'}), 400

    user = Usuario.query.filter_by(usuario=usuario).first()

    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Si estás guardando la contraseña como texto plano (NO recomendado):
    if user.contrasena != contrasena:
        return jsonify({'error': 'Contraseña incorrecta'}), 401

    # Si usas hashes (recomendado):
    # if not check_password_hash(user.contrasena, contrasena):
    #     return jsonify({'error': 'Contraseña incorrecta'}), 401

    return jsonify({'mensaje': 'Login exitoso'})
    
@app.route('/api/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()

    # Verificar campos requeridos
    campos = ['nombre', 'apellido', 'tipo_documento', 'numero_documento', 'email', 'telefono', 'usuario', 'contrasena']
    if not all(campo in datos for campo in campos):
        return jsonify({'error': 'Faltan datos'}), 400

    # Verificar duplicados
    if Usuario.query.filter_by(email=datos['email']).first():
        return jsonify({'error': 'El email ya está registrado'}), 409
    if Usuario.query.filter_by(numero_documento=datos['numero_documento']).first():
        return jsonify({'error': 'El número de documento ya está registrado'}), 409
    if Usuario.query.filter_by(usuario=datos['usuario']).first():
        return jsonify({'error': 'El nombre de usuario ya existe'}), 409

    nuevo_usuario = Usuario(
        nombre=datos['nombre'],
        apellido=datos['apellido'],
        tipo_documento=datos['tipo_documento'],
        numero_documento=datos['numero_documento'],
        email=datos['email'],
        telefono=datos['telefono'],
        usuario=datos['usuario'],
        contrasena=datos['contrasena']  # ❗ Mejor encriptarla en producción
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)
