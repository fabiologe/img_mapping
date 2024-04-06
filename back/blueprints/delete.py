import os
from flask import Blueprint, jsonify, request

delete_jpgs_blueprint = Blueprint('delete_jpgs', __name__)

@delete_jpgs_blueprint.route('/delete_jpgs', methods=['POST'])
def delete_jpgs():
    directory = request.json.get('directory')
    print(directory)
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            # Check if the file is a JPEG
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                # Construct the full file path
                filepath = os.path.join(directory, filename)
                # Delete the file
                os.remove(filepath)
        return 'JPEG files deleted successfully', 200
    except Exception as e:
        return str(e), 500
