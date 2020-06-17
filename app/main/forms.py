from flask_wtf import FlaskForm
from wtforms import StringField , TextAreaField,SubmitField
from wtforms.validators import Required

class SignForm(FlaskForm):

    username = StringField('username',validators=[Required()])
    password = StringField('password', validators=[Required()])
    submit = SubmitField("submit")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    category_name = StringField('Pitch Category',validators=[Required()])
    submit = SubmitField('Create')

class PitchForm(FlaskForm):
    """
    class to create a form to create pitch
    """
    pitch = StringField('Pitch',validators=[Required()])
    submit = SubmitField('Create')

class CommentForm(FlaskForm):
    """
    class to create form to comment on a pitch
    """
    comment = StringField('Comment Content', validators=[Required()])
    submit = SubmitField('Submit')