from flask import Flask, url_for, abort, redirect, render_template
from model.data import get_users

app = Flask(__name__)


# app.debug = True

@app.route('/')
@app.route('/accueil')
def accueil():
    return "<p>Page d accueil</p>"


# Variable Rules <variable_name> --> http://127.0.0.1:5000/profil/jl/20
@app.route('/profil/<string:username>/<int:age>')
def profil(username, age):
    return f"Bonjour {username} vous avez {age} ans"


# Génération des urld avec url_for()
@app.route('/contact')
def contact():
    return 'page de contact <a href="/accueil">Retour à accueil</a>'


@app.route('/contact2')
def contact2():
    return 'page de contact <a href="' + url_for("accueil") + '">Retour à accueil</a>'


@app.route("/contact3")
def contact3():
    return """<a href="%s">Retour à la page d'accueil</a>""" % \
           url_for('accueil')


# Fichier static --> Dans Flask, il est possible de stocker des fichiers dans un répertoire static, situé dans le
# même répertoire que le fichier Python définissant l’application.
@app.route("/page")
def page():
    return 'Hello <img src="' + url_for('static', filename='logo_flask.png') + '" alt="logo flask">'


# Renvoyer code HTTP avec abort()
@app.route('/protected/<int:code>')
def protected(code):
    if code == 1234:
        return "Autorisé"
    else:
        # return "Accès refusé"
        # abort(404)  # Not found
        # abort(403)  # Forbidden
        # abort(401)  # Unauthorized
        return redirect(url_for('login_default'))


# Redirection avec return rediect()
@app.route('/login_default')
def login_default():
    return "Merci de vous identifier"


# Les templates --> https://www.youtube.com/watch?v=pjqd9FNnfTo&list=PLPoGXNI6sXm6D0TKBC0dxp2f_LYfruoof&index=3
@app.route('/users')
def show_users():
    users = get_users()
    app.logger.debug(users)
    # return str(users)
    return render_template('users.html', users=users, title='Liste des utilisateurs')                    # Avec moteur de template jinja

# Héritage de template
@app.route('/heritage')
def heritage():
    users = get_users()
    return render_template('heritage.html', users=users, title='Liste des utilisateurs')


"""
if __name__ == '__main__':
    app.run()
"""
