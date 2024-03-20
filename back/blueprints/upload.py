from __future__ import print_function
from flask import Flask, request, jsonify , Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging
#from py.creating_map import mosaick_geotiffs

upload_tiffs_blueprint = Blueprint('upload_tiffs', __name__)
upload_jpgs_blueprint = Blueprint('upload_jpgs', __name__)

FILENAMES_TIF = []
ALLOWED_EXTENSIONS = {'tif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_tiffs_blueprint.route('/upload_tiffs',methods = ['GET', 'POST'])
def upload_tiffs():
    if request.method == 'POST':
        uploaded_tiffs = request.files.getlist('tif')  # List of uploaded files
        total_files = len(uploaded_tiffs)
        uploaded_count = 0

        response_object = {'status': 'success', 'message': ''}

        if not uploaded_tiffs:
            response_object['status'] = 'error'
            response_object['message'] = 'No files uploaded!'
            return jsonify(response_object)

        for file in uploaded_tiffs:
            if file.filename == '':
                response_object['status'] = 'error'
                response_object['message'] = 'Empty filename detected!'
                return jsonify(response_object)

            if not allowed_marker(file.filename):
                response_object['status'] = 'error'
                response_object['message'] = f'Invalid file extension for "{file.filename}"'
                return jsonify(response_object)

            filename = secure_filename(file.filename)
            save_path = os.path.join('map_tiles', filename)  

            try:
                with open(save_path, 'wb') as f:
                    f.write(file.stream.read())
                uploaded_count += 1
            except Exception as e:
                logging.error(f"Error saving file '{filename}': {e}")
                continue  # Skip to the next file

        response_object['message'] = f'{uploaded_count} tiff(s) uploaded successfully!'
        return jsonify(response_object)

    else:
        print("didnt work man")
        # Handle GET requests differently if needed (e.g., return list of uploaded files)
        pass



ALLOWED_MARKERS = {'jpg'}


def allowed_marker(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_MARKERS


@upload_jpgs_blueprint.route('/upload_jpgs', methods=['GET', 'POST'])
def upload_jpgs():
    if request.method == 'POST':
        uploaded_jpgs = request.files.getlist('jpg')  # List of uploaded files
        total_files = len(uploaded_jpgs)
        uploaded_count = 0

        response_object = {'status': 'success', 'message': ''}

        if not uploaded_jpgs:
            response_object['status'] = 'error'
            response_object['message'] = 'No files uploaded!'
            return jsonify(response_object)

        for file in uploaded_jpgs:
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

