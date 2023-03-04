from flask import Blueprint

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/getalumn', methods = ['GET'])
def getalumn():
    return {'key': 'Alumnos'}

@alumnos.route('/savealumn', methods = ['GET'])
def savealumn():
    return {'key': 'Alumnos Guardar'}

#__INIT__ RECONOCE LAS CARPETAS COMO MODULOS Y CREA AUTO. EL PAQUETE __PYCHACHE__