from flask import Flask, request, render_template
import pickle
#import requests
import json
from sets import Set
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def notify():
	if request.method == 'GET':
                return render_template('404.html'), 404
	if request.method == 'POST':
                return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
