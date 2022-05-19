from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controller.index import index_blueprint
from controller.Todo_Liste.todo_items import todo_items_blueprint

from DB.models import db

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/TodoListe"

db.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(todo_items_blueprint)

app.run(debug=True)
