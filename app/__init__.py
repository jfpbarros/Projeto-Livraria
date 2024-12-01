#quando coloco init, eu crio um módulo.  e inicia por ele.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
crsf = CSRFProtect()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    crsf.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    login.login_view='login'

    with app.app_context():
        from . import routes, models
        db.create_all()

        @login.user_loader
        def load_user(user_id):
            return models.User.query.get(int(user_id))
        
        return app



