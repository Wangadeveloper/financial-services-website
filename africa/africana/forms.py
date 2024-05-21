from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField,IntegerField,SelectField,FileField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from africana.models import User

class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('email',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('password',validators=[DataRequired()])
    conf_password=PasswordField('password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('submit')
    
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already taken')
        
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already taken')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Length(min=2,max=20)])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('submit')
    
class Loan_form(FlaskForm):
    first_name=StringField('name',validators=[DataRequired()])
    middle_name=StringField('name',validators=[DataRequired()])
    sir_name=StringField('name',validators=[DataRequired(),])
    id_no=IntegerField('id_no',validators=[DataRequired()])
    income=IntegerField('id_no',validators=[DataRequired()])
    county=StringField('county',validators=[DataRequired(),])
    sub_county=StringField('county',validators=[DataRequired(),])
    location=StringField('county',validators=[DataRequired(),])
    sub_location=StringField('county',validators=[DataRequired(),])
    loan_type=SelectField('loan_type',choices=['large scale','small scale',
                                               'middle income bussineses'],
                          validators=[DataRequired()])
    bussiness_type=SelectField('bussiness',choices=['school fees','farming ',
                                               'business ','asset financing','kicking poverty loan'],
                          validators=[DataRequired()])
    date=DateField('date',validators=[DataRequired()])
    gender=SelectField('gender',choices=['male','female'],validators=[DataRequired()])
    upload_id=FileField('id',validators=[DataRequired()])
    submit=SubmitField('submit')