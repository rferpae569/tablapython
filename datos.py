from flask import json
#import json json.dumps()

class Datos:
    def recibedatos(self):
        pythonDictionary = {'1':{'name':'Bob', 'age':44, 'isEmployed':True},'2':{'name':'Peter', 'age':55, 'isEmployed':False},'3':{'name':'John', 'age':33, 'isEmployed':True}}
        dictionaryToJson = json.jsonify(pythonDictionary)
        return dictionaryToJson

    def recibemostrardatos(self,datos):
        if (datos=='empleados'):
            empleados = {'1':{'name':'Bob', 'age':44, 'isEmployed':True},'2':{'name':'Peter', 'age':55, 'isEmployed':False},'3':{'name':'John', 'age':33, 'isEmployed':True}}
            a=empleados
        else:
            alumnos={'1':{'Nombre':'Pedro', 'Edad':23, 'Nota':7},'2':{'Nombre':'Francisco', 'Edad':44, 'Nota':8},'3':{'Nombre':'Alberto', 'Edad':33, 'Nota':10},'4':{'Nombre':'Alejandro', 'Edad':23, 'Nota':9},'5':{'Nombre':'Emilio', 'Edad':34, 'Nota':6.5}}
            a=alumnos
        return a