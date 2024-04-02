from flask import Blueprint, request, jsonify
import os
from py.data_img import get_date
from pymongo import MongoClient

save_project_blueprint = Blueprint('perm_save', __name__)  # Removed slash from blueprint name

client = MongoClient('mongodb://localhost:27017/')
db = client['mongodb']
files_collection = db['files']  # Used consistent collection name

@save_project_blueprint.route('/perm_save', methods=['POST'])
def save_project():
    try:
        # Get the project name from the request body
        project_name = request.json.get('project_name')
        print(f"Received project name: {project_name}")

        # Respond with the received project name as JSON
        return jsonify({'project_name': project_name}), 200
    except Exception as e:
        # Respond with an error message
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500




list_projects_blueprint = Blueprint('list_projects', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mongodb']
files_collection = db['files']

@list_projects_blueprint.route('/list_projects', methods=['GET'])
def list_projects():
    try:
        # Aggregate to get the count of files for each project
        pipeline = [
            {"$group": {"_id": "$project_name", "count": {"$sum": 1}}},
            {"$project": {"_id": 0, "project_name": "$_id", "file_count": "$count"}}
        ]
        projects = list(files_collection.aggregate(pipeline))
        return jsonify({'projects': projects}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
