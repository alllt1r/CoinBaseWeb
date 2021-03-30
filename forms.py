from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class SearchForm(FlaskForm):
    """прописываю поля формы"""
    from_curr = StringField('From Currency')
    to_curr = StringField('To Currency')
    type = StringField('Type')
    submit = SubmitField('Search')