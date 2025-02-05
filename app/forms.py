from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('description',validators=[DataRequired()])

    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg','jpeg','png',],'Image Files Allowed Only.')])