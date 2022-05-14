#all the imports
import flask
from app import app,engine
import pandas as pd
from flask import render_template, request, redirect, url_for,flash
from app.models import User
from app import db
from flask_login import login_user, logout_user

#tentativa de passar o mysql.connect deu erro
#tentar passar para o SQLALquemy para o login
#o login continuar dando um redirect errado...
#register consegue logar corretamente 
#tentar ver o debug do Flask para encontrar o erro...

query_select_password = 'SELECT password FROM users WHERE email=%(email)s'

@app.route('/', methods=['GET', 'POST'])
def first_page():
    return render_template('start_page.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        user = User(name=name, email=email, password=pwd)
        db.session.add(user)
        db.session.commit()
        if name and email and pwd:
           return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':    
        email = request.form['email']
        pwd = request.form['password']
        try:
            df = pd.read_sql_query(query_select_password, engine, params={'email' : email})
            user = User.query.filter_by(email=email).first() 
            #if not user or not user.verify_password(pwd):
            if df['password'][0] == pwd:
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Login ou senha invalido")
                return redirect(url_for('login'))
        except:
            flash("Usuario ou senha incorreta")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home') #caso nao tenha methods ele pega GET
def home():
    return render_template('home.html')

#chamada para o terminal do flask 
@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )

#@app.route('/logout', methods=['GET', 'POST'])
#def logout():
#    if request.method == 'POST':
#        if request.form['email'] == 'M123@gmail.com' and request.form['password'] == 'M123':
#            return redirect(url_for('home'))
#    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

















# ==== DECORETOR ====
#def calcular_tempo(funcao):
#    def wrapper():
#        funcao()
#    return wrapper

