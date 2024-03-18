#from py.creating_map import process_geotiff, mosaick_geotiffs
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from blueprints.upload import upload_tiff_blueprint, upload_jpgs_blueprint, upload_update_blueprint, FILENAMES
from flask import Flask
from flask_cors import CORS
vue_path = "http://localhost:5173"
app = Flask(__name__)
CORS(app, resources={
    r"/upload_tiffs": {"origins": vue_path},
    r"/upload_jpgs": {"origins": vue_path}
})




@app.route('/')
def index():
    return jsonify(FILENAMES)  # Or any other response


app.register_blueprint(upload_tiff_blueprint)
app.register_blueprint(upload_jpgs_blueprint)
app.register_blueprint(upload_update_blueprint)

if __name__ == '__main__':
    app.run(debug=True)