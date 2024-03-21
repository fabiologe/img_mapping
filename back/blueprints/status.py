from __future__ import print_function
from flask import Flask, request, jsonify , Blueprint
from werkzeug.utils import secure_filename
import os
import shutil
import logging

check_tiffs_blueprint = Blueprint('check_tiffs', __name__)
check_jpgs_blueprint = Blueprint('check_jpgs', __name__)

@check_tiffs_blueprint.route('/check_tiffs',methods = ['GET', 'POST'])
def check_tiffs():
    pass

@check_jpgs_blueprint.route('/check_jpgs',methods = ['GET', 'POST'])
def check_jpgs():
    pass