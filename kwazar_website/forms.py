from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.recaptcha import RecaptchaField, Recaptcha


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Pamiętaj mnie')
    submit = SubmitField('Zaloguj się')


class PostForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    submit = SubmitField('Gotowe')


class ContactForm(FlaskForm):
    title = StringField('Temat wiadomości', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    email = StringField('E-mail kontaktowy', validators=[DataRequired(), Email(message='Podano nieprawidłowy adres e-mail')])
    picture = FileField('Zdjęcie <span class="text-muted">(pole opcjonalne)</span>', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'], message='Podany format pliku jest nieobsługiwany')])
    recaptcha = RecaptchaField('reCAPTCHA', validators=[Recaptcha()])
    submit = SubmitField('Wyślij')
