######################################################################################
#                          AQUI SE CREAR EL PROYECTO BIOMEC                          #
######################################################################################

from flask import Flask
from config import Config              # traemos las configuraciones del archivo => config.py
from flask_wtf.csrf import CSRFProtect # para la proteccion del login, importante crear la SECRET_KEY

csrf = CSRFProtect()                           # creamos una instancia para la proteccion para login   => csrf

#######################################################################################
# Creando el proyecto, con las rutas de las carpetas las cuales estan en => config.py #
#######################################################################################
servi_tec = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
servi_tec.config.from_object(Config)
csrf.init_app(servi_tec)


#####################################################################################
#                                 RUTAS                                             #
#     Aqui se llama a las rutas imprimiendo su template, osea la VISTA en la WEB    #
#####################################################################################

# biomec.register_blueprint(global_scope, url_prefix="/")
# biomec.register_blueprint(tipo_scope,url_prefix ="/tipo")
# biomec.register_blueprint(seguro_scope,url_prefix ="/seguro")
# biomec.register_blueprint(personal_scope,url_prefix ="/personal")
# biomec.register_blueprint(laboratorista_scope,url_prefix ="/laboratorista")
# biomec.register_blueprint(especialidad_scope,url_prefix ="/especialidad")
# biomec.register_blueprint(privilegio_scope,url_prefix ="/privilegio")
# biomec.register_blueprint(paciente_scope,url_prefix ="/paciente")