from flask import Flask,render_template,request
from datetime import datetime
from datos import Datos
import sys
# app = Flask(__name__,template_folder='plantillas',static_folder='otronombre')
app=Flask(__name__,)

@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template("index.html",year=datetime.now().year,message="Elije una opción")

@app.route('/datos')
def datos():
    mostrar=Datos()
    dictionaryToJson=mostrar.recibedatos()
    return dictionaryToJson


@app.route('/mostrardatos/<datos>')
def mostrardatos(datos):
    mostrar=Datos()
    return render_template("mostrardatos.html",year=datetime.now().year,message="Opciones",datos=mostrar.recibemostrardatos(datos))

@app.route('/multiplica',methods=['GET'])
def formulario():
  #Comprobamos si viene el parámetro por GET
   try:
        numero2 = request.args.get('numero')
 
        if (numero2 == None):
               return render_template('formulario_get.html',year=datetime.now().year,message="Opciones")
        else:
           if (int(numero2) >= 0):
               return render_template('multiplica.html',numero=int(numero2),year=datetime.now().year,message="Opciones")
           else:
               raise Exception("El número no puede ser negativo") #esto se controlaría desde el formulario, es por ver cómo lanzar excepciones
   except:
        return render_template('error.html',error=sys.exc_info()[1])

@app.route('/saludar',methods=['GET'])
def saludo():
    nombre=request.args.get('nombre')
    return f'Hola {nombre} !!!'

if __name__=='__main__':
    app.debug = True
    app.run()