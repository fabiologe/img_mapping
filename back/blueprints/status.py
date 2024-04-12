from __future__ import print_function
from flask import Flask, request, jsonify , Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging
from py.geo_process import move_gps_jpgs, get_boundaries, add_utm

check_tiffs_blueprint = Blueprint('check_tiffs', __name__)
check_jpgs_blueprint = Blueprint('check_jpgs', __name__)



@check_jpgs_blueprint.route('/check_jpgs', methods=['GET', 'POST'])
def check_jpgs():
    """
    Checks for JPG files, sorts based on GPS presence, and returns processed data as JSON.

    Returns:
        JSON response containing data about processed JPG files, including:
            - 'jpgs': Dictionary containing information for each JPG file:
                - filename: Name of the JPG file
                - in_gps_folder (optional): Boolean indicating if in GPS directory (if returned by move_gps_jpgs)
                - error (optional): Error message for any processing errors (if returned by move_gps_jpgs)
    """
    
    jpg_dir = 'jpgs'
    gps_dir = os.path.join(jpg_dir, 'gps')
    if os.listdir(gps_dir):
        for file_name in os.listdir(gps_dir):
            file_path = os.path.join(gps_dir, file_name)
            os.remove(file_path)
    processed_data = move_gps_jpgs(jpg_dir)
    processed_data_utm = add_utm(processed_data)
    print(processed_data_utm)
    return jsonify(processed_data_utm)


@check_tiffs_blueprint.route('/check_tiffs', methods=['GET', 'POST'])
def check_tiffs():
    tiff_gk_dir = 'map_tiles/gk/'
    tiff_utm_dir = 'map_tiles/utm/'
    tiff_data = []

    # Check for TIFF files in UTM directory first
    if os.path.exists(tiff_utm_dir):
        print("\nTIFF files found in 'utm' directory:")
        for filename in os.listdir(tiff_utm_dir):
            if filename.endswith('.tif') or filename.endswith('.tiff'):
                file_path = os.path.join(tiff_utm_dir, filename)
                print(file_path)
                xy_values = get_boundaries(file_path)  # Extract XY values (you need to implement this function)
                tiff_data.append({'filename': filename, 'xy_values': xy_values})

    # If UTM directory doesn't have TIFF files, check for files in GK directory
    elif os.path.exists(tiff_gk_dir):
        print("TIFF files found in 'gk' directory:")
        for filename in os.listdir(tiff_gk_dir):
            if filename.endswith('.tif') or filename.endswith('.tiff'):
                file_path = os.path.join(tiff_gk_dir, filename)
                print(file_path)
                xy_values = get_boundaries(file_path)  # Extract XY values (you need to implement this function)
                tiff_data.append({'filename': filename, 'xy_values': xy_values})

    # Neither 'utm' nor 'gk' directory has TIFF files
    else:
        print("No TIFF files found in 'utm' or 'gk' directories.")

    #extract geodata using gdal NEEDS TO BE IMPLEMENTED !!!!
    return jsonify(tiff_data)


