import os
import asyncio
import shutil
from flask import Flask, render_template, request, jsonify, flash, url_for
import requests
from gtts import gTTS
from text_standardized import remove_special_chars, encode_string

import time


app = Flask(__name__)
app.config['SECRET_KEY'] = "caas-srk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
