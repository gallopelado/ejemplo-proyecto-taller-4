from flask import Blueprint, render_template, request, redirect, url_for, session, flash

loginmod = Blueprint('login', __name__, template_folder='templates')

@loginmod.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login/index.html')
    elif request.method == 'POST':
        # recuperar el user y el pass
        user = request.form['txt_user']
        clave = request.form['txt_pass']
        if user and user == 'jj' and clave and clave == '123':
            # ir al inicio
            session['user'] = user
            if user == 'jj':
                session['rol'] = 'admin'
            elif user == 'lidia':
                session['rol'] = 'db'
            else:
                session['rol'] = 'invitado'
            return redirect(url_for('login.inicio'))
        else:
            flash('Usuario o clave incorrectos', 'warning')
            return redirect(url_for('login.index'))
    return redirect(url_for('login.index'))

@loginmod.route('/inicio')
def inicio():
    if 'user' not in session:
        return redirect(url_for('login.index'))
    return render_template('login/inicio.html')

@loginmod.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('rol', None)
    return redirect(url_for('login.index'))