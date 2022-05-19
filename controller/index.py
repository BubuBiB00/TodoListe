from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from DB.models import db


index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route("/")
def index():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    return render_template("index.html")
