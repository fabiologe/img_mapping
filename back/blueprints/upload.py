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
    response_object = {'status': 'success'}

    if request.method == "POST":
        try:
            # Get JSON data from request body
            post_data = request.get_json()

            # Print filenames to the terminal
            print("Received filenames:", post_data.get('filenames', []))

            # Validate filenames (assuming multiple filenames are sent)
            filenames = post_data.get('filenames', [])
            for filename in filenames:
                if not allowed_marker(filename):
                    print('!!! Invalide File!!!')
                    response_object['status'] = 'error'
                    response_object['message'] = f'Invalid file extension for "{filename}"'
                    return jsonify(response_object)

            # Append filenames to the list (assuming FILENAMES is defined globally)
            FILENAMES.extend(filenames)  # Use extend to add multiple filenames

            # Update response object with success message
            response_object['message'] = f'{len(filenames)} jpg(s) added!'

        except Exception as e:
            response_object['status'] = 'error'
            response_object['message'] = str(e)

    else:  # GET request
        response_object['files'] = FILENAMES

    return jsonify(response_object)



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

