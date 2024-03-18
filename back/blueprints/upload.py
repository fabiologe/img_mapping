from __future__ import print_function
from flask import Flask, request, jsonify , Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging
#from py.creating_map import mosaick_geotiffs

upload_tiff_blueprint = Blueprint('upload_tiff', __name__)
upload_jpgs_blueprint = Blueprint('upload_jpgs', __name__)
upload_update_blueprint = Blueprint('update_progress', __name__)

ALLOWED_EXTENSIONS = {'tif', 'tiff', 'geotiff'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



ALLOWED_MARKERS = {'jpg'}


def allowed_marker(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_MARKERS


@upload_jpgs_blueprint.route('/upload_jpgs', methods=['GET', 'POST'])
def upload_jpgs():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('jpg')  # List of uploaded files
        total_files = len(uploaded_files)
        uploaded_count = 0

        response_object = {'status': 'success', 'message': ''}

        if not uploaded_files:
            response_object['status'] = 'error'
            response_object['message'] = 'No files uploaded!'
            return jsonify(response_object)

        for file in uploaded_files:
            if file.filename == '':
                response_object['status'] = 'error'
                response_object['message'] = 'Empty filename detected!'
                return jsonify(response_object)

            if not allowed_marker(file.filename):
                response_object['status'] = 'error'
                response_object['message'] = f'Invalid file extension for "{file.filename}"'
                return jsonify(response_object)

            filename = secure_filename(file.filename)
            save_path = os.path.join('jpgs', filename)  # Assuming "jpgs" folder is in the same directory

            try:
                with open(save_path, 'wb') as f:
                    f.write(file.stream.read())
                uploaded_count += 1
            except Exception as e:
                logging.error(f"Error saving file '{filename}': {e}")
                continue  # Skip to the next file

        response_object['message'] = f'{uploaded_count} jpg(s) uploaded successfully!'
        return jsonify(response_object)

    else:
        print("didnt work man")
        # Handle GET requests differently if needed (e.g., return list of uploaded files)
        pass



FILENAMES = [
    {'filename' : "346664532445446564524.jpg"},
    {'filename': "dfegjefeelfef.jpg"},
    {'filename': "fhufhwfhwef.jpg"}
]












@upload_tiff_blueprint.route('/upload_tiff', methods=['GET', 'POST'])
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

