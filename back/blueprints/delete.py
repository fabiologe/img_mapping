import os
from flask import Blueprint, jsonify

# Define the blueprint
delete_jpgs_blueprint = Blueprint('delete_jpgs', __name__)

@delete_jpgs_blueprint.route('/delete_jpgs/<path:directory>', methods=['POST'])
def delete_jpgs(directory):
    try:
        # Check if the specified directory exists
        if os.path.exists(directory):
            # Remove all files from the specified directory
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                os.remove(file_path)
            return jsonify({'message': f'Temporary files in {directory} deleted successfully.'}), 200
        else:
            return jsonify({'message': f'Directory {directory} not found.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
