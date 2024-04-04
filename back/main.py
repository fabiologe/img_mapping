#from py.creating_map import process_geotiff, mosaick_geotiffs
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from blueprints.upload import upload_tiffs_blueprint, upload_jpgs_blueprint, FILENAMES
from blueprints.status import check_jpgs_blueprint, check_tiffs_blueprint
from blueprints.download import serve_jpgs_blueprint, serve_tiffUTM_blueprint
from blueprints.delete import delete_jpgs_blueprint
from flask import Flask
from flask_cors import CORS
from database.perm_save import save_project_blueprint, list_projects_blueprint, load_perm_jpgs_blueprint
from bson import Binary

vue_path = "http://localhost:5173"
app = Flask(__name__)
CORS(app, resources={
    r"/upload_tiffs": {"origins": vue_path},
    r"/upload_jpgs": {"origins": vue_path},
    r"/check_tiffs":{"origins":vue_path},
    r"/check_jpgs":{"origins":vue_path},
    r"/serve_jpgs":{"origins":vue_path},
    r"/serve_tiffUTM":{"origins":vue_path},
    r"/delete_jpgs/*":{"origins":vue_path},
    r"/perm_save":{"origins": vue_path},
    r"/list_projects":{"origins": vue_path},
    r"/load_perm_jpgs/*": {"origins": vue_path}

})




@app.route('/')
def index():
    return jsonify(FILENAMES)  # Or any other response

app.register_blueprint(save_project_blueprint)
app.register_blueprint(list_projects_blueprint)
app.register_blueprint(load_perm_jpgs_blueprint)
app.register_blueprint(upload_tiffs_blueprint)
app.register_blueprint(upload_jpgs_blueprint)
app.register_blueprint(check_jpgs_blueprint)
app.register_blueprint(check_tiffs_blueprint)
app.register_blueprint(serve_jpgs_blueprint)
app.register_blueprint(serve_tiffUTM_blueprint)
app.register_blueprint(delete_jpgs_blueprint)

if __name__ == '__main__':
    app.run(debug=True)