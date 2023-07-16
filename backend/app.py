from flask import Flask, jsonify, request, session, render_template
from flask_cors import CORS
import mysql.connector
import base64
import imghdr
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


# Rutas para guardar informacion
@app.route('/api/guardarpalabras', methods=['POST'])
def crear_palabra():
    palabra = request.form.get('palabra')
    significado = request.form.get('significado')
    imagen = request.files['imagen']
    imagendata = imagen.read()

    print(palabra, significado, imagen)

    cursor = db.cursor()
    query = "INSERT INTO palabras (palabra, significado, imagen) VALUES (%s, %s, %s)"
    values = (palabra, significado, imagendata)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

        
    # Aquí puedes realizar la lógica para guardar el nuevo dato en una base de datos, por ejemplo
    return jsonify({'message': 'Dato creado exitosamente'})

@app.route('/api/guardarinfo', methods=['POST'])
def crear_info():
    informacion = request.form.get('informacion')
    significado = request.form.get('significado')
    imagen = request.files['imagen']
    imagendata = imagen.read()

    print(informacion, significado, imagen)
    db.reconnect()
    cursor = db.cursor()
    query = "INSERT INTO informacion (informacion, significado, imagen) VALUES (%s, %s, %s)"
    values = (informacion, significado, imagendata)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

        
    # Aquí puedes realizar la lógica para guardar el nuevo dato en una base de datos, por ejemplo
    return jsonify({'message': 'Dato creado exitosamente'})

@app.route('/api/guardaroracion', methods=['POST'])
def crear_oracion():
    oracion = request.form.get('oracion')
    significado = request.form.get('significado')
    imagen = request.files['imagen']
    imagendata = imagen.read()

    print(oracion, significado, imagen)

    db.reconnect()
    cursor = db.cursor()
    query = "INSERT INTO oraciones (oracion, significado, imagen) VALUES (%s, %s, %s)"
    values = (oracion, significado, imagendata)
    cursor.execute(query, values)
    db.commit()
    cursor.close()

        
    # Aquí puedes realizar la lógica para guardar el nuevo dato en una base de datos, por ejemplo
    return jsonify({'message': 'Dato creado exitosamente'})



# Ruta para enviar la informacion
@app.route('/api/palabras', methods=['GET'])
def obtenerPalabras():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT palabra, significado, imagen FROM palabras"
    cursor.execute(query)
    palabras = cursor.fetchall()
    cursor.close()
    resultado = []
    for palabra, significado, imagen in palabras: 
        imagen_base64 = base64.b64encode(imagen).decode('utf-8')
        formato_imagen = imghdr.what(None, imagen)
        resultado.append({ 'palabra': palabra, 'significado': significado, 'imagen': imagen_base64, 'formato': formato_imagen})
    print(resultado)
    response = jsonify(resultado)
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    return response

@app.route('/api/oraciones', methods=['GET'])
def obtenerOraciones():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT oracion, significado, imagen FROM oraciones"
    cursor.execute(query)
    oraciones = cursor.fetchall()
    cursor.close()
    resultado = []
    for oracion, significado, imagen in oraciones: 
        imagen_base64 = base64.b64encode(imagen).decode('utf-8')
        formato_imagen = imghdr.what(None, imagen)
        resultado.append({ 'oracion': oracion, 'significado': significado, 'imagen': imagen_base64, 'formato': formato_imagen})
    print(resultado)
    response = jsonify(resultado)
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    return response

@app.route('/api/info', methods=['GET'])
def obtenerInformacion():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT informacion, significado, imagen FROM informacion"
    cursor.execute(query)
    informacion = cursor.fetchall()
    cursor.close()
    resultado = []
    for info, significado, imagen in informacion: 
        imagen_base64 = base64.b64encode(imagen).decode('utf-8')
        formato_imagen = imghdr.what(None, imagen)
        resultado.append({ 'info': info, 'significado': significado, 'imagen': imagen_base64, 'formato': formato_imagen})
    print(resultado)
    response = jsonify(resultado)
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    return response

if __name__ == '__main__':
    app.run(port=8080)
