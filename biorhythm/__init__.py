from distutils.log import debug
from flask import Flask
app = Flask(__name__)
import biorhythm.views


app.config['SECRET_KEY'] = 'thisisakey'

if __name__=='__main__':
    app.run(debug = True)