from flask import Flask, jsonify, request, session, render_template, Response
from flask_cors import CORS
import mysql.connector
import base64
import imghdr
import json

app = Flask(__name__)
CORS(app)
app.secret_key = 'mi_clave_secreta'

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

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


#Rutas para editar la informacion

#imprimirpalabras
@app.route('/api/showtable', methods=['GET'])
def showpalabras():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT id, palabra, significado FROM palabras"
    cursor.execute(query)
    palabras = cursor.fetchall()
    cursor.close()
    print(palabras)
    json_data = json.dumps(palabras, cls=CustomJSONEncoder)
    response = Response(json_data, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    print(response)
    return response

if __name__ == '__main__':
    app.run(port=8080)

#eliminar palabras
@app.route('/api/palabras/<int:id>', methods=['DELETE'])
def eliminar_palabra(id):
    db.reconnect()
    cursor = db.cursor()
    query = "DELETE FROM palabras WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'Palabra eliminada correctamente'})

#editar palabras
@app.route('/api/palabras/<int:id>', methods=['PUT'])
def editar_palabra(id):

    nueva_palabra = request.json.get('palabra')
    nuevo_significado = request.json.get('significado')
    print(nueva_palabra, nuevo_significado)

    db.reconnect()
    cursor = db.cursor()
    query = "UPDATE palabras SET palabra = %s, significado = %s WHERE id = %s"
    cursor.execute(query, (nueva_palabra, nuevo_significado, id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'Palabra eliminada correctamente'})

#mandar imagen de palabras
@app.route('/api/palabras/<int:id>/image', methods=['GET'])
def imagen_palabras(id):
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT imagen FROM palabras WHERE id = %s"
    cursor.execute(query, (id,))
    imagen = cursor.fetchone()[0]
    cursor.close()
    imagen_base64 = base64.b64encode(imagen).decode('utf-8')
    formato_imagen = imghdr.what(None, imagen)
    response = jsonify({
        'imagen_base64': imagen_base64,
        'formato_imagen': formato_imagen
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#imprimiroraciones
@app.route('/api/showtableo', methods=['GET'])
def showoraciones():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT id, oracion, significado FROM oraciones"
    cursor.execute(query)
    oraciones = cursor.fetchall()
    cursor.close()
    print(oraciones)
    json_data = json.dumps(oraciones, cls=CustomJSONEncoder)
    response = Response(json_data, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    print(response)
    return response

if __name__ == '__main__':
    app.run(port=8080)

#eliminar oraciones
@app.route('/api/oraciones/<int:id>', methods=['DELETE'])
def eliminar_oracion(id):
    db.reconnect()
    cursor = db.cursor()
    query = "DELETE FROM oraciones WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'Palabra eliminada correctamente'})

#editar oraciones
@app.route('/api/oraciones/<int:id>', methods=['PUT'])
def editar_oracion(id):

    nueva_oracion = request.json.get('oracion')
    nuevo_significado = request.json.get('significado')
    print(nueva_oracion, nuevo_significado)

    db.reconnect()
    cursor = db.cursor()
    query = "UPDATE oraciones SET oracion = %s, significado = %s WHERE id = %s"
    cursor.execute(query, (nueva_oracion, nuevo_significado, id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'Palabra editada correctamente'})

#mandar imagen de oraciones
@app.route('/api/oraciones/<int:id>/image', methods=['GET'])
def imagen_oracion(id):
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT imagen FROM oraciones WHERE id = %s"
    cursor.execute(query, (id,))
    imagen = cursor.fetchone()[0]
    cursor.close()
    imagen_base64 = base64.b64encode(imagen).decode('utf-8')
    formato_imagen = imghdr.what(None, imagen)
    response = jsonify({
        'imagen_base64': imagen_base64,
        'formato_imagen': formato_imagen
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#imprimir informacion
@app.route('/api/showtablei', methods=['GET'])
def showoinfo():
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT id, informacion, significado FROM informacion"
    cursor.execute(query)
    informacion = cursor.fetchall()
    cursor.close()
    print(informacion)
    json_data = json.dumps(informacion, cls=CustomJSONEncoder)
    response = Response(json_data, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')  # Agregar el encabezado
    print(response)
    return response

if __name__ == '__main__':
    app.run(port=8080)

#eliminar informacion
@app.route('/api/info/<int:id>', methods=['DELETE'])
def eliminar_informacion(id):
    db.reconnect()
    cursor = db.cursor()
    query = "DELETE FROM informacion WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'informacion eliminada correctamente'})

#editar oraciones
@app.route('/api/info/<int:id>', methods=['PUT'])
def editar_informacion(id):

    nueva_info = request.json.get('informacion')
    nuevo_significado = request.json.get('significado')
    print(nueva_info, nuevo_significado)

    db.reconnect()
    cursor = db.cursor()
    query = "UPDATE informacion SET informacion = %s, significado = %s WHERE id = %s"
    cursor.execute(query, (nueva_info, nuevo_significado, id,))
    db.commit()
    cursor.close()
    
    return jsonify({'message': 'info editada correctamente'})

#mandar imagen de oraciones
@app.route('/api/info/<int:id>/image', methods=['GET'])
def imagen_informacion(id):
    db.reconnect()
    cursor = db.cursor()
    query = "SELECT imagen FROM informacion WHERE id = %s"
    cursor.execute(query, (id,))
    imagen = cursor.fetchone()[0]
    cursor.close()
    imagen_base64 = base64.b64encode(imagen).decode('utf-8')
    formato_imagen = imghdr.what(None, imagen)
    response = jsonify({
        'imagen_base64': imagen_base64,
        'formato_imagen': formato_imagen
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response