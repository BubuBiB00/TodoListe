from flask.templating import render_template
from flask import Blueprint, request, redirect
import sqlalchemy

from DB.models import db, Todoitem
from forms.add_item_form import Add_item_form

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


@todo_items_blueprint.route("/todo_items/add", methods = ["GET","POST"])
def add_todo_items():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    item = session.query(Todoitem).all()
    
    add_item_form = Add_item_form()
    
    if request.method == "POST":
        if add_item_form.validate_on_submit():
            item = Todoitem()
            item.item_name = add_item_form.item_name.data
            item.item_description = add_item_form.item_description.data
            
            db.session.add(item)
            db.session.commit()
            
            return redirect("/todo_items")
    
    else:
        return render_template("TodoItems/add_todo_item.html", form = add_item_form)
    
    
@todo_items_blueprint.route("/todo_items/edit")
def edit_todo_items():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    edit_item_form = Add_item_form()
    
    item_id = request.args["item_ID"]
    item_to_edit = session.query(Todoitem).filter(Todoitem.item_ID == item_id).first()
    
    if request.method == "POST":
        if edit_item_form.validate_on_submit():
            item_to_edit = item_to_edit = session.query(Todoitem).filter(Todoitem.item_ID == item_id).first()
            
            item_to_edit.item_ID = edit_item_form.item_ID.data
            item_to_edit.item_name = edit_item_form.item_name.data
            item_to_edit.item_description = edit_item_form.item_description.data
            
            
            db.session.commit()
        return redirect("/todo_items")
    else:
        edit_item_form.item_ID.data = item_to_edit.item_ID
        edit_item_form.item_name.data = item_to_edit.item_name
        edit_item_form.item_description.data = item_to_edit.item_description
        
        return render_template("TodoItems/add_todo_item.html", form = edit_item_form)
         
@todo_items_blueprint.route("/todo_items/delete")
def delete_todo_items():
    pass
