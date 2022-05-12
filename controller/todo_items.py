from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from DB.models import db, Todoitem


todo_items_blueprint = Blueprint('todo_items_blueprint', __name__)


@todo_items_blueprint.route("/todo_items")
def show_todo_items():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    todo_items = session.query(Todoitem)
    
    return render_template("TodoItems/todo_items.html", todo_items = todo_items)


@todo_items_blueprint.route("/todo_items/show_description")
def show_todo_item_description():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    todo_items = session.query(Todoitem)
    
    return render_template("TodoItems/todo_items_description.html", todo_items = todo_items)


@todo_items_blueprint.route("/todo_items/edit")
def edit_todo_items():
    pass


@todo_items_blueprint.route("/todo_items/delete")
def delete_todo_items():
    pass
