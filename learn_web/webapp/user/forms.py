from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Submit", render_kw={"class": "btn btn-primary"})

    remember_me = BooleanField(
        "Stay signed in", default=True, render_kw={"class": "form-check-input"}
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"},
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    password2 = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"class": "form-control"},
    )

    submit = SubmitField(
        "Create account!", render_kw={"class": "btn btn-primary"}
    )

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError("Username taken")

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError(
                f"Account with email {email.data} already registered"
            )
