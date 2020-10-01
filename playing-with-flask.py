#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:38:42 2020

@author: brianf
"""


from flask import Flask, url_for, redirect, render_template

auth = False

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home-page.html', names=['Brian', 'Lisa', 'BobJean'])

@app.route("/<name>/")
def user(name):
    return f'Hello {name}'

@app.route('/admin/')
def admin():
    if auth:
        return 'Welcome to the secret admin page'
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()