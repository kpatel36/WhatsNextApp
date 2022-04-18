from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_input = StringField('Search', validators=[DataRequired()])
    submit=SubmitField()

class addtoFavorites(FlaskForm):
    addtofaves=SubmitField()

class PostForm(FlaskForm):
    postbody= StringField('Create Post', validators=[DataRequired()])
    submit = SubmitField()