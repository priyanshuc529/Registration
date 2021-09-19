from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,PasswordField
from wtforms.validators import DataRequired,Email,Length



class Info(FlaskForm):
    name = StringField(label='Name',validators=[DataRequired()],render_kw={'placeholder':'name'})
    phone = StringField(label="Phone",validators=[DataRequired()],render_kw={'placeholder':'phone'})
    Batch = SelectField(label='Batch',choices=['1st','2nd','3rd','4th'],validators=[DataRequired()],render_kw={'placeholder':'Batch'})
    Branch = SelectField(label='Branch',choices=['Visakhapatnam','Hyderabad','Bengaluru'],validators=[DataRequired()],render_kw={'placeholder':'Branch'})
    Pinnumber = StringField(label='Pin number',validators=[DataRequired()],render_kw={'placeholder':'pinnumber'})
    Department = SelectField(label='Department',choices=['Graphic Design','Content','Editor'],validators=[DataRequired()],render_kw={'placeholder':'Department'})
    email = StringField(label='Email',validators=[DataRequired(),Email(message='please enter a valid email id')])
    submit = SubmitField(label='Submit')

class Register(FlaskForm):
    name = StringField(label='name',validators=[DataRequired()])
    email = StringField(label='email',validators=[DataRequired(),Email(message='please enter valid email id')])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label='Submit')

class Login(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired()])
    password = PasswordField(label='Password')
    submit = SubmitField(label='Submit')