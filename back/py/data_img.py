import os
import re
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_date(file_path):
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        date_taken = exif_data.get(36867)  
        return date_taken
    except Exception as e:
        print(f"Error extracting date taken: {e}")
        return None




