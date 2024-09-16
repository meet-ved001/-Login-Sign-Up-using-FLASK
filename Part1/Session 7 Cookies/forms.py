from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
    
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)
class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators = [DataRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    submit = SubmitField("Login")