from flask import Flask


def create_app():

    app = Flask(__name__)

    # from . import _config
    # app.config['SQLALCHEMY_DATABASE_URI'] = _connect_str
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # from . import models
    # models.db.init_app(app)

    @app.route('/')
    def index():
        return "hello, Petfax"

    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)
    
    return app

   