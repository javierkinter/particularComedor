import os
from flask import Flask, session
from route import route
 
def main():
    app = Flask(__name__,template_folder='templates',static_folder='static')

    app.config['SECRET_KEY'] = 'comedor'  


    route(app)
    app.run('0.0.0.0', 5001, debug=True) 
main()