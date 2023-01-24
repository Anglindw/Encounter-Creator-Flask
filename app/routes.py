from app import app
from flask import Flask, render_template, Blueprint

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/ogl')
def ogl():
    return render_template('ogl.html')