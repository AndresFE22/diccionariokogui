from flask import Flask, jsonify, request, session, render_template
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)
app.secret_key = 'mi_clave_secreta'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="diccionariokogui"
)

if db.is_connected():
        print("La conexión a la base de datos se estableció correctamente")
else:    
        print("La conexión a la base de datos no se pudo establecer")



@app.route('/')
def inicio():
    return ''

# Ruta de ejemplo para obtener datos
@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    datos = [
        {'id': 1, 'nombre': 'Ejemplo 1'},
        {'id': 2, 'nombre': 'Ejemplo 2'},
        {'id': 3, 'nombre': 'Ejemplo 3'}
    ]
    response = jsonify(datos)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    return response

# Ruta de ejemplo para crear datos
@app.route('/api/datos', methods=['POST'])
def crear_dato():
    palabra = request.form.get('palabra')
    significado = request.form.get('significado')
    imagen = request.files['imagen']

    print(palabra, significado, imagen)
        
    # Aquí puedes realizar la lógica para guardar el nuevo dato en una base de datos, por ejemplo
    return jsonify({'message': 'Dato creado exitosamente'})

if __name__ == '__main__':
    app.run()

@app.route('/imagen')
def verimagen():
    imagen = session.get('imagen') 
    # Aquí puedes realizar la lógica para guardar el nuevo dato en una base de datos, por ejemplo
    return render_template('imagen', imagen=imagen)