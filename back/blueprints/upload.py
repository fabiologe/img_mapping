from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
#from py.creating_map import mosaick_geotiffs

upload_tiff_blueprint = Blueprint('upload_tiff', __name__)
upload_jpgs_blueprint = Blueprint('upload_jpgs', __name__)

ALLOWED_EXTENSIONS = {'tif', 'tiff', 'geotiff'}
ALLOWED_MARKERS = {'jpg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_marker(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_MARKERS

@upload_jpgs_blueprint.route('/upload_jpgs', methods=['POST'])
def upload_jpgs():
    if 'jpgs[]' not in request.files:
        return jsonify({'error': 'No file part'})

    jpg_files = request.files.getlist('jpgs[]')  # Get list of uploaded JPG files

    if len(jpg_files) < 1:
        return jsonify({'error': 'No files uploaded'})

    for jpg_file in jpg_files:
        if jpg_file.filename == '':
            return jsonify({'error': 'No selected file'})
        if jpg_file and allowed_marker(jpg_file.filename):
            filename = secure_filename(jpg_file.filename)
            file_path = os.path.join('jpgs', filename)
            jpg_file.save(file_path)  # Save each uploaded JPG file to 'back/jpgs' directory

    return jsonify({'message': 'JPG files uploaded successfully'})

@upload_tiff_blueprint.route('/upload_tiff', methods=['POST'])
def upload_tiff():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist('file')  # Get list of uploaded files

    if len(files) < 1:
        return jsonify({'error': 'No files uploaded'})

    filenames = []  # List to store filenames of uploaded files

    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join('map_tiles', filename)
            file.save(file_path)  # Save each uploaded file to 'map_tiles' directory
            filenames.append(file_path)

            output_directory = 'map_tiles/merged'
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            output_path = os.path.join(output_directory)
            shutil.move(filenames[0], output_path)
            return jsonify({'message': 'File moved to merged directory'})

''' # If more than one file was uploaded, mosaic them
    if len(filenames) > 1:
        output_directory = os.path.dirname(filenames[0])
        output_path = os.path.join(output_directory)
        mosaick_geotiffs(output_path)  # Mosaic the files
        return jsonify({'message': 'Files uploaded and mosaicked successfully'})
    if len(filenames) == 1:
        # Move the single file to the 'map_tiles/merged' directory
        output_directory = 'map_tiles/merged'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        output_path = os.path.join(output_directory)
        shutil.move(filenames[0], output_path)
        return jsonify({'message': 'File moved to merged directory'})
    else:
        return jsonify({'error': 'No files uploaded'})'''

