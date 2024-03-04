#from py.creating_map import process_geotiff, mosaick_geotiffs
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from blueprints.upload import upload_blueprint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "http://localhost:5173"}})



ALLOWED_EXTENSIONS = {'tif', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return 'Hello, World!'  # Or any other response


app.register_blueprint(upload_blueprint)

if __name__ == '__main__':
    app.run(debug=True)