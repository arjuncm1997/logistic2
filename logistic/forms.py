from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,IntegerField, DateField,SelectField,HiddenField, TextField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from logistic.models import Materials, Login,Offer, Credit ,Pay



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Login.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = Login.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Account(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[Email()])
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')




class Material(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    avail = StringField('Avail quantity', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    gst = StringField('GST in %', validators=[DataRequired()])
    place = StringField('Place', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('Submit')

class Offers(FlaskForm):
    name = StringField('Offer Name',
                        validators=[DataRequired()])
    price = StringField('Discount Price')
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])

    def get_all_materials():
        return Materials.query

    matname=QuerySelectField('Material Name',query_factory=get_all_materials,get_label="name")

    submit = SubmitField('Submit')




class Materialedit(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    avail = StringField('Avail quantity')
    price = StringField('Price')
    gst = StringField('GST in %')
    gstprice = StringField('GST in %')
    netprice = StringField('Netprice')
    offerprice = StringField('Offer Price')
    place = StringField('Place')
    pic = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    owner = StringField('Owner')
    submit = SubmitField('Approve')

class Reject(FlaskForm):
    reject = TextAreaField('reason',
                        validators=[DataRequired()])
    submit = SubmitField('Reject')

class Cart(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('ADD TO CART')

class Cart1(FlaskForm):
    value = IntegerField(validators=[DataRequired()])
    submit = SubmitField('continue')

class Cartaddress(FlaskForm):
    name = StringField('Name',render_kw={"placeholder":"NAME"},
                        validators=[DataRequired()])
    phone = StringField('Mobile',render_kw={"placeholder":"MOBILE"})
    address = StringField('Delivery Address',render_kw={"placeholder":"DELIVERY ADDRESS"},
                        validators=[DataRequired()])
    submit = SubmitField('continue')


class Cod(FlaskForm):
    submit = SubmitField('Make a payment')

class Purchaseview(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
                        
    submit = SubmitField('submit')

class Purchaseview2(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    date = DateField('Date',format='%m/%d/%Y',render_kw={"placeholder":"mm/dd/yyyy"})
    submit = SubmitField('submit')

class Purchaseview3(FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired()])
    date = DateField('Date',format='%m/%d/%Y',render_kw={"placeholder":"mm/dd/yyyy"},
                        validators=[DataRequired()])
    submit = SubmitField('submit')

class Creditcard(FlaskForm):
    name = StringField('Name',render_kw={"placeholder":"Name"},
                        validators=[DataRequired()])
    number = StringField('number',render_kw={"placeholder":".... .... .... ...."},validators=[DataRequired()])
    cvv = StringField(' cvv',render_kw={"placeholder":"..."},
                        validators=[DataRequired()])
    date = StringField('date',render_kw={"placeholder":"MM/YY"},
                        validators=[DataRequired()])
    submit = SubmitField('Make A Payment')

class Paypal(FlaskForm):
    number = StringField('number',render_kw={"placeholder":"xxxx xxxx xxxx xxxx"},
                        validators=[DataRequired()])
    name = StringField('Name',render_kw={"placeholder":"Name"},validators=[DataRequired()])
    cvv = StringField(' cvv',render_kw={"placeholder":"xxx"},
                        validators=[DataRequired()])
    date = StringField('date',render_kw={"placeholder":"MM/YY"},
                        validators=[DataRequired()])
    submit = SubmitField('Proceed Payment')



class Changepassword(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',
                                     validators=[ EqualTo('password')])
    submit = SubmitField('Reset Password')


class Reset(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = Login.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class Changepassword(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',
                                     validators=[ EqualTo('password')])
    submit = SubmitField('Reset Password')