from flask import Blueprint, request, jsonify

# create blueprint
tareas_bp = Blueprint('tareas', __name__)

#Create a Endpoint, get tareas
@tareas_bp.route('/obtener', methods=['GET'])
def get():
    return jsonify({"Mensaje": "Estas son tus tareas"})

#Create endpoint with post getting data from the body
@tareas_bp.route('/crear', methods=['POST'])
def crear():
    
    # Obtain data from body
    data = request.get_json()
    
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    
    return jsonify({"saludo": f"Hola {nombre} {apellido} como estas?"})

# Create endpoint using PUT passing data through the body and url
@tareas_bp.route('/modificar/<int:user_id>', methods=['PUT'])
def modificar(user_id):
    
    #Get data from the bidy
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    
    mensaje = f"Usuario con id: {user_id} y nombre: {nombre} y apellido: {apellido}"
    
    return jsonify({"saludo": mensaje})