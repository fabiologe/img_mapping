from flask import Blueprint, request, jsonify
import os
from bson import Binary, ObjectId
from py.data_img import get_date
from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
import io
import piexif

save_project_blueprint = Blueprint('perm_save', __name__)  # Removed slash from blueprint name
list_projects_blueprint = Blueprint('list_projects', __name__)
perm_save_jpgs_blueprint = Blueprint('perm_save_jps',__name__)
load_perm_jpgs_blueprint = Blueprint('load_perm_jpgs', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mongodb']
files_collection = db['project']  # Used consistent collection name
grid_fs = GridFS(db)

@save_project_blueprint.route('/perm_save', methods=['POST'])
def save_project():
    try:
        # Get the project name from the request body
        project_name = request.json.get('project_name')
        print(f"Received project name: {project_name}")
        # Save project data to MongoDB
        result = files_collection.insert_one({'project_name': project_name})

        print(f"Inserted document ID: {result.inserted_id}")
        save_jpgs_to_mongodb(project_name)

        # Respond with the received project name as JSON
        return jsonify({'project_name': project_name}), 200
    except Exception as e:
        # Respond with an error message
        print(f'Error: {str(e)}')
        return jsonify({'error': str(e)}), 500




@list_projects_blueprint.route('/list_projects', methods=['GET'])
def list_projects():
    try:
        # Retrieve all documents from the 'project' collection
        projects = files_collection.find({}, {'_id': 0, 'project_name': 1})
        
        # Extract project names from documents
        project_names = [project['project_name'] for project in projects]
        
        # Return project names as JSON response
        return jsonify({'projects': project_names}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def save_jpgs_to_mongodb(project_name):
    try:
        # Directory paths for JPGs
        jpgs_directories = ['jpgs/gps', 'jpgs/no_gps']
        
        for directory in jpgs_directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith('.jpg'):
                        file_path = os.path.join(root, file)
                        # Open JPEG file with PIL
                        with Image.open(file_path) as img:
                            # Extract EXIF data
                            exif_data = img.info.get("exif")
                            
                            # Compress the image with JPEG compression
                            compressed_img = io.BytesIO()
                            img.save(compressed_img, format='JPEG', quality=70, exif=exif_data)  # Preserve EXIF data
                            compressed_img.seek(0)
                            
                            # Store the compressed image in GridFS
                            file_id = grid_fs.put(compressed_img, filename=file)
                            
                            # Save file ID and path to MongoDB
                            files_collection.update_one(
                                {'project_name': project_name},
                                {'$addToSet': {'jpgs': {'file_name': file, 'file_path': file_path, 'file_id': file_id}}},
                                upsert=True
                            )
                        print(f"Added {file} to project {project_name}")
    except Exception as e:
        print(f'Error saving JPEGs: {str(e)}')


@load_perm_jpgs_blueprint.route('/load_perm_jpgs/<path:project_name>', methods=['GET', 'POST', 'OPTIONS'])
def load_perm_jpgs(project_name):
    try:    
        # Query MongoDB to retrieve the project document based on the project name
        project = db.project.find_one({'project_name': project_name})
        if not project:
            return jsonify({'error': 'Project not found'}), 404
        
        # Extract the 'jpgs' field from the project document
        jpgs = project.get('jpgs', [])
        
        # Iterate through the jpgs array
        for jpg in jpgs:
            file_id = jpg.get('file_id')
            # Retrieve the file from GridFS using the file ID
            file_doc = db.fs.files.find_one({'_id': ObjectId(file_id)})
            if not file_doc:
                return jsonify({'error': 'File not found'}), 404
            
            # Get the filename from the file document
            file_name = file_doc.get('filename')

            # Retrieve file data from GridFS
            file_data = b""
            for chunk in db.fs.chunks.find({'files_id': file_id}).sort('n'):
                file_data += chunk.get('data')

            # Save the file data to the desired folder
            with open(os.path.join(os.getcwd(), 'jpgs', file_name), 'wb') as f:
                f.write(file_data)
        
        return jsonify({'message': 'JPEG files loaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
