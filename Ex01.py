# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:48:03 2022

@author: watson
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "這個是首頁"

@app.route("/news")
def hotnews():
    return "新聞頁面"

@app.route("/message")
def msg():
    return "訊息頁"


app.run()






    