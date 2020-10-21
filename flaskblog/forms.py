from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, College


class RegistrationForm(FlaskForm):
    firstname = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone Number',
                           validators=[DataRequired(), Length(10)])
    roll = StringField('Roll Number',
                           validators=[DataRequired(), Length(10)])
    rank = StringField('Rank',
                           validators=[DataRequired(), Length(min=1, max=20)])
    
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_firstname(self, firstname):
        user = User.query.filter_by(firstname=firstname.data).first()
        if user:
            raise ValidationError('That firstname is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone Number',
                           validators=[DataRequired(), Length(10)])
    roll = StringField('Roll Number',
                           validators=[DataRequired(), Length(10)])
    rank = StringField('Rank',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_firstname(self, firstname):
        if firstname.data != current_user.firstname:
            user = User.query.filter_by(firstname=firstname.data).first()
            if user:
                raise ValidationError('That firstname is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    # choices = College.query.all()
    newchoices = []
    # for choice in choices:
    #     newchoices.append(choice.college_name)
    title1 = SelectField('Choice 1', validators=[DataRequired()],choices = newchoices)
    title2 = SelectField('Choice 2', validators=[DataRequired()],choices = newchoices)

    title3 = SelectField('Choice 3', validators=[DataRequired()],choices = newchoices)
    title4 = SelectField('Choice 4', validators=[DataRequired()],choices = newchoices)
    title5 = SelectField('Choice 5', validators=[DataRequired()],choices = newchoices)
    # content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
