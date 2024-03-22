from __future__ import print_function
from flask import Flask, request, jsonify , Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging
from py.check_gps import move_gps_jpgs

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
    processed_data = move_gps_jpgs(jpg_dir)
    print(processed_data)
    return jsonify(processed_data)


@check_tiffs_blueprint.route('/check_tiffs',methods = ['GET', 'POST'])
def check_tiffs():
    pass