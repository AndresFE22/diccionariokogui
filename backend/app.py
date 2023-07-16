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

# Ruta de ejemplo para obtener datos
@app.route('/api/palabras', methods=['GET'])
def obtenerPalabras():
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

# Ruta de ejemplo para crear datos
@app.route('/api/datos', methods=['POST'])
def crear_dato():
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

if __name__ == '__main__':
    app.run(port=8080)
