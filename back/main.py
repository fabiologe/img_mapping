from py.creating_map import process_geotiff, mosaick_geotiffs
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from blueprints.upload import upload_blueprint

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'tif', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

app.register_blueprint(upload_blueprint)

if __name__ == '__main__':
    app.run(debug=True)