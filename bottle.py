#!usr/bin/env python3
# -*- enconding: utf-8 -*-

import os
from bottle import get, post, request # or route
#Aplicação Web em Desenvolvimento para fins didáticos
#Autor: Dieferson Soares
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="Nome" type="text" />
            Password: <input name="Senha" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Suas informações de login foi correta.</p>"
    else:
        return "<p>falha no login.</p>"

run(host='localhost', port=8080, debug=True)


