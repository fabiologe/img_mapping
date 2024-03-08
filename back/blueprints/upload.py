from flask import Flask, request, jsonify, Response, Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging
#from py.creating_map import mosaick_geotiffs

upload_tiff_blueprint = Blueprint('upload_tiff', __name__)
upload_jpgs_blueprint = Blueprint('upload_jpgs', __name__)
upload_update_blueprint = Blueprint('update_progress', __name__)

ALLOWED_EXTENSIONS = {'tif', 'tiff', 'geotiff'}
ALLOWED_MARKERS = {'jpg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_marker(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_MARKERS

# Endpoint to serve progress updates to the client
@upload_update_blueprint.route('/upload_progress')
def upload_progress():
    return Response(generate_progress(), content_type='text/event-stream')


def generate_progress(files):
    total_files = len(files)
    uploaded_count = 0

    for jpg_file in files:
        if jpg_file.filename == '':
            return jsonify({'error': 'No selected file'})

        if jpg_file and allowed_marker(jpg_file.filename):
            filename = secure_filename(jpg_file.filename)
            file_path = os.path.join('jpgs', filename)
            
            try:
                with open(file_path, 'wb') as f:
                    f.write(jpg_file.stream.read())
            except Exception as e:
                # Log the error
                logging.error(f"Error saving file '{filename}': {e}")
                continue  # Continue with the next file
            
            uploaded_count += 1
            
            # Calculate progress percentage
            progress = int((uploaded_count / total_files) * 100)
            
            # Send real-time progress update to the client
            yield f"data: {progress}\n\n"

@upload_jpgs_blueprint.route('/upload_jpgs', methods=['POST'])
def upload_jpgs():
    files = request.files.getlist('jpg')
    return Response(generate_progress(files), content_type='text/event-stream')














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

