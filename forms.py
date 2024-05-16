from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import InputRequired

class ChatForm(FlaskForm):
    query = TextAreaFieldField('query_label', validators=[InputRequired()])
    submit_button = SubmitField('submit_label')