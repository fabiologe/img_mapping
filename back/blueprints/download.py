from __future__ import print_function
import os
from flask import Blueprint, send_from_directory, request



serve_jpgs_blueprint = Blueprint("serve_jpgs",__name__)
serve_tiffUTM_blueprint = Blueprint("serve_tiffUTM", __name__)

@serve_jpgs_blueprint.route('/serve_jpgs', methods=['POST'])
def serve_jpgs():
    data = request.get_json()
    filename = data.get('filename')
    images_directory = 'jpgs/gps'
    return send_from_directory(images_directory, filename)

@serve_tiffUTM_blueprint.route('/serve_tiffUTM', methods=['POST'])
def serve_tiffUTM():
    data = request.get_json()
    filename = data.get('filename')
    tiff_directory = 'map_tiles/utm'
    return send_from_directory(tiff_directory, filename)