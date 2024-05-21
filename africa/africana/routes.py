from flask import Flask,render_template,url_for,redirect,request,flash,make_response
from africana.forms import RegistrationForm,LoginForm,Loan_form
from africana.models import User
from africana import app,bcrypt,db 
import google.generativeai as genai
import os


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        enc_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=enc_password)
        db.session.add(user)
        db.session.commit()
        flash('acount created succesfully!',category='success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('login succesfully!',category='success')
        return redirect(url_for('home'))
    return render_template('login.html',form=form)


@app.route('/borrow_wisely',methods=['GET','POST'])
def borrow():
    form=Loan_form()
    if form.validate_on_submit():
        os.environ['GOOGLE_API_KEY']="AIzaSyBlDP16OreX4EQPXNYMQL_7lVEJgpxRsDI"
        genai.configure(api_key = os.environ['GOOGLE_API_KEY']) 
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f'advice me on what amount of {form.bussiness_type.data} loan to apply in kenya having a monthly income of kenya shillings {form.income.data},and {form.loan_type.data} bussines')
        return render_template('wanga_ai.html',response=response)
    return render_template('loan.html',form=form)

    