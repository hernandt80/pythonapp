from flask import Flask, render_template

from base import models

from usuarioapppackagegeo import nav

#Configuracion aplicacion
app = Flask(__name__, template_folder= 'htmls')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/postgres'
models.db.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('home.html')


# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.nav import mod_user as user_module
from app.base.nav import mod_base as base_module
from usuarioapppackagegeo.nav import mod_geo as geo_module

# Register blueprint(s)
app.register_blueprint(base_module)
app.register_blueprint(user_module)
app.register_blueprint(geo_module)
# app.register_blueprint(xyz_module)
# ..


if __name__ == '__main__':
    app.run(debug=True)
