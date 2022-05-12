from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class Add_item_form(FlaskForm):
    item_ID = StringField("item_ID")
    item_name = StringField("item_name")
    item_description = StringField("item_description")
