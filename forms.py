from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired

class ChatForm(FlaskForm):
    query = TextAreaField('query_label', validators=[InputRequired()])
    submit_button = SubmitField('send')